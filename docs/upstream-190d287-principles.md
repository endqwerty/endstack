# Principles: upstream rewrites and a readable design note

## Why (2026-10-21)

Two findings from the same review.

- **Upstream rewrote four principles.** pstack (`cursor/plugins` at
  `190d287`, 2026-10-20) restated four principles "as reasoning, not rules"
  in [e5136d8](https://github.com/cursor/plugins/commit/e5136d8): each had
  banned or prescribed a mechanism (matcher names, nil-check guards, an actor
  census, process-ID locks) that is wrong outside the case it was written for.
  [36cecbf](https://github.com/cursor/plugins/commit/36cecbf) added a
  follow-up to Fix Root Causes. No principle was added, removed or renamed. Six
  others were only shortened upstream, because pstack's per-turn mode restates
  their rules; endstack has no such mode, so they stay as they are.
- **The principles are read but not reported.** T3 Code threads since the
  design step was installed (2026-10-16 14:19 to 2026-10-21, Mac only): Claude
  leads that edited code read the principles index in 13 of 14 threads (6 of 6
  where Daniel typed `$principles`, 7 of 8 where he did not), and Codex
  builders in 36 of 37. Typing `$principles` changed nothing measurable. But
  Claude leads named a principle in chat in 1 of 14 of those threads, and of
  169 Mainworthy pull requests opened in that window, 127 have a "Why this
  approach" section and 3 name a principle. The design step already asked for
  the principles in "why this approach"; nothing checked it.

## What changed

- `skills/principles/references/`: `attack-the-premise.md`,
  `fix-root-causes.md`, `make-operations-idempotent.md` and
  `test-behavior-not-implementation.md` take upstream's new bodies, with
  sibling links pointed at endstack's references.
  - Attack the Premise: test the premise with an observation that would come
    out differently if it were false, instead of a census of which actors hold
    an imbalance.
  - Fix Root Causes: the root cause is the first wrong decision; a guard is a
    fix only when the state it handles is legitimate; after a deep dig,
    propose the cheap, always-on signal that would have shown the fact.
  - Make Operations Idempotent: derive each step from the state that exists and
    apply only the difference; leftovers must be recognisable as stale wherever
    the last run stopped. The process-ID lock recipe goes.
  - Test Behavior, Not Implementation: judge a test by two imagined edits,
    breaking the behaviour (it must fail) and changing the internals (it must
    pass). The contract decides, not the assertion's shape.
- `skills/principles/SKILL.md`: the four index lines follow (5845 bytes).
- `skills/correct/SKILL.md` step 3: the two imagined edits replace "would
  still pass if every function it calls returned nothing".
- `skills/build/references/design.md`: step 7 asks how the next run recognises
  and reconciles what an interrupted one left; step 8 asserts what the contract
  promises instead of "a literal outcome"; the design note ends with one line,
  `Principles: <name> (<the choice it changed>); ...` or
  `Principles: n/a: <reason>`, that a project's checks can read.
- Mainworthy (separate pull request): its `description` CI job fails a pull
  request whose description has no such line, names something that is not in
  the index, or says `n/a` without a reason.

Turned down:

- Copying upstream's shortening of the six other principles. It relies on a
  mode endstack dropped.
- A reminder in `build` or `verify` to cite principles. Both already ask for
  it in prose and are at their size caps; the measurement shows prose is what
  failed. A check in the project's CI is the stronger guard (`correct`, level
  2), and Mainworthy, where 169 of the window's pull requests were opened,
  already runs one on every description.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` prints `OK`.
2. Each of the four references matches upstream's body at `190d287` apart
   from frontmatter and link targets.
3. Dry run, old and new text, below.
4. Mainworthy: a test fails before the check exists and passes after; the
   check run on real past pull requests reports the missing line.

Results: 1 passes (`0 problem(s)` twice, `Ran 16 tests ... OK`). 2 passes by
diff. 4: the new test failed first (`Export named 'principles' not found`),
then `25 pass, 0 fail`; `pr-body` on #673, #678, #683, #700 and #715 each
printed `The description has no \`Principles:\` line.` (#683 wrote "Principles
that shaped it:", which the fixed line does not accept on purpose).

## Dry run (2026-10-21)

Each scenario was decided by Sonnet 5.5 at medium effort with no tools,
holding only the old or only the new reference text, one sample each. The
prompts name no change.

| Scenario | Old text | New text |
| --- | --- | --- |
| Crash on an unassigned test case; unassigned is a supported state | fix in `renderAssignee`: "Handle unassigned explicitly there" | same: "the code that doesn't handle a legitimate state". No uplift |
| `order.total` is NaN; a total must always be a number | fix at checkout, "A `Number.isNaN` check there would only hide the bug" | same. No regression |
| Report after a four-hour hunt for skipped CSV rows | reconciliation alert among seven items | "That signal would have shown this at first look instead of after four hours" |
| Test pins an error message no caller reads | rewrite to assert the error type | same. No uplift |
| `charge` not called for an empty cart, paired with a test asserting the charge payload | **rewrite**: "`not.toHaveBeenCalled()` is an absence-only check" | **keep**: "a missing `charge` call is something it can observe" |
| Two fixes assumed "the upload is slow" | "write a rerunnable census script ... remove the asymmetry" | "Check whether each failure took exactly the timeout ... which means a hang, not slowness" |
| PID lock file after crashes; PIDs reused after reboot | PID plus start time plus boot ID, reclaim stale | "use a kernel-held lock, not a PID file ... A stale lock therefore can't exist" |
| Write the design note for a change whose principles are given (2 samples each) | principles listed in prose, 2 of 2; no fixed line | ends with `Principles: Model the Domain (...); Subtract Before You Add (...)`, 2 of 2 |

The rewrites change the decision where the old rule overreached (the paired
absence test, the census, the lock) and leave the plain cases as they were.
The design-note run hands the model its principles, so it shows only the
format; whether real sessions put the note in the pull request is what
Mainworthy's check enforces.

## Not checked

- Real sessions after the change. The dry run is one model's stated decision,
  one sample per row.
- Projects other than Mainworthy have no check on the line. homelab and
  endstack open few pull requests; add one if they start to.
- Pull requests open when Mainworthy's check lands fail its `description` job
  until their description gains the line.
