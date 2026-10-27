---
name: ship
description: Land identified pull requests only when explicitly asked to merge, land or ship them. Not for building, fixing checks, status, planning or a general keep-going request.
---

# Ship

Own only the landing the user authorized.

1. Identify the exact work and destination, and the instruction granting merge
   authority. An explicit “ship this pull request”, or “autopilot” or “full
   send” on it, counts; selecting this skill, ownership or a budget request
   alone does not. Honor holds, later stops and operator-reserved gates. If
   the scope is unclear, do not land anything.
2. Require [verify](../verify/SKILL.md)'s independent passing verdict on the
   current revision, or its applicable nonbehavioral exemption. Required checks
   and safety evidence must pass; unresolved blockers or unavailable review
   stop landing. Every finding on it, a bot's included, has a fix or a
   written reason. Confirm current host mergeability and dependency readiness.
3. Land only the contiguous authorized, verified run from the lowest unmerged
   dependency, one request at a time, using the project's delivery mechanism.
   Do not merge a child into an unlanded parent or arm descendants. Changed
   revisions or bases require fresh checks and a current independent verdict
   (verify says when an earlier one carries forward).
4. Confirm each landed result in the intended destination, not merely that a
   merge was requested. Reinspect the next request after each landing. If the
   remote outcome is unknown, inspect it before retrying. Stop at the first gap.
5. Report what actually landed, its revision and destination, remaining work
   and limits. Preserve unlanded branches and perform prescribed local cleanup.

Do not arm automatic merging without explicit merge-when-ready authority and
gates that preserve the verified revision. Merge permission does not authorize
deployment, destructive operations or unrelated work. Planning and help requests
explain this process without executing it; a stop instruction prevents writes.
