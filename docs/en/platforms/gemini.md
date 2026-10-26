# Gemini (Gems and Gemini CLI)

*Last reviewed: 2026-10-26.*

Two different products, two different ways.

## Gemini Gems (chat app)

**Where the letter goes:** the Gem's **Instructions** field.

1. Create a **new Gem**. Name it with the agent's working name.
2. Paste the **whole letter** into Instructions. If it does not fit, use the pointer-plus-file fallback described in the [ChatGPT page](chatgpt.md#fallback-when-the-letter-is-longer-than-the-field) (attach the letter as a Gem knowledge file).
3. Open the Gem, say hello, answer the questions, read and confirm the SOUL.
4. **Save the SOUL by hand**: a Gem cannot write files. Add the SOUL text to the Gem's Instructions below the letter, or attach it as a knowledge file and say in the instructions to read it first.

Watch-outs: Gems have no tools of your own unless you connect them; keep connected apps off until the SOUL declares a need. Check the sharing setting: keep the Gem private.

## Gemini CLI

**Where the letter goes:** a `GEMINI.md` context file in the folder where you run the CLI.

1. **Create an empty folder**, save the letter as `GEMINI.md`, and run the CLI there with `--approval-mode default` or `plan` (not `auto_edit` or `yolo`).
2. After you confirm the SOUL the agent writes `SOUL.md`; add one line at the end of `GEMINI.md`: "At the start of every session, read SOUL.md in this folder and follow it."
3. Like other folder-based agents, it loads context files from parent folders too — keep the folder isolated.

## Confirmed in the official documentation (consulted 2026-10-26)

| Fact | Source |
| --- | --- |
| **Gemini CLI approval modes** (flag `--approval-mode`): `default` (asks for most writes), `auto_edit` (auto-approves some writes; called `autoEdit` in policy files), `yolo` (auto-approves tools — use with extreme caution), `plan` (read-only, defined by policy). The policy engine (allow / deny / ask_user, priorities, admin rules) still matters. **A mode is not OS isolation and not authorisation from your organisation.** | [Policy engine](https://geminicli.com/docs/reference/policy-engine/), [CLI reference](https://geminicli.com/docs/cli/cli-reference/) |

## Not documented — check it yourself

- **A maximum length for a Gem's instructions** is not published in the official Gems pages consulted ([Gems guides](https://support.google.com/gemini/answer/15236321?hl=en), [Gem instructions](https://support.google.com/gemini/answer/15235603?hl=en)): they give a structure, not a number. Do not borrow limits from the Gemini API (`systemInstruction`) or from model context sizes.
- Whether Gems keep memory between conversations, and the CLI's context-file loading order: check the product documentation for your version.

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
