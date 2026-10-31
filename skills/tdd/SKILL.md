---
name: tdd
description: Test-first fixes, when a test is asked for or the bug has a cheap local test.
disable-model-invocation: true
---

# TDD Bug Fix

When fixing a bug with a clear, cheap test path, make the broken behavior executable before changing production code. The goal is a focused regression test that fails before the fix and passes after it.

Do not force a test when it would be impractical. If the available test would require broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state, vague reproduction steps, or large unrelated fixture churn, skip adding a new test and use the closest useful verification instead.

## Workflow

When a step names a principle, read that reference before doing the step.

1. **Understand the bug.** Identify the intended behavior, current behavior, affected path, and smallest observable reproduction. Trace the symptom to its cause per the [fix-root-causes](../principles/references/fix-root-causes.md) principle. Then, before writing the test:
   - **Find every consumer with the same fault**, not only the one reported: other clients (web, mobile, command line, integrations) and sibling functions that do the same job. Search by what the faulty code does (the data it reads, writes or combines), not only by its name or call spelling. List each place you find.
   - **Name the shape** if the fix changes a type or a state, and keep impossible combinations out of it, per the [type-system-discipline](../principles/references/type-system-discipline.md) principle.
   - **Name what the fix makes redundant**: a guard or workaround downstream of the cause. Delete it in the fix, but not an interface callers outside the repository may use.
   - A fix that crosses a function boundary or adds a module: read build's [design step](../build/references/design.md) and do it. Under build, its design step applies to every fix anyway.
2. **Choose the narrowest executable check.** Prefer the closest unit, component, integration, or regression test already used for that codepath. If no practical test path is obvious, do not create one from scratch just to satisfy the workflow.
3. **Write the failing test first.** Add the smallest focused test that would have caught the bug, for each independently faulty place found in step 1. Consumers that share one faulty implementation share one regression check on it. The test should encode intended behavior, not mirror the current implementation, per the [test-behavior-not-implementation](../principles/references/test-behavior-not-implementation.md) principle.
4. **Run the new test before fixing.** Confirm it fails for the intended reason. If it passes or fails for an unrelated reason, correct the test or reproduction before editing the implementation. Where the history allows, commit the failing test before the fix. That is the canonical order of the [sequence-verifiable-units](../principles/references/sequence-verifiable-units.md) principle.
5. **Fix the bug.** Make the smallest production change that satisfies the intended behavior while preserving nearby contracts. Fix the cause, not a guard downstream, in every consumer listed in step 1, or say why one is exempt.
6. **Rerun the regression test.** Confirm the test now passes.
7. **Decide whether the test stays.** It has proved the fix; joining the suite is a separate call, because every kept test is read and maintained. Keep it when a plausible later change to code that stays could bring the bug back unnoticed, it passes the two edits of the test-behavior-not-implementation principle, it is fast and deterministic, and no existing test covers the case (extend an existing case rather than add a file). Drop it when the bug cannot recur there: a one-time script, migration or data repair, a path the fix removed, a test that only restates a value. Remove a dropped test in its own last commit, so the history still shows it fail and pass, and reverting that commit restores it.

## If a Failing Test Is Impractical

Use the closest executable regression check instead: a targeted script, manual reproduction command, browser automation, snapshot comparison, log assertion, or focused integration check.

Prefer no new test over a bad test. A bad test is one that mostly tests mocks, encodes current implementation details, depends on timing or unrelated global state, or needs expensive infrastructure for a small fix.

## Guardrails

- Do not change tests merely to match a wrong implementation.
- Do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.
- Keep the regression test focused on the bug. Avoid broad fixture churn or unrelated coverage expansion.
- If the bug is flaky, make the test deterministic where possible and document the signal being locked down.
- If the bug exposes a broader class of failures, first land the focused regression path, then consider additional sibling coverage.

## Final Response

Report the evidence, not just the outcome:

- Name the failing-before test or executable check and the failure it produced.
- Name the passing-after test run and any nearby validation performed.
- Say which new tests stay and which were dropped, why, and the commit that dropped them.
- If failing-before evidence could not be demonstrated, state why and describe the closest regression check used instead.
- List the consumers checked for the same fault, which ones changed, and why any was left.
- Name each principle that changed a choice, and the choice.
