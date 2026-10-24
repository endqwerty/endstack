---
name: correct
description: Make a mistake agents keep repeating impossible, preferring architecture, types, lint and tests over docs.
disable-model-invocation: true
---

# Correct

The operator keeps correcting agents in this repo for the same mistakes. Change the repo so the next agent can't make them.

Assume every contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Design the repo so a change that looks right from one file is right for the whole repo.

## First, is it a mistake?

A correction names a defect against something still wanted, a preference, or an experiment. Only a defect gets a guard. Record a preference in the user's words with how firm it was ("maybe", "for now"); it stays open to change. Give an experiment the condition that ends it. Never freeze a first measurement or an agent's own choice into a limit, and never credit the user with a choice an agent made. Before a project's 1.0, any rule may go once it stops serving.

A guard taxes every later change. Add one only when the mistake recurs and costs more than the guard; a correction about wording or presentation does not justify a parser or a blocking check.

## One rule

When you are about to add a rule to an agent instruction file, or were just corrected, handle that one mistake instead of sweeping the repository: take it down the levels below, fix it at the highest level that works in the same change, and prove the guard fails on the mistake. A rule the user asked for is still written, as one row in the rule table naming what enforces it and quoting their words, so a later word can replace it; otherwise write a rule only if it still needs judgment.

## Find the mistake classes

First, read recent commits, reverts, review comments, agent instruction files, and comments that explain workarounds. Group the mistakes into classes. A class counts once it has happened twice.

## Fix each class at the highest level that works

1. **Eliminate it with architecture.** Give each piece of state one owner and each task one supported way. Hide internals so the wrong import fails. Replace hand-synced lists with one source of truth. Delete old ways and dead code an agent would copy.
2. **Enforce it with types so the bad state can't be written.** If bad code still compiles, add a lint or CI check whose error names the file, type, or function to use instead. If the pattern is already common, fail only when a change adds more.
3. **Test the behavior.** Fix or delete any test that still passes when the behavior it checks breaks, or that fails when only the internals change.
4. **Write docs or agent rules last, only for judgment calls.** Nothing fails when an agent skips them.

## Fix and prove

Then fix the most frequent classes now, one commit each. Prove each new check fails on a real past mistake. Run the same command locally and in CI. Exceptions go on the offending line with a reason, an expiry date, and a human's approval.

## Keep the rule table

Last, keep a table in the agent instruction file that pairs each rule with what enforces it. When the operator corrects you, follow One rule above. If the rule was already there and nothing enforces it, that's a repeat, so fix it at the highest level in the same change. Drop a rule once its mistake can't happen.

**Reply:** each class with its evidence, the level you picked, and why a higher level didn't work.
