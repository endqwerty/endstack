---
name: ship
description: Land pull requests when the user invokes ship or asks to merge, land or ship them; invoking it is the go-ahead. Not for building, fixing checks, status, planning or keep-going.
---

# Ship

Own only the landing the user authorized.

1. The user invoking this skill by name, or asking to merge, land or ship, is
   the merge authority: land without asking whether to. Take the work they
   name; with none named, the work this conversation built or the current
   branch's open pull request. Ask only if no target or several fit. Your own
   choice of this skill, ownership or a budget never counts. Honor holds,
   later stops and operator-reserved gates.
2. Land only with [verify](../verify/SKILL.md)'s passing verdict or a
   documented exemption on the current revision, required checks passing,
   every finding, a bot's included, fixed or answered, and the host reporting
   it mergeable. Otherwise report the gap; do not ask for approval.
3. Land only the contiguous authorized, verified run from the lowest unmerged
   dependency, one request at a time, using the project's delivery mechanism.
   Do not merge a child into an unlanded parent or arm descendants.
4. Confirm each landed result in the intended destination, not merely that a
   merge was requested. If the remote outcome is unknown, inspect it before
   retrying. Stop at the first gap.

Do not arm automatic merging. Merge permission does not authorize deployment,
destructive operations or unrelated work.
