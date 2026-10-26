# Claude Projects

*Last reviewed: 2026-10-26.*

**Where the letter goes:** the project's **Instructions**. They apply to every conversation inside the project, which is exactly what you want.

## Steps

1. In Claude, create a **new project** and give it the agent's working name (you will rename it after first run).
2. Open the project's instructions and **paste the whole letter**.
3. Optional: upload the [Golden Rules](../../../reglas/en/GOLDEN-RULES.md) and the [Harness](../../../harness/en/HARNESS-SOLO-AGENT.md) as project files, so you can point to them later. The letter already contains them.
4. Start a conversation in the project and say hello. Expect questions, not work (see [First run](../reading-your-agent/first-run.md)).
5. Answer, read the SOUL it prints, correct it, and confirm.
6. **Save the SOUL:** add it to the project instructions *below the letter* (or upload it as a project file named `SOUL.md` and tell the agent in the instructions to read it first). Then rename the project.

## Where the SOUL lives

In the project: instructions or a project file. The agent cannot write it for you. Whenever the SOUL changes, you update that copy.

## Limits and watch-outs

- Instructions and project files share the model's context window with the conversation. A very long letter plus many files leaves less room for the work.
- Projects are for repeated work with shared context; the agent has **no tools** you did not connect. Keep connectors off until the SOUL declares a need.
- Platform memory features (if enabled) are separate from the SOUL and not controlled by the letter. Check what is remembered, and delete what should not be.
- Sharing a project shares its instructions. Keep it private to the responsible human.

## Confirmed in the official documentation (consulted 2026-10-26)

- **Availability:** traditional Projects are available to all users, Free included (Free: at most 5 projects); sharing with Team/Enterprise is subject to admin settings ([create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), [personalization](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features), [what are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)).
- **A newer Projects version (beta)** is rolling out selectively to Pro/Max, first to Claude Code users and some migrations of existing projects; the guide says other plans and surfaces follow. Do not assume you have it: this page describes traditional Projects ([what are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)).

## Not documented — check it yourself

- **A maximum length for project instructions** is not published in the official pages consulted. Do not borrow `CLAUDE.md` limits from Claude Code, and do not read the context window or retrieval behaviour as an instruction cap. Paste the letter and, in the first reply, confirm the agent really starts with the questions.

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
