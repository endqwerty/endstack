---
name: autopilot-full
description: Deliver a change or bounded work queue end to end, merges included, when the user says autopilot or full send for it. Not a plan, a budget, a keep-going request or a stack the user lands.
---

# Full autopilot

Own delivery inside an explicit boundary, not an unlimited backlog.

- Establish the queue, dependencies, completion checks and operator-held
  items before execution. “Autopilot” or “full send” on named work authorizes
  both the work and its landing, and nothing then waits for the user's
  approval; “keep going” or a budget does neither. If the work is unclear,
  land nothing. Plan/help requests do not execute.
- Compose [build](../build/SKILL.md), [babysit](../babysit/SKILL.md) and
  [ship](../ship/SKILL.md). Their boundaries and [verify](../verify/SKILL.md)'s
  independent current-revision gate still apply to each item; autonomy removes
  prompts and the user's approval, never evidence or the host's protections.
- Before any code or brief for an item, read build's
  [design step](../build/references/design.md) and do it. Give each
  participant a bounded change, ownership and that note. The coordinator owns
  dependency order and delivery. Land only the authorized verified frontier;
  do not skip blocked prerequisites or delegate away an operator-held decision.
- Keep a [show-me-your-work](../show-me-your-work/SKILL.md) decision log.
  Track progress by artifacts and current checks, not reassuring status text.
  Keep independent authorized work moving when one item is blocked. Stop at
  queue completion, an authority boundary, or an explicit stop. On stop, place
  all participants on a no-writes hold and report issued operations' known state.
- Report each landed revision and destination, remaining requests and gates,
  evidence and limits. Release only project-prescribed local artifacts.

Merge authority is not permission to deploy, delete data, override protections
or perform unrelated irreversible actions. Never expand the authorized queue
merely to consume spare capacity.
