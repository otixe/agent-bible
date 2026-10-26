# Other tools

*Last reviewed: 2026-10-26. Names change quickly; this page teaches what to look for.*

Every tool has some form of **text that applies to all conversations**. Use these examples as a guide, and confirm names in the product's own documentation.

| Family | Where the letter usually goes | The SOUL |
| --- | --- | --- |
| IDE assistants (Cursor, Windsurf, GitHub Copilot…) | A rules/instructions file in the workspace (e.g. `AGENTS.md`, or the tool's own rules folder) | The agent can write `SOUL.md` in the workspace if file tools are on. Use an empty workspace. |
| Custom-assistant builders (Copilot Studio, Le Chat agents, Perplexity Spaces…) | The assistant's *Instructions* / custom instructions | You save it into the instructions or a knowledge file |
| API or SDK (you write the program) | The **system prompt** of your request | Your code stores it; load it into the system prompt at each start |
| Anything with only a chat box | The **first message** of a new conversation | Paste it again at the start of each conversation |

## Checklist for any tool

1. Is there a field that applies to *every* conversation with this agent? Put the letter there.
2. If the field is too short, use a short pointer plus an attached copy of the letter, and verify in the first reply that the agent follows the protocol to the end.
3. Can the agent write files? If yes, give it a dedicated empty folder. If no, plan to save the SOUL yourself.
4. Which tools, connectors or actions are on? Turn them off until the SOUL declares a need.
5. Does the tool log activity? Where?
6. Who else can open the agent? Keep it private.

See the [eight questions](README.md#eight-questions-before-you-choose-or-configure-a-platform) for the rest.
