# Amazon Quick

*Last reviewed: 2026-10-26. Field names below follow the English console; other languages and versions label them differently.*

**Where the letter goes:** the chat agent's **Agent profile → Instructions**.

Pasting a *manual* into Quick as the description does not work: Quick generates a generic agent from the text and does not apply the method. The letter works because it is the agent's own instructions.

## Fields and what goes in each

| Field | What to put |
| --- | --- |
| Title | The agent's working name |
| Description | One line: its purpose (you will refine it after first run) |
| Agent profile → **Instructions** | **The letter, whole** |
| Agent profile → Reference documents | Optional: Golden Rules and Harness files, the SOUL after first run (several file types accepted; the *extracted document text* is capped — see below) |
| Knowledge sources | **None** at the start |
| Actions | **None** at the start |
| Personalization | A welcome message and suggested questions (see below) |
| Preview pane | Where you run the first test before publishing; refresh after every change |
| Share | Only the responsible human |

## Steps

1. In **Chat agents**, create a new agent. On the first screen choose **Skip** (configure manually). The "Generate" option writes the instructions itself and can summarise or change the rules.
2. Fill Title and Description. Paste the **letter** into Instructions.
3. Leave knowledge sources and actions empty.
4. Set a welcome message such as: "Hi. I'm a new agent and I don't have a name or a role yet. I'll ask you a few questions, one at a time."
5. In the **preview**, say hello. Expect questions, not work. Answer; read the SOUL it prints; confirm.
6. **Save the SOUL:** attach it as a reference document and add to the instructions: "At the start of every conversation, read the SOUL document and follow it." If the instruction field has room, paste the SOUL below the letter instead.
7. Publish and share only with the responsible human. Add knowledge sources and actions later, one at a time, each tested.

## Limits and watch-outs

- **Instruction length.** The official guide does **not** publish a maximum for the instructions, so you cannot count on the letter fitting: paste it whole and check the first reply. If a field refuses it, use the file fallback; do not trim the letter. If you must split content, keep this priority: Golden Rules, identity and limits, Harness, style; the rest goes to a reference document.
- **Memory.** If the platform has no persistent memory, the SOUL and the agent's preferences must live in a reference document you update.
- **Action confirmation.** Check whether Quick asks you before running an action. If it does not, the letter's rules are the only barrier: test them in the preview.
- The platform's "enterprise guardrails" notice refers to the platform's general controls. They do **not** replace the Golden Rules or the limits you give the role.

## Confirmed in the official documentation (consulted 2026-10-26)

- The **100,000-character figure is the text extracted from uploaded reference documents** (up to 10 files), **not a limit on the instructions** ([Custom chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-agents.html)). Do not read it as an instruction cap, and do not apply it to spaces.
- **Not documented** in the guides consulted: a maximum length for the agent's instruction fields (Agent identity, Persona, Tone, Response format, Length), and a character limit for a space's instructions ([Creating a space](https://docs.aws.amazon.com/quicksuite/latest/userguide/creating-spaces.html), [Managing a space](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-spaces.html)). "Not documented" means no published figure, **not unlimited**.

Still to check in your own console: memory features, activity logging, and data retention and use by the provider.

Full source list and caveats: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
