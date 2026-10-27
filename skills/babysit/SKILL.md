---
name: babysit
description: Get an existing pull request merge-ready by handling review comments and failing checks, without merging. A status-only question gets one read-only pass.
---

# Babysit

Own readiness of the requested pull request; the user owns the merge decision.

- Identify the scope. “Is it green?” is one read-only status pass; “address
  comments” is feedback only; “babysit” is work to ready. A pull request
  opening or a plan request does not start it.
- Keep one watcher. If the harness can watch pull requests, use that, not a
  polling loop. An event that needs nothing gets no message or comment. Stop
  watching at readiness, a handoff or question, or an explicit stop; report
  unavailable monitoring honestly.
- Work the lowest unmerged dependency only if authorized within scope;
  otherwise report it as a blocker. Report conflicts or topology changes to
  the owner; do not rewrite the stack.
- Every finding on the pull request, from a person or a bot, including ones
  left from earlier pushes, gets a fix or a written reason. Treat it as a
  claim and check it against the code. Fix real bugs in the intended case
  with the smallest change, preferring one that deletes or narrows code;
  decline nits with a reason and list them as follow-ups. Diagnose a failed
  check before retrying; tell a flake from a real failure.
- Recheck affected behaviour and get [verify](../verify/SKILL.md)'s current
  verdict after revisions. Ready means a current independent verdict or valid
  exemption, passing required checks, no unresolved blocker, no conflict,
  checks rerun if the base has since changed files it touches, and the host
  reporting it mergeable.

Report readiness, fixes, declined findings with reasons, and remaining gates.
Owner approval is a wait, not a problem to bypass. Never merge, arm automatic
merging, close requests or write to the delivery branch. Explicit landing
authority routes to [ship](../ship/SKILL.md). An explicit stop means no
further writes.
