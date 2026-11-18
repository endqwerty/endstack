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
  script trips every check and asserts each line names a fix.
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
| flaky | N | `join()` on the returned thread; read no skill | the same |
| flaky | S | the same | the same |
| comments | N | deleted the narration, the dead `_total` and the `IMPORTANT` comment, which became a test; kept the docstring | the same, but kept `_total` |
| comments | S | the same as N | the same as N |
| pin | N | comment deleted; reason moved into a new test's failure message | kept a two-line prose comment |
| pin | S | one `WARNING:` line naming the hazard and its test, plus that test | one `WARNING:` line naming the hazard and who approves an upgrade |

Every flaky run's suite passed 40 of 40 reruns, and every comments run's
suite passed. Each pin-task suite passes apart from the fixture's own flaky
notifier test, which that task does not touch.

Reading:

- **pin** is where the change works. Without it, the two runs went two
  different ways: one dropped the comment, the other kept a paragraph.
  With it, both wrote the single-line `WARNING:` form, 2 of 2.
- **flaky** and **comments** show no uplift. The flaky fix was easy enough
  that no run read a skill: every run joined the thread. In the comments
  task the constraint could be tested, so both arms encoded it and deleted the
  comment, as step 5 already says. The new section did not change anything
  there, and it did not break anything either.
- The check-script messages were not dry-run: no run tripped a check. The
  unit tests show that each problem carries a fix.

## Not checked

- One sample per cell: a direction, not a rate.
- A flaky test that tempts an agent to retry or raise its timeout. This
  fixture's fix was too obvious to show that, so the `test-design` wording
  has no evidence of uplift.
- Whether the shorter fix messages help an agent repair a skill faster.
