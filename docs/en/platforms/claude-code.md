# Claude Code

*Last reviewed: 2026-10-26.*

**Where the letter goes:** a `CLAUDE.md` file in the folder where you run the agent. Claude Code reads it at the start of the session.

## Steps

1. **Create a new, empty folder** for this agent (not a code repository; not inside one that already has a `CLAUDE.md` above it).
2. Save the letter as `CLAUDE.md` in that folder.
3. Start Claude Code from that folder in **`default` (also called Manual) or `plan` permission mode**, not in a mode that auto-approves. Say hello.
4. Expect questions, not work. Answer, then read the SOUL the agent proposes. It should **show it to you before writing the file**.
5. When you confirm, the agent writes `SOUL.md` in the same folder. Add one line at the end of `CLAUDE.md` so every later session loads it:

```text
@SOUL.md
```

Write that line as plain text **outside any backticks or code fence** in your real `CLAUDE.md` (it is shown in a fence here only to explain it; imports are not expanded inside code spans or fences). The path is relative to the file that imports it. If your version does not expand it, write instead: "At the start of every session, read SOUL.md and follow it."

## Where the SOUL lives

`SOUL.md` in the agent's folder. Back it up like any file; keep the previous version when it changes.

## Limits and watch-outs

- Claude Code is a **coding agent** with file and shell tools. The letter tells it not to act before the first-run questions, but only the permission mode *stops* it from writing or running things. Start with approvals on; loosen them one at a time.
- A user-level `~/.claude/CLAUDE.md` applies to every project you open. Do **not** put the letter there.
- Files in parent folders are loaded too; that is why the folder should be empty and isolated.
- Instructions in a folder are text the agent reads. Do not drop a letter you did not read into a folder you use.

## Confirmed in the official documentation (consulted 2026-10-26)

| Fact | Source |
| --- | --- |
| **Imports:** `@path/to/import` in `CLAUDE.md`; relative or absolute paths, relative paths resolved from the importing file; **at most four hops** of recursive imports. Not expanded inside code spans or fences; spaces must be escaped with a backslash; a quoted path is not imported. Imports from outside the project need per-project approval. | [How Claude remembers your project](https://code.claude.com/docs/en/memory) |
| **Permission modes:** `default` (Manual), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. `default` reads without asking; `acceptEdits` also allows edits and common filesystem commands; `auto` reviews in the background; `dontAsk` denies what it would otherwise ask; `bypassPermissions` skips permission checks and is for isolated environments only. **A mode is not a sandbox or an access-control list**, and `plan` is not a guarantee of zero effects. | [Choose a permission mode](https://code.claude.com/docs/en/permission-modes) |

Not documented in the sources consulted: a size limit for `CLAUDE.md`; do not assume one, and do not carry it over to Claude Projects.

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
