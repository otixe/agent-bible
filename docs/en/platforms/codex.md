# Codex (OpenAI Codex CLI)

*Last reviewed: 2026-10-26.*

**Where the letter goes:** an `AGENTS.md` file in the folder where you run Codex. Codex reads instruction files at the start of a session; a user-level file also exists, but is not the place for this.

## Steps

1. **Create a new, empty folder** for this agent.
2. Save the letter as `AGENTS.md` in that folder.
3. Start Codex from that folder with the **`read-only` sandbox** and `approval_policy = on-request` (use `/permissions` to check or change them). Say hello.
4. Expect questions, not work. Answer, read the SOUL the agent proposes, correct it, confirm.
5. The agent writes `SOUL.md` next to `AGENTS.md`. Because instruction files may not import each other, add this line at the end of `AGENTS.md`:

```text
At the start of every session, read SOUL.md in this folder and follow it.
```

## Where the SOUL lives

`SOUL.md` in the agent's folder.

## Limits and watch-outs

- Instruction files are combined under a **size budget of 32 KiB (32,768 bytes) by default**, shared by the whole discovered chain. The single-agent letter is about 9 KB and the team-lead letter about 13.7 KB (UTF-8, see [sizes](README.md#how-long-are-the-letters)), so they fit alone; but a global `AGENTS.md` plus files from parent folders count against the same budget, and Codex stops adding files once the cap is reached. Keep the folder isolated and check, in the first reply, that the agent follows the protocol to the end.
- Codex is a coding agent with shell and file tools. The **approval mode** is what actually restrains it; the letter only asks.
- `~/.codex/AGENTS.md` (user-level) applies everywhere. Do not put the letter there.

## Confirmed in the official documentation (consulted 2026-10-26)

| Fact | Source |
| --- | --- |
| **Size cap:** 32 KiB = 32,768 **bytes** by default, configurable with `project_doc_max_bytes`. It is a *combined* budget for the discovered chain, not characters and not a quota per file. | [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) |
| **Discovery and merge:** global file first (`AGENTS.override.md`, else `AGENTS.md`, first non-empty one); then from the project root down to the working directory, **at most one file per directory**, concatenated with blank lines, closer instructions last. If no project root is found, only the working directory. Built at the start of each run or session. | [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) |
| **Approval policy:** `on-request`, `never` or a granular object. `untrusted` is not supported and `on-failure` is deprecated. (Do not confuse the retired `approval_policy = untrusted` with `projects.<path>.trust_level = untrusted`, which is still documented.) | [Configuration reference](https://developers.openai.com/codex/config-reference), [Approvals & security](https://developers.openai.com/codex/agent-approvals-security) |
| **Sandbox:** `read-only`, `workspace-write`, `danger-full-access`. These are separate from the approval policy: `never` removes prompts but does **not** grant full access or remove the sandbox. Full access/bypass is not a recommendation here. | same two pages |

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
