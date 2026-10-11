# Codex follow-up decisions

Read-only simulation of Q–T from `docs/delivery-follow-up-fixtures.json`; no case operations performed.

## Q — babysit + verify

Proposed next action: report missing independent review as the blocker and hand back to the owner; end any existing watch at handoff. Payment behavior has no nonbehavioral exemption. Passing checks and host mergeability do not establish readiness, even though the transient failure cleared without a revision. With no reviewer available, stop **unverified, not merge-ready**; do not merge or call it done.

Deciding words: babysit says “Even without revisions, ready requires a current independent verdict or valid exemption”; verify says “Without one, report unverified” and “if review cannot run, stop unverified.”

## R — build

Proposed next action: cease implementation and PR preparation immediately; report the unpublished change and that no external write is in flight. Preserve the existing work without additional writes, publication, commits or cleanup edits. Readiness is not established by the fixture; stopping follows the explicit cancellation, not completion.

Deciding words: “An explicit stop means no further writes; report the known state of any issued operations.” The inherited ownership rule cannot override the user's stop.

## S — ship + verify

Proposed next action: report the pending required check as a blocker and return control now. The passing independent verdict does not satisfy the separate required-check gate. **Not ready to land**; nothing merges. Do not watch, arm automatic merging or wait through an ongoing delivery workflow: the request explicitly requires blocker reporting otherwise.

Deciding words: ship requires “Required checks and safety evidence must pass” and “Stop at the first gap”; verify requires a verdict that “passes all required checks.” Conditional merge authority does not cover a pending check.

## T — babysit + verify

Proposed next action: report PR 12's failing check and unmerged dependency as PR 13's readiness blocker. PR 12 belongs to another owner and lies outside the authorized scope. Make no changes to it; hand back and end any existing watch. **PR 13 is not ready**; its other gates are unspecified, not passes.

Deciding words: “Work the lowest unmerged dependency only if authorized within the requested scope. Otherwise report it as a blocker.”

## Loaded skill SHA-256

- babysit: `503a6f87356d476fef07bb4fe9f83c9fe23d16076e72762c23eaf8c6398531cf`
- verify: `ff1f34981601479e0dd930cdf450d550f5530984c35e5620ad3301ac9a43285a`
- build: `985e9397ba5b2de1c932ae1d2d468196dc14aa1f399e649d67e8beda52d5c74b`
- ship: `2ac09859365337eafc25e64335401bf93f803cf2d15cb018d6dbc234ba6c7b7c`

## Context limits

Inherited global/project rules remain loaded and may mask text differences; this run cannot isolate skill effects. Required README/DISTILL reading exposed historical run summaries in DISTILL, contrary to the requested isolation; those summaries were not used for these decisions. No delivery-checks, cookbook, reviews or separate run reports were opened. No live host state, reviewer or behavioral checks were exercised; fixture facts are assumed. This report makes no self-grade or expected-failure claim.
