# Statechart beside archify

## Why (2026-10-30)

Daniel asked to look into pstack's formal verification and state diagram
generation, compare it with archify and "maybe" consolidate into pstack's
state diagram. pstack added a `statechart` skill on 2026-10-21, after the
`190d287` review: it checks a TLA+ model with TLC and draws the states TLC
finds as a Mermaid statechart, marking each state that breaks a rule and giving
the shortest path to it. On 2026-10-23 pstack's create-formal-verification-skill
gained one paragraph telling the generated skill to read TLA+ results with it.

## Decision

Not consolidated. Statechart draws one kind of diagram and needs a TLA+ model
for each chart; archify draws ten kinds (architecture, sequence, ERD, flat
lifecycle and others) from authored JSON and makes one-page explainers, and
its lifecycle type has no nesting, parallel regions or rule marks. Archify's
Mermaid input rewrites a `stateDiagram` into its own lifecycle, so it cannot
carry a checked chart either. They overlap only on a state diagram that must
be right, which goes to statechart.

- Statechart is installed by homelab unchanged from upstream, pinned to
  `cursor/plugins` `4dd1d05`, not ported into `skills/`: its 3,900-line
  compiler and 5,500 lines of tests are deterministic work that endstack's
  rules keep out of a skill, and a port would be a code import to maintain.
  Homelab adds only `agents/openai.yaml` (its new `"explicit"` source field),
  since upstream has no Codex policy file.
- create-formal-verification-skill takes upstream's paragraph, with a skill
  name where upstream links a sibling path that does not exist in this
  repository.
- ROUTING.md gains one bullet: a state diagram goes to `statechart` when it is
  drawn from a checked model or shows a bug as a path, otherwise to `archify`.
  `scripts/check-routing.py` accepts these two names, which are not in
  `skills/`, and still requires each to appear at most once.

## Checks

- Before editing: both checkers at 0 problems, ROUTING.md at most 2,600 bytes,
  the formal entrypoint under 6,000, a routing test for external names seen
  failing first; a paired routing run and a paired formal run.
- After: `check-skills.py` and `check-routing.py` report `0 problem(s)`;
  ROUTING.md 2,552 bytes, the formal entrypoint 5,714; `Ran 17 tests` / `OK`
  (the new test failed before the checker change).
- Statechart itself, run on omarchy on a three-variable model with a planted
  stale-ack bug: exit 1 in 5.6 s, and the report read
  `SyncedMeansSaved breaks` / `The shortest path has 2 steps`. The copy
  installed by homelab's sync into a scratch home ran a passing model with
  exit 0.

## Dry runs

Headless Claude Sonnet 5.5, medium effort, no tools, one sample per arm,
2026-10-30, from a scratch directory. Full prompts and responses are in
[statechart-runs/](statechart-runs/). Routing arms got ROUTING.md before or
after the change and five prompts; formal arms got the entrypoint before or
after and a request to write the generated skill for a TLA+ model of a job
queue.

| Prompt | Before | After |
| --- | --- | --- |
| Draw a checkout order's states for a PM | `how` | `archify`, "Nobody asked for a checked model" |
| Show, checked against a model, how "Synced" shows for an unsaved edit | `create-formal-verification-skill` | `statechart`, formal creation first if no model exists |
| Draw the payment service architecture | `how` | `archify` |
| Fix a double-pickup race with a regression test | `tdd`, `build`, `verify` | the same; no formal or statechart route |
| Prove the lease protocol never has two writers | `create-formal-verification-skill` | the same |

The generated skill from the new entrypoint says "Read every result with the
`statechart` skill" and "Do not copy its commands into this file"; the one
from the old entrypoint does not mention it. Both embed their own TLC command
for running the check, which is the model check, not statechart.

Not checked: a live agent run of statechart picked by routing, Codex
routing, and the Mac, which has no `mise` (homelab `workstation.md` records
what its first run needs).
