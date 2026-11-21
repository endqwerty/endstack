---
name: test-design
description: Decide what test to write, at which layer, and whether it stays. Also fixes a bug test-first when it has a cheap local test or a regression test is asked for.
disable-model-invocation: true
---

# Test design

Every kept test is a standing cost: each later change runs it, reads it and repairs it when it breaks. Keep a test only when its failure tells someone what to fix, at the cheapest layer that can say it. Proving a change and keeping a test are separate decisions.

Read the project's testing guide first, if it has one.

## Before writing a test

1. **Name the failure.** State the reachable fault: which input or later change causes it, what goes wrong for a user, and who would act on the failure. If you cannot, write no test.
2. **Find the existing holder.** Search for a test that already asserts the fact, at this layer or a cheaper one. Search by what it observes (the reply, the stored row, the text on screen), not by name. Extend that test, or name it and write nothing.
3. **Choose the cheapest layer that reaches the fault**, and the cheapest schedule: every change, daily, or only when its code changes. A browser only for what needs its engine (layout, real focus and keys, navigation); one browser journey covers a flow, and its conditions go a layer down.

## Writing it

- Follow the [test-behavior-not-implementation](../principles/references/test-behavior-not-implementation.md) principle: derive expected values from the requirement, not from a run of the code.
- No sleeps, wall-clock deadlines, fixed ports, shared directories or order dependence. Wait on the operation or a signal it resolves; to move time, use the framework's fake clock.

## Bug fix: fail first

For a bug with a cheap local test, or when a failing or regression test is asked for.

1. **Find the cause, then every consumer with the same fault.** Read the [principles index](../principles/SKILL.md) first, then trace the symptom to its cause per the [fix-root-causes](../principles/references/fix-root-causes.md) principle. Then check every consumer, not only the one reported: other clients (web, mobile, command line, integrations) and sibling functions that do the same job. Search by what the faulty code does (the data it reads, writes or combines), not only by its name or call spelling. List each place you find.
2. **Name what the fix makes redundant**: a guard or workaround downstream of the cause. Delete it in the fix, but not an interface callers outside the repository may use.
3. **Write the failing test first**, one for each independently faulty place; consumers that share one faulty implementation share one regression test on it. Run it and see it fail for the intended reason. Where the history allows, commit it before the fix.
4. **Fix the cause in every consumer you listed**, not a guard downstream, or say why one is exempt. Rerun the test; it passes. Then decide whether it stays, below.

If a failing test would need broad harness setup, brittle mocks, production-only state or large fixture churn, use the closest executable check instead (a script, a reproduction command, a focused integration check) and say why. Prefer no new test over a bad one. Never change a test to match a wrong implementation, or weaken an assertion unless the intended behaviour changed.

## Prove, then decide

1. **Prove it.** A test of new or fixed behaviour must fail without the change for the intended reason, not because a symbol is missing, and pass with it. A test that pins behaviour a refactor must keep passes before and after.
2. **Keep it only when all hold:** a plausible later change to code that stays could break the behaviour unnoticed; it catches a behaviour break and survives a refactor that keeps behaviour; it is fast and deterministic.
3. **Drop it** when the fault cannot recur there: a one-time script or data repair retired after its run, a path the change removed, a test that only restates a value. A migration that new or restored databases still run is code that stays, so its test can stay.
4. **A dropped proof** goes where the project's guide puts proofs outside the suite, with the deciding lines quoted in the pull request. Otherwise remove it in its own last commit, per the [sequence-verifiable-units](../principles/references/sequence-verifiable-units.md) principle, so the history shows it fail and pass and a revert restores it.

## Changing the suite

- **A flaky test is a defect.** Fix its cause: a shared resource, an unordered read, or a deadline below the work. Retries and longer timeouts are not fixes. Make it deterministic and document the signal being locked down.
- **Deleting is normal.** Delete a test whose fact a cheaper kept test holds, whose state a refactor made unreachable, or whose feature is gone, and name the holder or the reason.
- Internal tooling gets a proof, not a kept test, unless a mistake there is costly to undo.

## Report

In the pull request or reply:

- each fix's failing-before and passing-after lines, or why no failing test was possible and the check used instead;
- for a bug fix, the consumers checked for the same fault, which changed, and why any was left, and each principle that changed a choice;
- which new tests stay and which were dropped or deleted, with the holder or reason and the commit that removed them;
- the time added to the every-change suite, when measurable.
