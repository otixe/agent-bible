#!/usr/bin/env python3
"""Offline checks for the exact delivered letters and their real transcripts.
This checks artifact integrity and structure, not model safety or translation.
Run without model credentials: python3 evidencia/verify_artifacts.py
"""
import hashlib
import json
from pathlib import Path
import re

if not __debug__:
    raise RuntimeError('Run without -O; assertions must remain enabled')
ROOT = Path(__file__).resolve().parents[1]
CASES = {
    'es-solo': ('carta/es/CARTA-AGENTE-SOLO.md', 'reglas/es/REGLAS-DE-ORO.md', 'harness/es/HARNESS-AGENTE-SOLO.md', 4),
    'es-leader': ('carta/es/CARTA-LIDER-DE-EQUIPO.md', 'reglas/es/REGLAS-DE-ORO.md', 'harness/es/HARNESS-OFICINA.md', 5),
    'en-solo': ('carta/en/LETTER-SOLO-AGENT.md', 'reglas/en/GOLDEN-RULES.md', 'harness/en/HARNESS-SOLO-AGENT.md', 4),
    'en-leader': ('carta/en/LETTER-TEAM-LEAD.md', 'reglas/en/GOLDEN-RULES.md', 'harness/en/HARNESS-OFFICE.md', 5),
}


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def check_response(reply, count):
    numbered = [int(x) for x in re.findall(r'^\s*(?:\*\*)?(\d+)[.)]', reply, re.M)]
    assert numbered == list(range(1, count + 1)), numbered
    assert 'SOUL.md' in reply and '?' in reply
    assert not re.search(r'(?i)(?:me llamo|my name is|soy tu (?:asistente|líder)|i am your (?:assistant|leader))', reply)
    assert not re.search(r'(?mi)^#{1,3}\s+(?:SOUL|Identidad|Identity)', reply)


def check_bound_input(body, result):
    assert digest(body) == result['letter_sha256'], 'Letter changed since inference'


def run():
    checked = []
    for case, (letter, rules, harness, count) in CASES.items():
        body = (ROOT / letter).read_text(encoding='utf-8')
        record = json.loads((ROOT / 'evidencia' / case / 'result.json').read_text())
        check_bound_input(body, record)
        assert record['letter'] == letter and record['prior_messages'] == 0
        assert record['tools_enabled'] == [] and record['tool_executions'] == 0
        assert record['fresh_process'] and record['clean_agent_directory']
        assert record['input_is_entire_letter'] and record['first_message_only']
        assert not record['office_credentials_inherited'] and not record['session_persisted']
        for flag in ['context_files', 'extensions', 'mcp', 'skills', 'prompt_templates']:
            assert record[flag] is False, flag
        assert record['syntax_checks'] == 'PASS'
        reply = (ROOT / 'evidencia' / case / 'first-response.txt').read_text(encoding='utf-8')
        assert digest(reply) == record['response_sha256']
        check_response(reply, count)
        transcript = (ROOT / 'evidencia' / case / 'transcript.md').read_text(encoding='utf-8')
        assert '## USER\n\n' + body + '\n## ASSISTANT — first message\n\n' + reply + '\n' in transcript
        public_rules = '1. **' + (ROOT / rules).read_text(encoding='utf-8').split('1. **', 1)[1]
        assert [int(x) for x in re.findall(r'^(\d+)\. \*\*', public_rules, re.M)] == list(range(1, 13))
        assert public_rules.strip() in body, 'Rules are not self-contained'
        method = (ROOT / harness).read_text(encoding='utf-8')
        method = '## ' + method.split('\n## ', 1)[1]
        assert method.strip() in body, 'Harness is not self-contained'
        protocol = body.rsplit('## ', 1)[1]
        assert [int(x) for x in re.findall(r'^(\d+)\. \*\*', protocol, re.M)] == list(range(1, count + 1))
        checked.append({'case': case, 'letter_sha256': digest(body), 'response_sha256': digest(reply), 'question_groups': count})

    # Control negatives prove these checks fail rather than merely printing PASS.
    sample = (ROOT / 'evidencia/es-solo/first-response.txt').read_text(encoding='utf-8')
    sample_record = json.loads((ROOT / 'evidencia/es-solo/result.json').read_text())
    body = (ROOT / sample_record['letter']).read_text(encoding='utf-8')
    negatives = [
        ('changed input', lambda: check_bound_input(body + '\nchanged', sample_record)),
        ('assumed identity', lambda: check_response('Me llamo Inventado.\n' + sample, 4)),
        ('missing question', lambda: check_response(sample.replace('4. **', '9. **'), 4)),
        ('wrong leader coverage', lambda: check_response(sample, 5)),
    ]
    for name, check in negatives:
        try:
            check()
        except AssertionError:
            continue
        raise AssertionError('False green for negative control: ' + name)
    return {'current_cases': checked, 'integrity_and_structure': 'PASS',
            'negative_controls_rejected': [name for name, _ in negatives],
            'limitations': 'Not independent QA; no safety or translation guarantee.'}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
