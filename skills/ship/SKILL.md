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
2. Require [verify](../verify/SKILL.md)'s independent passing verdict on the
   current revision, or a documented exemption under its review scope. Required checks
   and safety evidence must pass; unresolved blockers or unavailable review
   stop landing: report them, do not ask for approval. Every finding, a bot's
   included, has a fix or a written reason. Confirm host mergeability and
   dependency readiness.
3. Land only the contiguous authorized, verified run from the lowest unmerged
   dependency, one request at a time, using the project's delivery mechanism.
   Do not merge a child into an unlanded parent or arm descendants. Changed
   revisions or bases require fresh checks and a current passing verdict or
   documented exemption under verify, including its carry-forward rules.
4. Confirm each landed result in the intended destination, not merely that a
   merge was requested. Reinspect the next request after each landing. If the
   remote outcome is unknown, inspect it before retrying. Stop at the first gap.
5. Report what actually landed, its revision and destination, remaining work
   and limits. Preserve unlanded branches and perform prescribed local cleanup.

Do not arm automatic merging without explicit merge-when-ready authority and
gates that preserve the verified revision. Merge permission does not authorize
deployment, destructive operations or unrelated work. Planning and help questions
explain this process without executing it; a stop instruction prevents writes.
