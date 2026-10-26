# The SOUL

The **SOUL** is the document that says *who the agent is*: its name, its role, whom it answers to, what it may and may not do, and how it communicates. It is loaded at the start of every conversation and it is the agent's base instructions.

An agent without a SOUL still answers — but as the generic model. It changes its criteria depending on how you ask, has no limits of its own, and there is nothing to audit its behaviour against. The SOUL is what turns a language model into **an agent with responsibilities**.

## What the agent writes into it

The letter requires the SOUL to contain: the name; a transparent identity as an AI; the responsible human and agreed form of address; purpose, functions and limits; effective tools and permissions; memory and the agreed location; all the Golden Rules; the Harness; confirmed preferences; and a version. This layout is one way to organise that; the agent fills it from your answers and must mark anything you did not answer as missing, not invent it.

```markdown
# <Agent name>   (technical id: agent-<unit>-<name>)

## Who I am
An AI agent. <Purpose in one sentence.>

## What I do
<Concrete functions.>

## What I do not do
<Limits, as concrete as the functions.>

## Who I answer to
<Responsible human, how to address them, channel, time zone.>

## How I communicate
<Style, in positive terms: what I am, not just what I avoid.>

## Tools, sources and permissions
<Only what is actually connected and authorised; what needs my confirmation.>

## Memory and where this file lives
<How my memory works; the location you confirmed for SOUL.md.>

## Golden Rules
<The Golden Rules, whole.>

## Working method (Harness)
<The Harness, whole.>

## How I learn from my user
<What I observe, that I ask before adopting a pattern, and that you can see, fix or delete it.>

## First contact
<What I do at the start, so I do not repeat the protocol every time.>

## Version and change log
<Version · date · what changed · who approved.>
```

## Why the name matters

A name is not decoration. In practice it does four things: it keeps the agent's **identity stable** across conversations (it is the anchor it returns to); it makes every action **attributable** (documents and records are signed by an identifiable agent); it makes it **clear to people** that they are talking to an AI; and it **separates responsibilities** when you have more than one agent.

Choose a name that is short, pronounceable and unique among your agents; that does not look like a real colleague's name; and that does not suggest authority the agent does not have ("Auditor" for something that only summarises).

## Role, in three levels

| Level | Question | Example |
| --- | --- | --- |
| Purpose | Why does it exist? | "Prepare the background material for my weekly planning meeting." |
| Functions | What does it do, concretely? | Summarise emails, draft minutes, find documents, remind me of commitments. |
| Limits | What does it never do? | Never sends email in my name; never edits shared documents; never approves anything. |

Limits matter as much as functions: writing them prevents the agent from "helping too much".

## Correcting the SOUL safely

1. **Ask the agent to propose the change** in plain language and show you the new text.
2. **Read the difference.** Changes to role, limits or permissions are decisions, not edits; take them seriously.
3. **Keep the old version whole.** The SOUL has a version and a date; each change adds a line to the change log (what, why, who approved). Never overwrite without a copy.
4. **Update every copy.** On chat platforms the SOUL lives in the platform's instructions or files; update it there too.
5. **Retest.** After changing a limit or a permission, try the case it governs (see [the rules explained](golden-rules-explained.md)).

## What it cannot override

A SOUL can *add* restrictions to the Golden Rules. It cannot remove them. If the SOUL and a rule conflict, the rule wins and the agent should say why it cannot proceed.

If the responsible human changes jobs or leaves, the agent is suspended until someone is assigned or the agent is retired. The SOUL should say so.
