# tdd: decide whether a test stays

## Why (2026-10-31)

Daniel: "because Pstack relied so heavily on writing a failing test first,
lots of tests got added. Maybe the agent needs to consider if the failing test
should even be committed into the repo at the end of working."

`tdd` asked for a failing test per faulty place and said to commit it before
the fix. Nothing asked whether the test earned a place in the suite once it
had proved the fix. The one hint pointed the other way: "prefer no new test
over a bad test", where a bad test included one that "would be deleted
immediately after proving the fix". That either skips the red-then-green proof
or, when the agent writes the test anyway, keeps it.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes;
   `tdd`'s SKILL.md stays under 6000 bytes.
2. `ROUTING.md` is unchanged, so homelab's copy still matches.
3. Dry run, with and without the change, on a fixture with two bugs: one in
   product code that stays, one in a one-off backfill script that its own
   docstring says is deleted after one production run. Pass for "with": the
   product test stays, the backfill test is not in the final tree, and the
   reply says which tests stayed and why. The "without" arm is reported as it
   comes out.

## What changed

- `skills/tdd/SKILL.md` (5539 bytes): new step 7, "Decide whether the test
  stays". Keep a test when a plausible later change to code that stays could
  bring the bug back unnoticed, it passes the two edits of
  test-behavior-not-implementation, it is fast and deterministic, and no
  existing test covers the case. Drop it when the bug cannot recur there (a
  one-time script, migration or data repair, a path the fix removed, a test
  that only restates a value). A dropped test comes out in its own last
  commit, so the history still shows it fail and pass, and reverting that
  commit restores it. The final response says which tests stayed, which were
  dropped, and the dropping commit. The "would be deleted immediately" clause
  is gone from the definition of a bad test.
- `skills/build/references/design.md` step 8 and the sequence-verifiable-units
  principle carry the same rule in one sentence each, for feature work that
  goes through `build` without `tdd`.

Turned down:

- **Never committing a dropped test.** Cheaper, but the failing-before proof
  then lives only in the pull request text, the reviewer cannot rerun it, and
  restoring it means retyping it. A test committed and then removed in its own
  last commit costs one commit and survives a merge commit.
- **A rule in `verify`.** It is a core skill at its 2.2 KB limit, and its
  author step already says "a failing check", not "a test". A check does not
  have to be kept, so `verify` needs no change.
- **Dropping regression tests by default.** A bug that came from a plausible
  mistake in code that stays usually recurs, so the default is to keep those.

## Dry run (2026-10-31)

Fixture: [tdd-keep-runs/fixture/](tdd-keep-runs/fixture/), a six-file Python
package. `parse_duration` overwrites its total instead of adding to it
(`1h30m` gives 1800); `scripts/backfill_slugs_2026_10.py` loops over
`rows[:-1]` and skips the last row of each batch. Prompt, the same for every
run: "Two bugs were reported. Fix both: `shiplog freeze --for 1h30m` freezes
releases for 30 minutes instead of 90. The OPS-412 slug backfill left some
releases without a slug on staging. Fix it before tonight's production run."
Each run was told to follow `tdd` at a given path: without, `main` at
`f163585`; with, this branch. Claude Code subagents on Sonnet 5.5, file and
shell tools, each in its own scratch repository. Scored from each repository's
`git log --stat` and `git ls-files tests` at the end; every final tree passes
its suite and has the `+=` fix.

| Run | Duration test | Backfill test | Backfill proof |
| --- | --- | --- | --- |
| without 1 | kept | never written: "a test for it would go with it" | an unsaved inline script |
| without 2 | kept | kept, three tests; a docstring line says to delete them with the script, "If it is left behind, the suite fails on the missing import" | failing test committed |
| with 1 | kept | written, failed, then removed in its own last commit (`9e24cd1`) | failing test in history |
| with 2 | kept | written, failed, then removed in its own last commit (`f32769c`) | failing test in history |

With the change, both runs kept the product test, dropped the one-off test,
and left a red-then-green record a reviewer can replay. Without it, one run
already avoided the test (through the clause this change removes) but kept no
replayable proof, and the other committed a test that breaks the suite on the
script's planned deletion. Two runs per side on one model: a sample, not a
rate. Not exercised: a case where the right call is to extend an existing
test, and a feature built under `build` without `tdd`.
