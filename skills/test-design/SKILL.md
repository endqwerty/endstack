---
name: test-design
description: Decide what test to write, at which layer, and whether it stays, when adding, keeping, moving or deleting a test. Fewer, cheaper tests whose failures say what to fix.
disable-model-invocation: true
---

# Test design

Every kept test is a standing cost: each later change runs it, reads it and repairs it when it breaks. Keep a test only when its failure tells someone what to fix, at the cheapest layer that can say it. Proving a change and keeping a test are separate decisions.

Read the project's testing guide, if it has one, before the first test; it wins where it is more specific (its layers, helpers, budgets, where proofs go). Without one, use the layers below.

## Before writing a test

1. **Name the failure.** State the reachable fault: which input or later change causes it, and what goes wrong for a user. If nothing reaches that state yet, write no test. If you cannot say who acts on the failure and what they would do, write no test.
2. **Find the existing holder.** Search for a test that already asserts the fact, at this layer or a cheaper one. Search by what it observes (the reply, the stored row, the text on screen), not by name. Extend that test, or name it and write nothing.
3. **Make the code cheap to check.** If a rule needs a database, server or browser only because it is tangled with them, move the decision into a pure function and test that, when the change's scope allows. Otherwise test at the layer the code allows and note the extraction as follow-up work.
4. **Choose the cheapest layer that reaches the fault.**
   - Pure logic: a unit test beside the code.
   - Storage, transactions, permissions: an operation test against the real store.
   - Process, route, header: a server test that starts the process once.
   - A browser only for what needs its engine: layout, CSS, real focus and keys, navigation, storage across tabs. One browser journey covers a flow; its conditions go a layer down.
5. **Prefer an invariant to an example.** A rule checked after every step of generated histories survives refactors and covers cases nobody listed. Write an example when the case is specific and no invariant states it.
6. **Place it by cost.** Each second in the every-change suite is paid on every change. Decide whether the fault needs checking on every change, daily, or only when its code changes, and put the test there.

## Writing it

- Follow the [test-behavior-not-implementation](../principles/references/test-behavior-not-implementation.md) principle: derive expected values from the requirement, not from a run of the code.
- The title states the promise; a failure shows expected and actual in the user's terms, so the reader knows what broke without opening the code.
- No sleeps, wall-clock deadlines, fixed ports, shared directories or order dependence. A test that fails only beside others shares something with them; fix the sharing.
- Wait on a signal, not a deadline: await the operation, or a promise that the handler or callback recording the event resolves. Polling a recorder or spy until a timeout fails under load. To move time, use the framework's fake clock.

## Prove, then decide

1. **Prove it.** A test of new or fixed behaviour must fail without the change for the intended reason, not because a symbol is missing, and pass with it. A test that pins behaviour a refactor must keep passes before and after, and fails under a deliberate break of that behaviour.
2. **Keep it only when all hold:** a plausible later change to code that stays could break the behaviour unnoticed; it catches a behaviour break and survives a refactor that keeps behaviour (that principle's two edits); no other kept test catches the same fault; it is fast and deterministic; its failure is actionable.
3. **Drop it** when the fault cannot recur there: a one-time script or data repair retired after its run, a path the change removed, a test that only restates a value. A migration that new or restored databases still run is code that stays, so its test can stay.
4. **How a dropped proof leaves:** where the project's guide gives proofs a place outside the suite, write them there and quote the deciding lines in the pull request. Otherwise commit the test with the change and remove it in its own last commit, so the history shows it fail and pass and a revert restores it.

## Changing the suite

- **A flaky test is a defect.** Retrying it or raising its timeout hides the defect; neither is a fix. Give it one fix whose cause is shown: a shared resource, an unordered read, a deadline below the work. With no cause found, delete it or move it to a schedule that tolerates load. A test guarding a security boundary, stored data or a merge decision stays until the cause is known; its flake may be a real race.
- **Deleting is normal.** Delete a test whose fact a cheaper kept test holds, whose state a refactor made unreachable, or whose feature is gone, and name the holder or the reason. When reading cannot tell which overlapping tests matter, measure: make small edits to the code they run and keep the smallest set that still fails on every edit.
- **Scale checks to what a failure costs.** Production paths and stored data get the strongest checks. Internal tooling gets a proof, not a kept test, unless a mistake there is costly to undo.

## Report

In the pull request or reply:

- each behaviour change and its proof (the deciding failing and passing lines);
- each kept test, the fault it catches and why it sits at that layer;
- each dropped or deleted test, with its holder or reason, and the commit that removed it;
- the time added to the every-change suite, when measurable.
