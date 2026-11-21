---
name: babysit
description: Get an existing pull request merge-ready by handling review comments and failing checks, without merging. A status-only question gets one read-only pass.
---

# Babysit

Own readiness of the requested pull request; the user owns the merge decision.

- Identify the scope. “Is it green?” is one read-only status pass; “address
  comments” is feedback only; “babysit” is work to ready.
- Keep one watcher. If the harness can watch pull requests, use that;
  otherwise [pr-watch](../pr-watch/SKILL.md), never a polling loop. Stop
  watching at readiness, a handoff or question, or an explicit stop.
- Work an unmerged dependency only if authorized; otherwise report it as a
  blocker, and do not rewrite the stack.
- Every finding on the pull request, from a person or a bot, including ones
  left from earlier pushes, gets a fix or a written reason. Treat it as a
  claim and check it against the code. Fix real bugs in the intended case
  with the smallest change; decline nits with a reason. Diagnose a failed
  check before retrying; tell a flake from a real failure.
- Recheck affected behaviour and get [verify](../verify/SKILL.md)'s current
  verdict after revisions; rerun checks when the base has since changed files
  the pull request touches. Ready means a current independent verdict or valid
  exemption, passing required checks, no unresolved blocker, no conflict, and
  the host reporting it mergeable.

Report readiness, fixes, declined findings with reasons, and remaining gates.
Never merge, arm automatic merging, close the pull request or write to the
delivery branch; landing is [ship](../ship/SKILL.md)'s. Owner approval is a
wait, not a gate to bypass. An explicit stop means no further writes.
