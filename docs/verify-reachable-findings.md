# Verify: a finding names what reaches it

## Why (2026-10-27)

Daniel asked Mainworthy's agents twice to stop guarding against states the
design rules out ("Don't overly guard against situations that have been
architected to not happen", 2026-10-24; "Only guard if it's absolutely
critical to do so", 2026-10-25). The rule went into Mainworthy's `AGENTS.md`,
which only the author reads. The verifier (this skill) and the Daybreak
security audit (project instruction files off) never saw it.

A read-only study of 32 guards added in 12 Mainworthy pull requests (merged
2026-10-22 to 10-27, chosen from review answers and removed guards, so not a
repository-wide rate) classified each by where it came from and what reaches
the guarded state:

| Origin | Reachable (input, stored or imported data, race) | Ruled out by design | Only a later change |
| --- | ---: | ---: | ---: |
| verifier | 13 | 1 | 0 |
| Daybreak audit | 14 | 1 | 1 |
| author | 1 | 0 | 1 |

The four unneeded guards (80 added lines, three later removed or replaced)
share one shape: a bad outcome with no present path to it. Three came from a
finding: "A for_each keyed by a value would print that key" (every key was a
literal); "a future quadratic parser could let an authenticated pipeline stall
the server" (the parser runs in the CLI); "pull-request workflow code can read"
repository variables (only the owner can open pull requests). The fourth was the
author's own: a throw in a test fixture because "a blow-up would hang the run",
with no change causing one. Mainworthy's own rule already covers an author;
this change reaches the verifier and the audit, which wrote the other three.
The counterexample matters as much: a strict reader looked unreachable because
every normal writer was correct, but an imported archive bypassed them
(Mainworthy #836, #848). So the rule names stored and imported data as paths,
not only callers.

The study found no broad habit of guarding: 28 of 32 guards had a real path.
The fix is narrow on purpose.

## What changed

- Verifier: "An issue names what reaches it in this revision: an input or
  caller, stored or imported data, a race. A state only a later change makes is
  a note."
- Author step 5: "Fix each reachable finding" (was "each real finding").
- To stay under the 2,200-byte core limit, wording elsewhere was shortened with
  no change in meaning; "if review cannot run, stop unverified" was dropped as a
  repeat of step 3, and "A review limit is not approval" stays.

Mainworthy's audit brief gets the same requirement in its own pull request.

## Dry run

Each run is one GPT 6.1 Sol (high) verifier holding only the old or the new
`SKILL.md`, the commit messages as the task, an export of the head and the
diff, in a read-only sandbox with no database (so every runtime check is
"not checked"). One run per cell; a model run varies, so a cell is a sample,
not a rate.

| Past state | What happened then | Old text | New text |
| --- | --- | --- | --- |
| Mainworthy #937 at `8bcef22f`, before the instance-key guard | Verifier asked for a guard for value-keyed `for_each`; later removed as unreachable | Did not raise it; raised a real replacement-output gap | Did not raise it; raised the same gap and said what reaches it: "Existing resources can reach this through replacement plans" |
| Mainworthy #970 at `3b79e9ba`, imported spans | Verifier found an imported half span; a later round an imported out-of-range end | Found the half span | Found the half span and the out-of-range end: "Archive import accepts bigint values without validating them" |

The case the change targets did not reproduce under the old text, so these two
runs show that the new text keeps reachable findings (including the
imported-data path), not that it suppresses hypothetical ones. The Daybreak
replay in Mainworthy's pull request, which uses the same requirement, did
reproduce two hypothetical findings under the old brief and dropped both
under the new one.

Not exercised: an author answering a verifier's unreachable finding over
several rounds, and a project with no import or stored-data path.
