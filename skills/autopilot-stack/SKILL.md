---
name: autopilot-stack
description: Build and verify a bounded queue of dependent changes into a pull-request stack for the user to land. Not full automatic delivery or a plan alone.
---

# Autopilot stack

Own the stack, never its landing.

- Establish the bounded queue, dependencies, observable completion checks and
  operator-held decisions. A request to describe the plan is not permission to
  execute it. Do not expand the queue just because capacity remains.
- Compose [build](../build/SKILL.md), [babysit](../babysit/SKILL.md) and
  [verify](../verify/SKILL.md) for each change. Before any code or brief for a
  change, read build's [design step](../build/references/design.md) and do it.
  Delegate disjoint implementation ownership, with its note, when useful.
  Topology has one writer, the coordinator: builders push only their own
  branches, start a dependent item from its parent's branch, and never
  rebase or retarget.
- Produce one reviewable linear chain, bottom-up, with only its root targeting
  the delivery branch. Record each request's parent and exact reviewed revision.
  Do not collapse review boundaries to make the stack look green.
- Keep dependent work blocked behind missing prerequisites. If a revision or
  base moves, refresh affected checks and independent verdicts (verify says
  when one carries forward) before declaring the chain ready. A successful child does not make an unverified parent safe.
- Hand the user the ordered request links, dependency map, evidence and current
  verdicts, unresolved gates and next action. Preserve the branches and release
  only project-prescribed local artifacts. Stop watchers at handoff.

No participant merges, arms automatic merging, closes requests or writes
directly to the delivery branch. The operator lands the chain; changing to
automatic delivery requires a new explicit grant for identified work, not
“keep going”. A stop instruction puts all participants on a no-writes hold.
