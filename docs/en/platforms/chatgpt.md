# ChatGPT

*Last reviewed: 2026-10-26.*

You have three places. Prefer the first. Note that the official text indexed on 2026-10-26 says creating and publishing *new* GPTs is not available on personal Free/Go/Plus/Pro accounts, so the custom-GPT route may not be open to you.

| Route | Where the letter goes | Good for | Problem |
| --- | --- | --- | --- |
| **Project** | The project's instructions | A persistent agent for ongoing work | The cap on project instructions is not documented — verify in the first reply |
| **Custom GPT** | The *Instructions* field of the GPT editor (Configure tab) | An agent you may share | May not be available to create on your plan; the field's cap is not documented |
| **A single chat** | First message | A trial run | Nothing persists |

**Do not use the account-wide "Custom Instructions"** for this: they apply to *every* conversation you have, with every topic, and would make all of ChatGPT behave as this agent. They are also too small for the letter: 1,500 characters on Free and Go, 5,000 on Plus, Pro, Enterprise, Business and Education ([source](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)). Every letter is longer than that.

## Steps (project)

1. Create a **project**, name it after the agent's working name.
2. Paste the **whole letter** into the project instructions. If the field refuses it, use the fallback below.
3. Start a chat inside the project, say hello, answer the questions, read and confirm the SOUL it prints.
4. **Save the SOUL**: paste it into the project instructions below the letter, or upload it as a project file `SOUL.md` and add one line to the instructions: "At the start of every conversation, read SOUL.md and follow it."

## Fallback when the letter is longer than the field

1. Put a **short pointer** in Instructions: that this agent's full instructions are in the attached file `LETTER.md`, that it must read it fully before replying, and that its first reply must be the first-run questions.
2. Upload the full letter as a knowledge/project file named `LETTER.md`.
3. In your first chat, check that the agent really started with the questions. Files are retrieved, not always loaded in full: if it skips the protocol, paste the letter as the first message instead.

## Custom GPT specifics

- Choose manual configuration rather than letting the builder "generate" the instructions: generated text can summarise or change the rules.
- Leave **Actions** and **web browsing / code tools** off until the SOUL declares them.
- Sharing a GPT shares its instructions with whoever can open it. Keep it private.

## Limits and watch-outs

- The agent cannot save files for you; the SOUL is something you store.
- ChatGPT's own memory is a separate feature. Check what it remembers.

## Confirmed in the official documentation (consulted 2026-10-26)

| Fact | Source |
| --- | --- |
| **Custom Instructions** (account-wide): 1,500 characters on Free and Go; 5,000 on Plus, Pro, Enterprise, Business and Education. Go is a paid plan but stays at 1,500. This does **not** apply to GPTs or Projects. | [Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt), [release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |
| **Projects** are available on all subscription types, free and paid, globally. Plan and admin settings change files, sharing and other features; availability does not mean equal quotas. | [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-chatgpt-projects) |

## Not documented — check it yourself

- **The limit of a project's instructions** and **of a GPT's Instructions field** are not published in the official text retrieved. The figure of 8,000 characters that circulated for GPTs is historical: do not rely on it. The help article once used as a guide to writing GPT instructions now describes GPT availability.
- Direct access to the help pages was blocked (HTTP 403) during verification, so some facts rest on the officially indexed text; this does not prove the absence of a limit elsewhere in the documentation.

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
