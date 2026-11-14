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
  document. You never answer the goldfish's questions in chat; an answer
  goes into the document or it does not exist.
- **Goldfish**: a separate read-only worker, from a different model family
  if available. Each pass and each round gets a new one; a goldfish that has
  seen an earlier draft is no longer a goldfish. If you cannot start
  separate workers (no harness support, or you are a delegated worker told
  not to), hand the pass to whoever can, such as the agent that delegated
  you, or report the document untested: reading your own document fresh is
  not possible.

## Passes

Build each brief from [references/goldfish-prompt.md](references/goldfish-prompt.md).
For a design doc, run the three passes as three goldfish at once. For a
routine pass over agent instruction files, one goldfish may run all three in
order.

1. **Comprehension.** Explain what the document is for and how the system
   it describes works. Compare the answer with what you know is true; each
   misunderstanding is a gap in the document, not in the reader.
2. **Critic.** Find what is missing, wrong, stale, contradictory or
   ambiguous. The goldfish checks claims against the referenced files and,
   read-only, against the real system where it can.
3. **Readiness.** Give two to four realistic tasks, taken from recent or
   planned work, stated the way the user would state them, with no hints.
   The goldfish says how it would do each one using only what it read, every
   question it would have had to ask, and where it guessed. For an agent
   instruction file it also lists what it read and never needed, and where
   length or order made it lose the thread: those are cut or move
   candidates.

## Judge and fix

- Each finding names the file and line, quotes it, gives the evidence and a
  proposed fix. Rank it: **blocker** (the reader would do the task wrong),
  **should** (it would have to ask or guess), **nit** (wording, taste,
  nothing shown reaches it).
- Check each finding against the real files before acting; a goldfish can
  be wrong too. Dismiss with a one-line reason.
- Fix blockers and shoulds in the document. Prefer cutting and reordering
  to adding: a longer file is harder for the next goldfish. A rule that
  keeps being missed belongs in a check, not more prose (the
  [correct](../correct/SKILL.md) skill).
- Run a new round with new goldfish until only nits remain. After three
  rounds with blockers still open, stop and report both sides: the document
  may be the wrong shape.

## Report

The document and revision tested, the tasks given, each finding with its
rank and what you did, the rounds run and the goldfish's model family.
