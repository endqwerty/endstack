---
name: autopilot-full
description: Deliver a bounded work queue end to end, merges included, only with explicit authority for that queue. Not a plan, a budget or a general keep-going request.
---

# Full autopilot

Own delivery inside an explicit boundary, not an unlimited backlog.

- Establish the queue, dependencies, completion checks, merge authority and
  operator-held items before execution. The user must authorize both the work
  and its landing; a skill name, “autopilot” or “keep going” alone is insufficient.
  Without landing authority, offer [autopilot-stack](../autopilot-stack/SKILL.md)
  rather than silently assuming permission. Plan/help requests do not execute.
- Compose [build](../build/SKILL.md), [babysit](../babysit/SKILL.md) and
  [ship](../ship/SKILL.md). Their boundaries and [verify](../verify/SKILL.md)'s
  independent current-revision gate still apply to each item; autonomy removes
  repetitive prompting, never evidence or approval requirements.
- Give each participant a bounded change and ownership. The coordinator owns
  dependency order and delivery. Land only the authorized verified frontier;
  do not skip blocked prerequisites or delegate away an operator-held decision.
- Track progress by artifacts and current checks, not reassuring status text.
  Keep independent authorized work moving when one item is blocked. Stop at
  queue completion, an authority boundary, or an explicit stop. On stop, place
  all participants on a no-writes hold and report issued operations' known state.
- Report each landed revision and destination, remaining requests and gates,
  evidence and limits. Release only project-prescribed local artifacts.

Merge authority is not permission to deploy, delete data, override protections
or perform unrelated irreversible actions. Never expand the authorized queue
merely to consume spare capacity.
