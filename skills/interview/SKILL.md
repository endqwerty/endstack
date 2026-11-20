---
name: interview
description: Before designing a feature, question the user to draw out their intent and judgment, then propose the first design yourself and argue it to a design doc.
disable-model-invocation: true
---

# Interview

## When

A new feature or product change whose result depends on the user's intent,
taste or priorities, unless the user opts out.

## 1. Ground

Read what the feature touches, then tell the user in a short paragraph how
you understand the relevant part of the system, so they can correct it
before it shapes anything.

## 2. Question, no code

Write no code and no design yet. Ask one question at a time, the one that
would change the design most first. Each question says why it matters and
the answer you would assume without one.

- Name edges the user has not covered: failure, scale, who else uses it,
  what it replaces, what it must never do.
- Disagree when the evidence says so, and show the evidence.

Stop when the user says so or when new answers stop changing the design.

## 3. How done is judged

Ask how the user will judge the result: what they will look at, try or
measure. These become the doc's behaviour scenarios and their checks.

## 4. Brief and concept review

Write the brief as a file next to where the design doc will go
(`<short-name>.brief.md` beside `docs/design/<short-name>.md` by default), so a
new session can draft from it, with these sections: *Overview* (the feature,
who it is for and why), *Goals* and *Non-goals*, *Analysis* (the concept
review below), *Alternatives weighed* (each option turned down and why,
credited to whoever turned it down), and *Key decisions*.

For the analysis, run the concept reviewers in
[goldfish](../goldfish/SKILL.md)'s
[reviewer roles](../goldfish/references/reviewers.md) on the overview, goals
and decisions, as fresh read-only workers; if you cannot start workers,
hand this step on as goldfish says. Show the user the two or three
strongest objections and settle each, one question at a time, updating the
brief.

## 5. You propose the first design

Propose the design yourself, in prose and a block diagram where it helps.
Proposing first shows whether you understood; reacting to the user's design
hides your blind spots. Argue it through with the user until it settles,
adding each option turned down to the brief.

## 6. Write the design doc

Write the doc into the project as [build](../build/SKILL.md)'s
[design reference](../build/references/design.md) describes, from the brief
and this conversation. Then reconcile it with the brief: list each question
the brief settled that the doc settles differently, quoting both, and each
architecture, interface or dependency choice the brief never raised. The
user decides each contradiction, one at a time; do not just make the doc
match the brief, since drafting read code the brief did not. Delete the
brief in the same change.

## Without the user

If the user is not there to answer (unattended or delegated work), do not
block. Answer each question and contradiction yourself with the default you
would assume, write the questions and your answers under the doc's open
questions, and name them in the first lines of the pull request so the user
can overturn them.
