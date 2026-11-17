# test-design: what test to write, where, and whether it stays

## Why (2026-11-16)

In Mainworthy, Daniel's messages from 2026-10-25 to 2026-11-16 return to one
complaint: agents add too many tests, reach for end-to-end tests, keep tests
whose failure says nothing actionable, and duplicate tests that already hold
the fact. The project's testing guide had most of the rules, but agents met
them only after writing the test, when a CI job or review refused it. `tdd`
covered bug fixes only; adding a feature, refactoring or deleting tests routed
to no skill.

`test-design` is the decision an agent makes before and after writing a test:
name the reachable failure and who acts on it, find the test that already
holds the fact, make the code cheap to check, pick the cheapest layer, prefer
an invariant, place the test by cost, prove it, then decide whether it stays.
`tdd` keeps the fail-first workflow and takes its keep and drop rules from
`test-design`, so the two lists cannot drift.

## Checks

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes.
2. ROUTING.md stays within 2,600 bytes, and the trims keep each other
   route's trigger: `create-formal-verification-skill` still needs an
   explicit request, `no-comments` still covers removing any comments,
   `benchmark-checklist` still covers performance numbers, and `tdd` still
   fires when a failing test is asked for.
3. Dry run, without and with the skill, on [the fixture](test-design-runs/fixture):
   a checkout service with a unit test file and a server test file, and the
   task "a big coupon can make the total negative; fix it and make sure it's
   tested". Pass for "with": tests at the unit layer only, each shown failing
   before the fix, a test of new behaviour that passes on base not kept, and the report the
   skill asks for.

## Dry run (Sonnet 5.5, medium effort, one run per arm)

- Without: clamped the total with `Math.max(0, …)`, added two unit tests
  (fixed coupon over the subtotal, percent over 100) to `src/cart.test.ts`, no
  server test. It did not run the tests against the old code: "I haven't seen
  them fail first."
- With: the same code change and the same two unit tests. It ran them on the
  old code first (`Expected: 0 Received: -1` and `Received: -1250`), wrote and
  then dropped a coupon-equals-subtotal test because "it passed before the
  fix", dropped a duplicate fixed-coupon assertion, explained why no server
  test (the route only passes the body to `total`), and reported the time
  added ("under 1 ms").

- With, rerun on the final skill text (after review): the same code change,
  one unit test in `src/cart.test.ts` committed with the fix, shown failing
  first (`Expected: 0 Received: -1`), no server test, and the full report.
  It folded four assertions into that test, including the coupon equal to
  the subtotal, which already passed on base; the test as a whole still
  fails without the change. The first "with" run (on the reviewed draft)
  dropped that boundary case instead.

The fixture separates the arms on proof and keep discipline, not on layer
choice: both arms chose the unit layer. A layer-choice difference needs a
larger repository where the fact is already held at another layer; Mainworthy's
`kept-tests` job and weekly prune measure that in practice.

## Review

A fresh read-only reviewer (Opus 5.5, high effort) found five issues; all were
fixed before the pull request:

- The first draft said to keep unkept proofs only in scratch space, which
  contradicted `tdd`, build's design step and sequence-verifiable-units (commit
  the proof, remove it in its own last commit). Now the project's guide decides
  where proofs go, and otherwise the commit-then-remove rule applies.
- "Keep only when it failed without the change" would drop a characterisation
  test before a refactor. Now such a test is proved by passing before and
  after and failing under a deliberate break.
- One-time scripts lost the migration exception; it is back.
- The keep rules lived in both skills and had already drifted; `tdd` now
  points to `test-design`.
- The first ROUTING.md trims changed other skills' triggers; they were
  restored and the bytes found in wording that kept its meaning.
