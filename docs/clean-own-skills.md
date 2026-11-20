# Cleaning up endstack's own skills (2026-11-20)

## Why

After taking pstack's cuts ([#41](https://github.com/endqwerty/endstack/pull/41),
[#42](https://github.com/endqwerty/endstack/pull/42)), Daniel asked to clean up
the skills endstack wrote itself and to check the catalog as a whole. Four
read-only audits ([audits](clean-own-skills-audits/)) went rule by rule through
the eleven endstack-written skills (D, E, F) and judged the catalog with usage
from 2,400 T3 threads on omarchy (G). Daniel approved every recommendation;
evidence-backed rules stay.

## What changed

Skills: 35 to 28 (5 core, 23 role). All skill files: 182 KB to 144 KB.

- **Routing** (ROUTING.md 2,491 to 2,234 bytes): `how` and `why` load only
  when the user asks how or why (53% and 59% of their loads were review
  threads); "Every task, first: `swarm`" goes (42% of swarm loads were in
  review threads, and it clashed with keeping trivial work local).
- **Merges:** `tdd` into `test-design` (a "Bug fix: fail first" section),
  `teach` into `how`, `reflect` into `correct`, `ketchup-video` into
  `ketchup/references/video.md`, the two formal-verification skills into
  `formal-verification`, `figure-it-out` into `show-me-your-work`.
- **Removed:** `recall` back to `candidates/` (no loads in six weeks); three
  principle leaves nobody read (never-block-on-the-human,
  outcome-oriented-execution, encode-lessons-in-structure).
- **Delivery skills:** the "plan explains, stop means no writes, preserve the
  branch, report what landed" tail copied into four skills goes; `build`
  2,178 to 976 bytes, its design step 7.2 KB to 4.7 KB; `babysit`, `ship`,
  `autopilot-full`, `verify` each lose rules that repeat the global rules,
  ROUTING or each other. Kept: ship's land-without-asking, its rule that an
  agent's own choice never authorizes a merge, holds and reserved gates;
  verify's reachability ranking, cheapest check, report-unverified and
  carry-forward patch comparison; build's read-the-design-step-first.
- **test-design, interview, goldfish:** duplicated and unmeasured rules go;
  goldfish's `standards.md`, Structure role and pattern catalog go
  (references 14.5 KB to 7.9 KB).
- **drift, orchestrate, principles index:** repeated rules go (orchestrate's
  four "never writes code", drift's "one question at a time"), and the
  index's "name each principle" rule, which only changed reply wording.
- **Structure:** `interrogate` states its own fan-out instead of citing
  arena's step numbers; dead pointers in `benchmark-checklist`, `no-comments`
  and `ketchup` are fixed; `technical-writing` drops sentence rules that
  repeat `unslop`.

## Dry runs

One fresh agent per arm, old text against new, one sample each
([runs](clean-own-skills-runs/)):

- **build** (archive-tasks feature): both produced the same tagged-state
  shape, fixed the web and CLI consumers through one shared filter, named
  tests, and planned architect, the design doc and goldfish (tool-free arms
  describe these steps; they did not run them). The new arm skipped
  `interview`, whose trigger now lives only in ROUTING, which the arm did not
  see.
- **ship** ("how would you ship PR #12?"): both explained and acted on
  nothing, so the dropped plan-explains sentence changed nothing.
- **routing** (review a diff before merge): the old routing said it would
  open `swarm` as a forced first step and then decline it; the new routing
  said it would open only `verify` and `unslop`. Neither arm loaded `how` or `why` here, so the
  measured misrouting did not reproduce in one shot.
- **test-design with tdd merged** (a fault shared by two consumers plus a
  copy): both found all three places, deleted the redundant cap and committed
  failing tests first; the new arm wrote 2 tests, the old 5 and dropped 3.
- **orchestrate** (14-endpoint migration): both sent one early message of
  questions with defaults, piloted one unit, left a typo to its owner and let
  owners land through ship; the new text kept "don't merge" stopping owners.

Limits: one sample per arm, one model; re-measure usage after
2026-12-20 for the skills G held (orchestrate, arena, sharpen, interview,
goldfish, drift, test-design).
