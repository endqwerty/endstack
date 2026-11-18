# Lessons from landmines

Why: [interfere-inc/landmines](https://github.com/interfere-inc/landmines)
(0.1.0) is a set of lint rules that block the shortcuts agents take to turn
checks green: mocks, fixed sleeps, polls against a deadline, retries, raised
timeouts and narrating comments. Most of these restate rules endstack already
has in prose. The lint is not imported. Three ideas behind it are worth
taking:

- **Every failure names its fix.** A landmines message says what to do
  ("await the operation itself or a promise its handler resolves"), so the
  agent that tripped it repairs it in the same pass. `check-skills.py` and
  `check-routing.py` printed only what was wrong.
- **A fixed shape for comments that stay.** landmines allows tool directives,
  single-line `WARNING:` comments for dangerous recurring footguns, and docs
  on exported public API. `no-comments` lost its Comment Sicko exception
  catalog when it was imported ([W3](import-notes/W3.md)), so it had no list
  of what may stay and no format for a keep.
- **Two test-design gaps.** Waiting on a signal instead of polling a recorder
  until a timeout, and calling retries and raised timeouts what they are:
  ways to hide a flake.

What changes:

- `scripts/check-skills.py`, `scripts/check-routing.py`: each problem ends in
  `; <fix>`. `FORBIDDEN` entries carry their fix as a third field. A test per
  script trips every check and asserts each line ends in a fix; it checks
  that a fix is there, not that following it clears the problem.
- `test-design`: one bullet under *Writing it* (wait on a signal; fake clock
  to move time) and one sentence on flaky tests (retrying or raising the
  timeout hides the defect).
- `no-comments`: a *What may stay* section; step 1 points to it when the role
  definition is missing.

Turned down:

- **landmines' allowlist that only shrinks** (an exact per-file count that
  fails when a file has fewer violations than allowed). It fits a
  check that has grandfathered exceptions; endstack's checks have none
  today. Revisit when one gets an exception.
- **A no-mocks rule in a skill.** `no-test-doubles.ts` is 2,356 lines,
  which shows how hard "a mock" is to define mechanically. The prose rule in
  `typescript-best-practices` stays as is.
- **`no-explicit-return-types`.** That is a taste call, and many codebases
  want explicit return types on exported functions.
- **Adopting the package.** That is a decision for each TypeScript project
  and too early at 0.1.0. Skills cannot name it anyway.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts -p 'test_*.py'`
   passes, and the two new tests fail against `main`'s scripts.
2. Dry run in [the fixture](landmines-lessons-runs/fixture): arm N gets
   `skills/` and ROUTING.md from `main`, arm S from this change. One run per
   cell, at medium effort. Prompts name no skill. Script:
   [run.sh](landmines-lessons-runs/run.sh).
   - **flaky:** `test_send_delivers_stripped_message` (a 50 ms poll on a
     thread that takes up to 80 ms) fails about one run in three. Pass: the
     poll is replaced by a wait on the operation, with no retry or longer
     deadline.
   - **comments:** clean up `client.py`. It has narrating comments, a
     docstring on an exported function, a misplaced `noqa`, and an
     `IMPORTANT ... do not remove` comment on a check the tests can cover.
   - **pin:** clean up `requirements.txt`. A three-line comment explains a
     pin nothing in the repository can test (an outside proxy rejects
     urllib3 2.x). Pass for arm S: the reason stays as one `WARNING:` line.
3. Independent review of the diff and this reading by a verifier from each
   provider.

## Results (2026-11-17)

Claude Opus 5.5 and GPT 6.2 Sol, both at medium effort.

| Task | Arm | Claude | Codex |
| --- | --- | --- | --- |
| flaky | N | read `test-design`; first committed `join(timeout=5)`, then dropped the timeout after its own review | read `test-design`; `join()` on the returned thread |
| flaky | S | read `test-design`; `join()` straight away | the same as N |
| comments | N | deleted the narration, the dead `_total` and the `IMPORTANT` comment, which became a test; kept the docstring | the same, but kept `_total` |
| comments | S | the same as N | the same as N |
| pin | N | comment deleted; reason moved into a new test's failure message | kept a two-line prose comment |
| pin | S (first text) | one `WARNING:` line naming the hazard and its test, plus that test, whose message dropped the reason | one `WARNING:` line naming the hazard and who approves an upgrade |
| pin | S (final text) | test with the reason in its failure message; comment deleted | one `WARNING:` line naming the hazard and who approves an upgrade |

Every flaky run's suite passed 40 of 40 reruns. In the comments and pin
runs, every test the agent touched passed; the fixture's own flaky notifier
test, which those tasks do not touch, failed now and then.

Reading:

- **pin** is where the change works, on Codex. Without it, Codex kept a
  two-line prose comment; with either text it wrote one `WARNING:` line.
  Claude on `main` already did what step 5 asks: it encoded the pin as a
  test, put the reason in the failure message and deleted the comment. The
  first text made Claude keep a `WARNING:` line beside the test and drop the
  reason from the test. Review caught that; the final text says an encoded
  constraint keeps no comment, and the rerun on it went back to the test-only
  result. So the change fixes Codex's prose keep and, in its final form, does
  not regress Claude.
- **flaky** shows little uplift. Every run read `test-design` and ended on
  `join()`. The one difference is the arm-N Claude run, which first bounded
  the wait with a timeout and removed it only after its own review; one sample
  cannot say whether the new wording caused that.
- **comments** shows no uplift. In the comments
  task the constraint could be tested, so both arms encoded it and deleted the
  comment, as step 5 already says. The new section did not change anything
  there, and it did not break anything either.
- The check-script messages were not dry-run: no run tripped a check. The
  unit tests show that each problem carries a fix.

## Not checked

- The final-text pin runs used the wording before the last review round,
  which scoped step 2's proof to hazard comments and fixed three check-script
  messages. Both edits leave the pin case unchanged; neither was run again.
  The final-text Claude run was stopped while it re-reviewed its own staged
  test; its result is that staged diff.
- One sample per cell: a direction, not a rate.
- A flaky test that tempts an agent to retry or raise its timeout. This
  fixture's fix was too obvious to show that, so the `test-design` wording
  has no evidence of uplift.
- Whether the shorter fix messages help an agent repair a skill faster.
