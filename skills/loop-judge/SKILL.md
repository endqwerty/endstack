---
name: loop-judge
description: From the third round of a loop on one goal (retries, fix and rerun, hill climbs, review rounds), a light fresh judge reads the goal and attempt log and says continue, pivot or stop.
disable-model-invocation: true
---

# Loop judge

An agent deep in a loop is the worst judge of whether to keep going. It remembers why each attempt should have worked, reads its near misses as progress, and has spent too much to stop. Once a loop reaches its third round, hand that call to a fresh judge that sees only the goal and the record.

The judge is light on purpose: your provider's light tier for gathering work, below the one doing the loop, in a separate context, one short call. The same provider is fine. It judges progress, never the code; correctness stays with the checks and [verify](../verify/SKILL.md). Without a separate context, answer the verdict yourself from the log alone and say the judge was not independent.

## When to ask

A loop is any repeated attempt at one goal: a failing test fixed and rerun, a flaky check, a hill climb on a number, review rounds, a red pull request, a hunt for a root cause. The first two rounds usually pay for themselves; let them run. Ask the judge from the third round on: after the third attempt at the same goal ends short of it, and after each round from then on. Also ask, at any round, before the loop spends something new: a wider scope, a new dependency, a pricier model, a one-way door.

Skip it for a loop still in its first two rounds, one retry of a known flake, or a loop whose stop rule is already a script, such as a watcher that waits for a merge.

## The brief

One short message:

- The goal as a predicate a check can decide, and the budget: rounds, time or spend allowed, and what is left.
- The attempt log, one line per round: what was tried, the hypothesis behind it, and the result as deciding lines (the number, the failing assertion, the error), not a story. A [show-me-your-work](../show-me-your-work/SKILL.md) log is this log.
- What the next round would try.

Leave out why you think it should continue, your confidence and the answer you want. A judge that hears the case for continuing agrees with it.

## The verdict

The judge answers one word and one reason that cites log lines:

- **Continue.** The last rounds moved the predicate by a measured amount, and the next step follows from that evidence.
- **Pivot.** No measured progress in the last two rounds; the same failure under different fixes; several rounds circling one hypothesis; or a result that contradicts the approach. Name what the log rules out and one different direction: another hypothesis, a smaller reproduction, a different layer, reading the source instead of guessing, or getting the one missing fact.
- **Stop.** The predicate is met; the budget is spent; the gap left costs more than it is worth; the next step needs something only the user can give or authority the loop lacks; or it is a one-way door the loop was not cleared to open. Say which.

When the log cannot decide it, the answer is Pivot to measuring: name the number the log is missing.

## Acting on it

- Follow the verdict. Overrule it only with evidence the judge did not have; log the override and that evidence. Asking another judge the same log is not new evidence.
- Two Pivots in a row with no progress between them is a Stop.
- Report a Stop as what it is, with the log and the gap left, never as done.
- The verdict grants nothing. Continue does not clear a gate, a merge or a one-way door; Stop does not skip a required check on work already delivered.
- Log each verdict and its reason as one row.
