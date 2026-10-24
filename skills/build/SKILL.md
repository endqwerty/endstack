---
name: build
description: Implement a feature or fix and prepare a checked pull request for review. Use to build, implement or fix, not to explain or plan. Stops before watching or merging.
---

# Build

Own the change through a reviewable pull request, not through landing.

- Establish the requested outcome, observable checks and scope before editing.
  Reproduce a bug first. Resolve engineering questions from evidence; leave
  product decisions that change the request to the user.
- Before the first edit to production code, read
  [references/design.md](references/design.md) and do its steps; keep its
  note. A delegated builder gets the note and reads the principles index and
  that file before coding. Report each principle that changed a choice.
- Implement the smallest complete change. Run the checks on the real artifact
  and keep their deciding output. Read the whole diff, including delegated work.
- Use [verify](../verify/SKILL.md) for independent review and exemptions.
  Missing evidence or review means unverified, never ready or done.
- A correction goes through [correct](../correct/SKILL.md): a recurring
  defect gets a guard, a preference a note.
- Prepare a non-draft pull request that opens with each choice made for the
  user and how to reverse it, then a standalone brief: why, what changed,
  where to start reading, why this approach, checks and deciding evidence,
  reviewer and exact revision, findings and remaining limits. Follow the
  project's template. Do not bury required context in the conversation.
- Report the pull request, current revision, readiness and anything still
  needed. Preserve its branch; release only project-prescribed local artifacts.

Opening a pull request does not start babysitting. Do not merge, arm automatic
merging, close the request or write directly to the delivery branch. Ownership,
“keep going” and a budget request do not grant landing authority. A later
explicit request to land identified work belongs to [ship](../ship/SKILL.md).
A plan or help request explains the workflow without executing it. An explicit
stop means no further writes; report the known state of any issued operations.
