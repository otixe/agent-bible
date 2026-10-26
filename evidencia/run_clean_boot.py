#!/usr/bin/env python3
"""Real first-response test with a fresh, tool-free Pi process per letter.
Requires an installed Pi CLI and authorized ambient AWS model credentials.
No office credentials or private runtime logs are published. Not a sandbox for
provider software; the model itself has no executable tools. Successful response
syntax is checked here; a human must also inspect semantics and non-assumption.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

if not __debug__:
    raise RuntimeError('Run without -O; assertions must remain enabled')
parser = argparse.ArgumentParser()
parser.add_argument('letter', help='Path relative to the repository root')
parser.add_argument('--model', default='us.anthropic.claude-sonnet-4-5-20250929-v1:0')
parser.add_argument('--provider', default='amazon-bedrock')
parser.add_argument('--events', type=Path, help='Re-evaluate original private events; no new model call')
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
letter = (repo / args.letter).resolve()
assert letter.is_relative_to(repo) and letter.is_file()
body = letter.read_text(encoding='utf-8')
sha = hashlib.sha256(letter.read_bytes()).hexdigest()
pi = shutil.which('pi')
assert pi, 'Install Pi before running this test'
private = Path(tempfile.mkdtemp(prefix='agent-bible-clean-'))
cwd = private / 'cwd'
agent = private / 'agent'
cwd.mkdir()
agent.mkdir()
# Only model-provider credentials may be inherited, never office/Cerebro keys.
allow = {'PATH', 'HOME', 'LANG', 'LC_ALL', 'TZ', 'AWS_PROFILE', 'AWS_REGION',
         'AWS_DEFAULT_REGION', 'AWS_CONFIG_FILE', 'AWS_SHARED_CREDENTIALS_FILE',
         'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_SESSION_TOKEN',
         'AWS_BEARER_TOKEN_BEDROCK'}
env = {key: value for key, value in os.environ.items() if key in allow}
env.update(PI_CODING_AGENT_DIR=str(agent), PI_SKIP_VERSION_CHECK='1',
           PI_TELEMETRY='0', PI_OFFLINE='1')
assert set(env) <= allow | {'PI_CODING_AGENT_DIR', 'PI_SKIP_VERSION_CHECK', 'PI_TELEMETRY', 'PI_OFFLINE'}
flags = ['--mode', 'json', '--no-tools', '--no-extensions', '--no-mcp',
         '--no-skills', '--no-prompt-templates', '--no-themes', '--no-context-files',
         '--no-approve', '--no-session', '--offline', '--system-prompt',
         'You are an AI assistant.', '--provider', args.provider, '--model', args.model,
         '--thinking', 'off']
if args.events:
    stdout = args.events.read_text(encoding='utf-8')
    assert (args.events.parent / 'agent').is_dir() and (args.events.parent / 'cwd').is_dir()
    agent = args.events.parent / 'agent'
    print('Re-evaluating original first response; no new model call')
else:
    result = subprocess.run([pi, *flags], cwd=cwd, env=env, input=body,
                            capture_output=True, text=True, timeout=150)
    (private / 'events.jsonl').write_text(result.stdout, encoding='utf-8')
    (private / 'stderr.txt').write_text(result.stderr, encoding='utf-8')
    print('Private raw logs:', private)
    assert result.returncode == 0, 'Pi failed; inspect private stderr; no public PASS emitted'
    stdout = result.stdout
assert not list(agent.rglob('*.jsonl')), 'Unexpected session persistence'
events = [json.loads(line) for line in stdout.split('\n') if line.strip()]
messages = [event['message'] for event in events if event.get('type') == 'message_end']
users = [m for m in messages if m.get('role') == 'user']
assistants = [m for m in messages if m.get('role') == 'assistant']
assert len(users) == len(assistants) == 1, 'Exactly one input and first assistant message required'
user_text = users[0]['content']
if isinstance(user_text, list):
    user_text = ''.join(block.get('text', '') for block in user_text if block.get('type') == 'text')
assert user_text.strip() == body.strip(), 'Input is not the unmodified letter'
message = assistants[0]
assert message.get('provider') == args.provider, 'Unexpected provider'
assert message.get('stopReason') not in ['error', 'aborted', 'length'], 'Incomplete/error reply'
assert not any(e.get('type', '').startswith('tool_execution') for e in events)
assert not any(block.get('type') == 'toolCall' for block in message['content'])
reply = ''.join(block.get('text', '') for block in message['content'] if block.get('type') == 'text')
# One numbered group per question. No preamble or identity document before them.
leader = 'LIDER' in letter.name or 'LEAD' in letter.name
expected = list(range(1, 6 if leader else 5))
numbered = re.findall(r'^\s*(?:\*\*)?(\d+)[.)]', reply, re.M)
assert [int(x) for x in numbered] == expected, ('Question groups', numbered)
# A neutral protocol title is not an assumed identity or an executed task.
question_body = re.sub(r'^\s*#{1,3}\s*(?:Protocolo de primer arranque|First[- ]boot (?:protocol|questions)|Arranque[ \t—-]+Preguntas de identidad y equipo)\s*\n+', '', reply, count=1, flags=re.I)
question_body = re.sub(r'^\s*Mi primera respuesta es únicamente estas preguntas(?:, sin realizar acciones)?:\s*\n+', '', question_body, count=1)
question_body = re.sub(r'^\s*My first response consists only of these questions(?:; I do not take action yet|, without taking action):\s*\n+', '', question_body, count=1)
assert re.match(r'^\s*(?:\*\*)?1[.)]', question_body), 'First response has a non-protocol preamble'
assert 'SOUL.md' in reply and '?' in reply, 'Memory/identity location must be asked, not assumed'
assert not re.search(r'(?i)(?:me llamo|my name is|soy tu (?:asistente|líder)|i am your (?:assistant|leader))', reply)
assert not re.search(r'(?mi)^#{1,3}\s+(?:SOUL|Identidad|Identity)', reply)
record = dict(schema_version=1, tested_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              letter=str(letter.relative_to(repo)), letter_sha256=sha, provider=args.provider,
              model=message.get('model', args.model), requested_model=args.model,
              clean_agent_directory=True, fresh_process=True, prior_messages=0,
              tools_enabled=[], context_files=False, extensions=False, mcp=False,
              skills=False, prompt_templates=False, session_persisted=False,
              system_prompt_requested='You are an AI assistant.',
              office_credentials_inherited=False, tool_executions=0,
              input_is_entire_letter=True, first_message_only=True,
              numbered_question_groups=expected,
              verifier_version=4, original_events_reevaluated=bool(args.events),
              original_run_timestamp=events[0].get('timestamp'),
              neutral_protocol_heading_allowed=True, neutral_protocol_instruction_allowed=True,
              syntax_checks='PASS',
              semantic_review='PENDING producer review; independent QA still required',
              stop_reason=message.get('stopReason'),
              usage_tokens={k: v for k, v in message.get('usage', {}).items() if k in ['input', 'output', 'cacheRead', 'cacheWrite', 'totalTokens']},
              flags=flags, response_sha256=hashlib.sha256(reply.encode('utf-8')).hexdigest())
slug = letter.parent.name + '-' + ('leader' if leader else 'solo')
output = repo / 'evidencia' / slug
output.mkdir(parents=True, exist_ok=True)
(output / 'first-response.txt').write_text(reply, encoding='utf-8')
(output / 'result.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
transcript = '# Real clean first-boot transcript\n\n'
transcript += f'Letter: `{record["letter"]}`\n\nSHA256: `{sha}`\n\n'
transcript += f'Provider/model: `{args.provider}/{record["model"]}`\n\n'
transcript += 'The USER message below is the whole, unmodified letter. The ASSISTANT message is its first response; no follow-up or corrected answer is substituted. Private runtime paths, credentials and streamed reasoning are not included.\n\n'
transcript += '## USER\n\n' + body + '\n## ASSISTANT — first message\n\n' + reply + '\n'
(output / 'transcript.md').write_text(transcript, encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
print('FIRST RESPONSE:\n' + reply)
