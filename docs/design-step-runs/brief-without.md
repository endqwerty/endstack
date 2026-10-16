# Brief: quarantine a test

Queue item 1 of 2. Item 2 (cancel a queued tracker request) is a separate brief.
Follow the `build` skill. This repository has no remote, so do not push, open a
pull request, or start a reviewer. Report the change as unverified.

## Why

A flaky or known-broken test fails the gate for every change. An operator needs
to take that test out of the verdict without deleting it or hiding it, and
everyone reading a change must still see that it is quarantined and why.

## Outcome

1. An operator can quarantine a test by name and must give a reason.
2. A failed result for a quarantined test no longer makes the verdict `fail`.
3. `gatekeep show` (`src/cli/changes.ts`) and the change page
   (`src/web/changes.ts`) both mark quarantined tests, with the reason.

## Decisions already made

- **Scope is the test name, across all changes.** Results and tracker requests
  already identify a test by its name alone. A quarantine is one record per test
  name, and it applies to every run, old and new, because the verdict is
  computed when it is read.
- **A reason is required.** Reject an empty or whitespace-only reason. Do not
  add users, roles, or authentication. The repository has none, and "operator"
  means whoever calls the quarantine method.
- **Quarantine changes the verdict, not the result.** `Result.outcome` stays
  `failed`. A quarantined failure is shown as failed and as quarantined.
- **Quarantining a test that is already quarantined replaces the reason.**
- Out of scope, do not build them: lifting a quarantine, listing quarantines,
  expiry, an HTTP route, any change to tracker requests.

## Design constraints

- Both clients read through the `Api` interface in `src/server/api.ts`. Add the
  quarantine operation and the data the clients need there, so the two clients
  cannot disagree. Neither client may keep its own list of quarantined tests.
- `verdictOf` in `src/core/model.ts` is the one place that turns results into a
  verdict. Give it the quarantine information as an input. Do not filter
  results in `Store` before calling it.
- Model the domain before writing branches. A result is either counted or
  quarantined, so carry that as data on what `results` returns (for example a
  `quarantine: { reason: string } | null` field on the returned result), not as
  a second list the caller must join by name.
- Keep the change small. Match the surrounding code, including tab indentation
  and the existing comment density.

## Verdict rules to pin down in tests

- A run with one failed quarantined test and one passed test is `pass`.
- A run with one failed quarantined test and one failed unquarantined test is
  `fail`.
- A run whose only result is a failed quarantined test is `pass`. Only an empty
  run is `pending`.
- Quarantining a test after a run was pushed changes that run's verdict.

## Checks to write first

Write these in `src/changes.test.ts` before the implementation, and watch each
one fail for the right reason.

1. The four verdict rules above, through `Store.gate`.
2. `Store` rejects a quarantine with an empty reason and leaves the verdict
   unchanged.
3. `show` prints a quarantined failed test with a visible marker and the
   reason, for example `  failed  login [quarantined: flaky on CI]`, and the
   header line shows `pass`.
4. `changePage` marks the same row, for example by adding a `quarantined` class
   and the reason to the `<li>`. Existing exact-string tests for unquarantined
   output must keep passing unchanged.
5. `bun test` passes in full.

The exact marker text is your call. Both clients must show the word
`quarantined` and the reason.

## Delivery

Commit on the current branch with a clear message. Report what changed, which
checks you ran with their deciding output, and that the change is unverified
because no independent verifier can run here.
