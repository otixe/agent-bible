# Real first-boot evidence / Evidencia real de primer arranque

**Four current letters, four real clean first replies: PASS in producer review. Independent QA is pending.** Each individual letter produces four numbered startup groups; each leader letter adds only the fifth about the existing team. No reply assumes a name, personality or work role, starts work, proposes creating agents or calls tools.

**Cuatro cartas vigentes, cuatro respuestas reales limpias: revisión del productor PASS; QA independiente pendiente.** Cada carta individual pregunta cuatro temas; la de líder añade el equipo. La pregunta 2 pide nombre o alias, trato, zona horaria y límites del humano. La 4 pregunta herramientas, permisos, memoria y ubicación/permiso para SOUL.md. Ninguna respuesta se inventa identidad o se pone a trabajar o crear agentes.

## Current cases

| Letter | First response | Entire input + first reply | Configuration and hashes |
| --- | --- | --- | --- |
| [Solo ES](../carta/es/CARTA-AGENTE-SOLO.md) | [Response](es-solo/first-response.txt) | [Transcript](es-solo/transcript.md) | [Result](es-solo/result.json) |
| [Leader ES](../carta/es/CARTA-LIDER-DE-EQUIPO.md) | [Response](es-leader/first-response.txt) | [Transcript](es-leader/transcript.md) | [Result](es-leader/result.json) |
| [Solo EN](../carta/en/LETTER-SOLO-AGENT.md) | [Response](en-solo/first-response.txt) | [Transcript](en-solo/transcript.md) | [Result](en-solo/result.json) |
| [Leader EN](../carta/en/LETTER-TEAM-LEAD.md) | [Response](en-leader/first-response.txt) | [Transcript](en-leader/transcript.md) | [Result](en-leader/result.json) |

Model: Amazon Bedrock `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, thinking off. Tested Pi build: **1.4.0**. Final model calls began 2026-10-26 at 13:48 UTC. Results record the original run timestamp separately from later artifact evaluation.

## What “clean” means here

Every model call gets its own new Pi process, working directory and agent configuration directory. No conversation is restored. Context files, tools, extensions, MCP, skills, prompt templates, themes, approval integration and session persistence are disabled. The requested system prompt is neutral: `You are an AI assistant.` The sole user input is the whole unmodified letter, matched to the recorded user message and SHA256. There are zero tool executions.

The environment is allowlisted: basic process settings plus authorized AWS model authentication settings. Office/Cerebro keys are not inherited. HOME may remain inherited for the authorized AWS provider chain; this is **not an empty-HOME container, kernel sandbox or claim of network isolation**. “Offline” suppresses runtime discovery/update activity, not the remote Bedrock inference. No credentials, account IDs, runtime session IDs, local private paths or hidden reasoning are published. Transcript labels and surrounding explanations are added by the recorder; USER and ASSISTANT text are not edited.

## Reproduce

Use a compatible Pi build supporting all flags in [run_clean_boot.py](run_clean_boot.py), on PATH, and your own authorized AWS model credentials. Do not silently drop unknown isolation flags. This runner's environment allowlist is AWS-specific.

```sh
python3 evidencia/run_clean_boot.py carta/es/CARTA-AGENTE-SOLO.md
python3 evidencia/run_clean_boot.py carta/es/CARTA-LIDER-DE-EQUIPO.md
python3 evidencia/run_clean_boot.py carta/en/LETTER-SOLO-AGENT.md
python3 evidencia/run_clean_boot.py carta/en/LETTER-TEAM-LEAD.md
python3 evidencia/verify_artifacts.py
```

Fresh calls use paid remote inference. Preserve existing evidence before rerunning: the runner updates the selected current case only after its checks pass. Raw events/stderr remain in the private temporary directory reported by the runner. `--events` reevaluates an existing original event log without a new model call; **independent QA must run fresh, without that option**, and inspect the full first response itself. A replay of our logs is not independent behavioral testing.

## Acceptance and verifier corrections

We accept the four/five startup groups and their required subjects, no assumed identity/role, no work or agent creation, no tool actions, and the correct memory/location question. A neutral question/protocol heading or the copied “only these questions, no actions” instruction is framing, not role adoption. Early format-only checks rejected such harmless framing; the verifier was corrected and the **same original replies** reevaluated. No changed answer or successful retry conceals that issue.

Nine actual inference requests were made: four final cases and five preserved earlier-version cases. Earlier versions remain under each case's `before-explicit-human-name/`; the first ES leader also remains under `es-leader/before-format/`. Changes were one extra blank line removed for Markdown lint, then explicit human name/alias in question 2. Final letters were tested afresh after edits. This is not nine independent trials of one unchanged prompt or a statistical reliability claim.

- [Producer semantic review](producer-review.json): not independent approval.
- [Offline integrity/structure checks](integrity.json): exact letter, response and transcript bindings; twelve rules and full Harness inline; four negative controls rejected.
- [Measured sizes](sizes.json): Unicode code points including newlines and UTF-8 bytes, **not tokens**. All four letters exceed 8,000 characters; do not assume they fit short instruction fields or truncate them.
- [Source/adaptation map](SOURCE-MAP.md).
- [Local Markdown lint](markdownlint.txt): 48 files, zero errors; verbatim evidence is excluded by the repository configuration.
- [Relative link targets](local-links.json): local existence only, not external HTTP or fragment validity.
- [Sanitization report](sanitization.json): measured checks, not a guarantee that arbitrary future content is safe.
- [Owned-file seal](file-sha256.json): excludes itself; any byte change requires revalidation.

## Limits

Only the first response was tested, on one model and one runtime configuration. We did not test the later SOUL draft/write/confirmation, filesystem persistence, real team operation, privilege enforcement, production actions or any other platform's UI. A letter is instructions, not executable RBAC. GitHub CI, independent QA and publication have not run as part of this delivery.
