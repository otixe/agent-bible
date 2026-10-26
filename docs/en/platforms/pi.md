# pi

*Last reviewed: 2026-10-26 (against pi's own documentation: configuration, security and CLI pages).*

**Where the letter goes:** `AGENTS.md` (or `CLAUDE.md`) in the folder where you run pi. pi loads such **context files** from its agent directory, the working directory and its **parent directories**.

## Steps

1. **Create a new, empty folder** for this agent, in a place whose parent folders have no `AGENTS.md` / `CLAUDE.md` of their own (or run once with `--no-context-files` to see the difference).
2. Save the letter as `AGENTS.md` in that folder.
3. Run `pi` from that folder. Say hello. Expect questions, not work.
4. Answer; read and confirm the SOUL. The agent writes `SOUL.md` in the folder.
5. Add this line at the end of `AGENTS.md`: "At the start of every session, read SOUL.md in this folder and follow it." After editing context files, `/reload` loads them without restarting.

## Two other places, and when to use them

| File | Effect | Use it when |
| --- | --- | --- |
| `.pi/APPEND_SYSTEM.md` | Adds your text to pi's system prompt | You want the letter at system level, not as a context file. Needs the project to be trusted. |
| `.pi/SYSTEM.md` | **Replaces** pi's default system prompt | Rarely. You lose pi's own tool guidance. |
| `<agent-dir>/AGENTS.md` | Applies to *every* folder you run pi in | **Not for this.** The letter would reach every project. |

## Where the SOUL lives

`SOUL.md` in the agent's folder.

## Limits and watch-outs

- **Context files load regardless of project trust.** pi's security notes say to treat instructions in a folder as untrusted input. Only use a letter you read yourself.
- pi has file and shell tools running with your operating-system permissions. The letter asks the agent to wait; permissions and your attention are what stop it. Use a separate folder (or container) with nothing valuable in it for the first runs.
- Files in parent directories are also loaded, so a parent `AGENTS.md` can change the agent's behaviour.

## Source

Checked on 2026-10-26 against the documentation shipped with pi 1.4 (the *configuration*, *security* and *CLI* pages). It is the source for your version: file names, loading order and trust rules can change between versions.
