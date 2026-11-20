---
name: goldfish
description: Test whether a design doc or agent instruction file stands alone, by giving it to fresh readers with no other context.
disable-model-invocation: true
---

# Goldfish

The author of a document holds context the document does not. A goldfish is a
fresh reader with no memory: it gets only the document's paths and the files
the document references, never the conversation, your conclusions or the
answers. If it cannot understand and act on the document, the document is
missing something, however clear it looks to you.

## When

- A design doc, before implementation starts and after edits that change
  its plan.
- An agent instruction file (`AGENTS.md`, a README agents start from, a long
  reference or runbook, a skill) after a substantial edit.

## Roles

- **Author**: you. You pick the tasks, judge the findings and edit the
  document. You never answer a goldfish in chat; an answer goes into the
  document or it does not exist.
- **Goldfish**: a separate read-only worker, from a different model family
  if available, new for every stage and round. Briefs come from
  [references/goldfish-prompt.md](references/goldfish-prompt.md).
- **Merging worker**: for a stage with two or more reviewers, as
  [references/reviewers.md](references/reviewers.md) describes.

If you cannot start separate workers (no harness support, or you are a
delegated worker told not to), hand the review to whoever can, such as the
agent that delegated you, or report the document untested: reading your own
document fresh is not possible.

## Agent instruction files

One goldfish runs the brief's three passes in order: comprehension, critic,
readiness. Readiness gets two to four realistic tasks from recent or planned
work, stated the way the user would state them. What it read and never
needed, and where length or order lost it, are cut or move candidates.
Repeat with a new goldfish under the loop rules below.

## Design docs: four stages

Roles are in [references/reviewers.md](references/reviewers.md). The feature
part is everything before *Implementation*; the detail part is
*Implementation* and *Tasks*. Run the stages in order, fixing between them.

1. **Zoom out**: zoom-out and design-pattern reviewers, whole doc.
2. **Comprehension**: one comprehension reviewer, whole doc, started
   directly so you read its paraphrase. Compare it with what you know is
   true; each misunderstanding is a gap in the document.
3. **Critic loop**: design critic and style, feature part.
4. **Readiness loop**: implementation readiness (with two to four realistic
   tasks), codebase details and style, detail part.

A doc with no detail part yet stops after stage 3. For a stage with one
reviewer, you write its report file.

## Loops

Stages 3 and 4 repeat with new reviewers until they converge.

- A round is **clean** when no blocker or should is open that is not
  settled; nits never block. A reviewer that did not run makes the round
  not clean. Decide this before applying the round's fixes.
- **Converged** is two clean rounds in a row: fresh readers sample
  differently, so one clean round proves little.
- A contested or declined finding is **settled** and stays closed when
  raised again. A fixed finding raised again is reopened: the fix failed.
- Stop after five rounds without converging and report the open findings by
  rank: the document may be the wrong shape.

## Judge and fix

Findings come ranked as the brief defines. Check each against the real
files, then give it one category:

- **Fix**: valid; edit the document.
- **Contest**: wrong, shown by evidence the goldfish could read: a file and
  symbol, or a decision the document records. "This was intentional" is not
  evidence.
- **Escalate**: wrong only by knowledge no file holds, such as a choice only
  the user can make. Ask the user, one question at a time; without the user,
  record it as [interview](../interview/SKILL.md)'s "Without the user" says.
- **Decline**: a nit not worth fixing.

Never contest a comprehension gap: if a fresh reader could not follow it,
context is missing.

## Report

The stages and rounds run, each reviewer's status, and each finding with
its rank and category.
