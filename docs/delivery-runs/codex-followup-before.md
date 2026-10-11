# Codex follow-up decision simulation: prior text

Skill revision: `8a6fee3`. Read with `git show 8a6fee3:skills/<name>/SKILL.md`: Q uses babysit and verify; R uses build; S uses ship and verify. Inputs: `docs/delivery-follow-up-fixtures.json` and inherited global/project rules.

## Q — Babysit payment PR; owner merges

Workflow: babysit, with verify's independent-review gate. Proposed next action: report missing independent review and unavailable reviewer; hand readiness back to the owner as blocked/unverified. The cleared transient failure needs no speculative revision. Passing required checks, no comments and host mergeability do not supply the missing verdict.

Readiness: **unverified, not merge-ready**. Deciding words: verify requires an independent check “before a change is merged or called done”; “Without one, report unverified; do not merge or call the change done” and “if review cannot run, stop unverified.” Babysit's “obtain … current verdict after revisions” does not exempt an unchanged payment revision from verify or the inherited money-review rule.

Stopping point: report the review blocker and end at handoff; stop any existing monitoring. Never merge or arm automatic merging. No watcher is started in this simulation.

## R — Stop unpublished build

Workflow: interrupted build. Proposed next action: immediately cease implementation, checking, PR preparation and publication; report that the work remains unpublished and preserve existing local work. No external write is in flight to reconcile.

Readiness: **stopped; readiness not established**. Deciding words: the user's “Stop working on the change now” overrides build's “Own the change through a reviewable pull request” and inherited end-to-end ownership. Build contains no explicit stop clause in this revision; the current user instruction still controls.

Stopping point: acknowledge the stop without further case writes, commits, PR creation or watcher activity.

## S — Conditional immediate merge

Workflow: ship with verify. Proposed next action: report the pending required check as a blocker; perform no landing or continued waiting.

Readiness: **not ready to land**, despite the passing independent verdict. Deciding words: ship says “Required checks and safety evidence must pass” and “Stop at the first gap”; the request requires checks to “already pass” and says “Otherwise report the blockers; do not watch or arm automatic merging.”

Stopping point: return the blocker report immediately. No merge, watcher or automatic merging.

## Context limits

Decision simulation only: no live checks or case operations. No working-tree skill texts, delivery-checks, cookbook or reviews were read. Required README/DISTILL reads exposed historical run summaries; those are excluded from decision evidence. No other run artifacts were opened. Inherited review and stop policies can mask differences in skill wording; these decisions do not establish comparative improvement.
