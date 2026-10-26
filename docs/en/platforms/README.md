# Platforms: where the letter goes

Almost every agent platform has the same few places to configure an agent, under different names. Find the one that holds **instructions applied to every conversation** — that is where the letter goes.

| This manual says | Usual names in platforms |
| --- | --- |
| **Instructions** (the letter goes here) | "instructions", "system prompt", "project instructions", "persona", "context file", "rules" |
| **Knowledge** | "knowledge", "files", "documents", "project knowledge", "reference documents" |
| **Tools / actions** | "tools", "actions", "connectors", "plugins", "integrations", "MCP servers" |
| **Sharing / permissions** | "share", "access", "roles", "approval mode", "sandbox" |
| **Memory** | "memory", "persistent context"; if absent, a document you maintain |

## At a glance

*Last reviewed: 2026-10-26. Each page ends with what was **confirmed in the official documentation** (with links) and what is **not documented**. "Not documented" means no published figure — it does not mean unlimited. Evidence and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).*

| Platform | Where the letter goes | Can the agent save its own SOUL? | Main watch-out |
| --- | --- | --- | --- |
| [Claude Projects](claude-projects.md) | Project instructions | No — you save it | Instruction cap not documented; a newer beta version is rolling out selectively |
| [ChatGPT](chatgpt.md) | Project instructions, or a custom GPT's Instructions field | No — you save it | Account-wide Custom Instructions are far too small (1,500–5,000 characters); project and GPT caps are not documented |
| [Claude Code](claude-code.md) | `CLAUDE.md` in an empty folder | Yes, as a file | The agent has file and shell tools — start in `default` or `plan` mode; a mode is not a sandbox |
| [Codex](codex.md) | `AGENTS.md` in an empty folder | Yes, as a file | 32 KiB combined budget for instruction files; sandbox and approval are separate controls |
| [pi](pi.md) | `AGENTS.md` (or `.pi/APPEND_SYSTEM.md`) in an empty folder | Yes, as a file | Context files from parent folders also load |
| [Gemini](gemini.md) | Gem "Instructions"; `GEMINI.md` in the CLI | Gem: no. CLI: yes | Gems cannot write files; keep the SOUL as text |
| [Amazon Quick](amazon-quick.md) | Agent profile → Instructions | No — you save it | Instruction cap is not documented (the 100,000 figure is for uploaded documents); skip the "generate" template |
| [Other tools](other-tools.md) | Rules / instructions file or system prompt | Depends | Check the eight questions below |
| Nothing fits | First message of a new conversation | No — you save it | Works only for that conversation |

## How long are the letters?

Measured on the files in this repository (Unicode characters including line breaks; bytes are UTF-8; **not tokens**). Source: [`evidencia/sizes.json`](../../../evidencia/sizes.json).

| Letter | Characters | Bytes |
| --- | ---: | ---: |
| [Single agent, English](../../../carta/en/LETTER-SOLO-AGENT.md) | 8,543 | 8,577 |
| [Single agent, Spanish](../../../carta/es/CARTA-AGENTE-SOLO.md) | 8,959 | 9,115 |
| [Team lead, English](../../../carta/en/LETTER-TEAM-LEAD.md) | 13,201 | 13,227 |
| [Team lead, Spanish](../../../carta/es/CARTA-LIDER-DE-EQUIPO.md) | 13,510 | 13,721 |

**Every letter is longer than 8,000 characters.** Do not assume it fits a short instructions field, and do not trim it to make it fit: a letter with missing rules or a missing first-boot protocol is a different, untested text. If a field has a cap below the letter's size, use one of the [fallbacks](chatgpt.md#fallback-when-the-letter-is-longer-than-the-field): the whole letter as an attached file with a short pointer in the instructions, or the whole letter as the first message of a conversation. In both cases check in the first reply that the agent really started with the questions. The rules and the Harness alone are small ([rules](../../../reglas/en/GOLDEN-RULES.md) ≈ 3,000 characters, [single-agent Harness](../../../harness/en/HARNESS-SOLO-AGENT.md) ≈ 2,900) if you want to attach them separately.

## Two families, two ways to keep the SOUL

**Chat platforms** (Claude Projects, ChatGPT, Gemini Gems, Quick). The agent cannot write files. At the end of the first run it *prints* its SOUL; you save it by pasting it into the platform's instructions (under the letter) or uploading it as a knowledge file, as the page explains. If you do not, the next conversation starts with no memory of who the agent is.

**Folder-based agents** (Claude Code, Codex, pi, Gemini CLI). The agent runs in a folder and, if you allow file writes and name the place in question 4, saves `SOUL.md` there (never somewhere it invented; it does not overwrite earlier files). The letter lives in the folder's instruction file; from the second session on, the agent reads its SOUL at start. **Use an empty folder dedicated to this agent**, not a code repository, and not a folder inside a parent that already has its own instruction files.

## Eight questions before you choose or configure a platform

| Question | Why it matters |
| --- | --- |
| Where are data processed and stored, and for how long? | Privacy rules apply to what you put in front of the agent. |
| Are conversations or files used to train the provider's models? Can you turn that off? | Confidentiality. |
| Can you limit sources and actions per agent? | Least privilege (Golden Rule 5). |
| Do actions with side effects ask you for confirmation before running? | Rules 1 and 2. If not, the *letter* must demand it, and you must test it. |
| Is there an activity log you can read? | Traceability (Rule 8). |
| What is the maximum length of the instructions? | Decides whether the letter fits or needs the fallback. |
| Is there persistent memory, and can you see and delete it? | Controlled learning. |
| Does it integrate with your organisation's sign-in? | So that the agent's human is who they say they are. |

## Configuration rules that apply everywhere

1. **Enable only what the SOUL declares.** Every source and every action should match a function written in the SOUL.
2. **Start read-only.** Turn on actions with side effects one at a time, after you have tested them.
3. **Do not share the agent** beyond its responsible human without a new decision.
4. **Write down the configuration you applied**, so you can compare it with the SOUL later.
5. **If the platform lacks a control** — for example, confirmation before an action — that control is written into the SOUL and tested. Its absence does not remove the rule.
6. **If the letter does not fit**, keep these in this order: Golden Rules, identity and limits, Harness, style. Put examples and detail in an attached document.
