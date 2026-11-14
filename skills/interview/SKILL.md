---
name: interview
description: Before designing a feature, question the user to draw out their intent and judgment, then propose the first design yourself and argue it to a design doc.
disable-model-invocation: true
---

# Interview

A feature's design rests on judgment only the user holds: what it is for,
what good looks like, what to give up. Asking for it after the code exists
is too late. This skill draws it out first, then writes it down where a
fresh agent can find it.

## When

A new feature or a product change whose result depends on the user's
intent, taste or priorities. Not for a bug with a clear fix, a mechanical
change, a chore the request fully specifies, or when the user opts out. A
project's own rules may name where it is required.

## 1. Ground

Read the docs and code the feature touches (the [how](../how/SKILL.md)
skill for an unfamiliar subsystem). Tell the user in a short paragraph how
you understand the relevant part of the system, so they can correct it
before it shapes anything.

## 2. Question, no code

Write no code and no design yet. Ask questions in small batches, three to
five, the ones that would change the design most first. Each question says
why it matters and the answer you would assume without one.

- Challenge assumptions. Name edges the user has not covered: failure,
  scale, who else uses it, what it replaces, what it must never do.
- Disagree when the evidence says so, and show the evidence. Agreeing is not
  help. If you notice yourself praising, ask a harder question instead.
- When an answer looks weak, ask why. When you are unsure of a fact, read
  the file rather than guess.

Stop when the user says so or when new answers stop changing the design.

## 3. How done is judged

Ask how the user will judge the result: what they will look at, try or
measure. These become the change's checks.

## 4. You propose the first design

Propose the design yourself, in prose and a block diagram where it helps,
pseudocode only where prose fails. Proposing first shows whether you
understood; reacting to the user's design hides your blind spots. Argue it
through with the user until it settles. Each option turned down, and why,
is kept.

## 5. Write the design doc

Write the doc into the project as [build](../build/SKILL.md)'s
[design reference](../build/references/design.md) describes, one section at
a time, from this conversation. Then test it with the
[goldfish](../goldfish/SKILL.md) skill before implementation starts; an
answer the user gave only in chat goes into the doc.

## Without the user

If the user is not there to answer (unattended or delegated work), do not
block. Answer each question yourself with the default you would assume,
write the questions and your answers under the doc's open questions, and
name them in the first lines of the pull request so the user can overturn
them.
