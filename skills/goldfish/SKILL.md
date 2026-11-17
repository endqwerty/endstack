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

- A design doc, before implementation starts and after any round of edits
  that changes its plan.
- An agent instruction file (`AGENTS.md`, a README agents start from, a
  long reference such as a workstation or runbook file, a skill) after a
  substantial edit, and in periodic passes over a project.

## Roles

- **Author**: you. You pick the tasks, judge the findings and edit the
  document. You never answer a goldfish in chat; an answer goes into the
  document or it does not exist.
- **Goldfish**: a separate read-only worker, from a different model family
  if available. Each stage and round gets new ones; a goldfish that has seen
  an earlier draft is no longer a goldfish. Briefs come from
  [references/goldfish-prompt.md](references/goldfish-prompt.md).
- **Merging worker**: for a stage with two or more reviewers, a separate
  worker starts them, merges and ranks their findings into a report file
  outside the tree, and returns only statuses and counts
  ([references/reviewers.md](references/reviewers.md)). Without nested
  workers, start the reviewers yourself and merge the same way.

If you cannot start separate workers (no harness support, or you are a
delegated worker told not to), hand the review to whoever can, such as the
agent that delegated you, or report the document untested: reading your own
document fresh is not possible.

## Agent instruction files

One goldfish runs the brief's three passes in order: comprehension, critic,
readiness. Readiness gets two to four realistic tasks from recent or planned
work, stated the way the user would state them, with no hints. What it read
and never needed, and where length or order lost it, are cut or move
candidates. Repeat with a new goldfish under the loop rules below.

## Design docs: five stages

Roles are in [references/reviewers.md](references/reviewers.md), standards in
[references/standards.md](references/standards.md). The feature part is
everything before *Implementation*; the detail part is *Implementation* and
*Tasks*. Run the stages in order, fixing between them.

1. **Zoom out**: zoom-out and design-pattern reviewers, whole doc.
2. **Comprehension**: one comprehension reviewer, started directly so you
   read its paraphrase. Compare it with what you know is true; each
   misunderstanding is a gap in the document.
3. **Critic loop**: design critic, structure and style, feature part.
4. **Zoom out again**: zoom-out reviewer, whole doc, not reopening what
   stage 1 settled.
5. **Readiness loop**: implementation readiness (with two to four realistic
   tasks), codebase details and style, detail part.

A doc with no detail part yet stops after stage 4.

## Loops

Stages 3 and 5 repeat with new reviewers until they converge.

- A round is **clean** when no blocker or should is open that is not
  settled; nits never block. A reviewer that did not run makes the round
  not clean. Decide this before applying the round's fixes.
- **Converged** is two clean rounds in a row: fresh readers sample
  differently, so one clean round proves little.
- A contested or declined finding is **settled** and stays closed when
  raised again. A fixed finding raised again is reopened: the fix failed.
- Stop at five rounds, or on **churn**: a new finding that reverting an
  earlier fix would clear. List the open findings by rank. With the user
  present, ask one question: accept, continue past the cap, or return the
  document to drafting. Without the user, report both sides: the document
  may be the wrong shape.

## Judge and fix

Each finding names the file and line, quotes it, gives evidence and a fix,
and is ranked **blocker** (the reader would do the task wrong), **should**
(it would have to ask or guess) or **nit** (wording, taste, nothing shown
reaches it). Check it against the real files, then give it one category:

- **Fix**: valid; edit the document.
- **Contest**: wrong, shown by evidence the goldfish could read: a file and
  symbol, or a decision the document records. "This was intentional" is not
  evidence. You wrote the document; wanting to contest is not proof.
- **Escalate**: wrong only by knowledge no file holds, such as a choice only
  the user can make. Ask the user, one question at a time; without the user,
  record it under the doc's open questions with the answer you assume. Either
  way the answer goes into the document.
- **Decline**: a nit not worth fixing.

Never contest a comprehension gap: if a fresh reader could not follow it,
context is missing. Never change a rank; contest it instead. Prefer cutting
and reordering to adding: a longer file is harder for the next goldfish. A
rule that keeps being missed belongs in a check, not more prose (the
[correct](../correct/SKILL.md) skill).

## Report

The document and revision, the stages and rounds run, each reviewer's
status and model family, the tasks given, each finding with its rank and
category, and the report files.
