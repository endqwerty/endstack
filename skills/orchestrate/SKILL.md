---
name: orchestrate
description: Run a multi-day program of many pull requests through delegated owners and verifiers from one standing coordinator thread. Use only when orchestrate is named.
disable-model-invocation: true
---

# Orchestrate

You run the program, never the code: assign work and check its results. One
coordinator thread owns a multi-day program of many, often stacked, pull
requests. Unavailable delegation is a blocker.

Use the harness's delegation. Keep the state needed to resume (goals,
ownership, PR links, verdicts, blockers) in a durable notes file in the repo
or tracker, and the decision trail through
[show-me-your-work](../show-me-your-work/SKILL.md). On pickup, read those
records and reconcile live work before launching replacements. Use event
subscriptions or watchers if the harness has them; do not build orchestration
scripts, poll, relay status between agents, or message workers to check on
them.

## Authority and delivery

Invoking orchestrate grants landing authority for the program, like
[autopilot-full](../autopilot-full/SKILL.md). Fully drive every PR through
build, verification, readiness and landing to the program's goal. Nothing
waits for the user's approval to merge. The owner lands only with a passing
independent verdict on the current head, required checks and honored holds,
through [ship](../ship/SKILL.md)'s gates. Resolve failed gates by re-delegating,
not asking for approval.

Before the first unit, anticipate product, preference, irreversible-step,
scope or risk decisions that could later hold a merge. Ask all known questions
early in one message, with stated defaults. Proceed on those defaults for
unanswered questions within existing authority. Defaults never grant excluded
permissions or override holds. Mid-program ask only for a genuinely new such
decision, never whether to merge or keep going.

Explicit "don't merge" or "I'll land it" instructions stop owners at
merge-ready. Authority excludes deployment, destructive operations and work
outside the program.

Owners compose [build](../build/SKILL.md), [babysit](../babysit/SKILL.md) for
readiness, and [verify](../verify/SKILL.md) for independent current-revision
evidence.

## Topology

- One owner per PR, the only writer of its branch, carries it from build to
  the authorized endpoint; conflicts, chain rebases and fixes go to it.
  Closing or retargeting a base can orphan children and needs your call.
- A fresh worker for each independent task. Its kickoff is self-contained,
  including each upstream report it depends on in full. Workers cannot see
  siblings. Choose an execution environment with the required code, runtime
  and access; work needing local transcripts, a simulator or local-only
  authentication stays where those exist.
- Add a sub-coordinator only for an area with many parallel workers. It owns
  their kickoffs and sends one rollup, never raw reports. Stop at three levels:
  you, sub-coordinators, workers. Keep about ten workers in flight per
  coordinator, subject to capacity; refill as each finishes. Both limits are
  untested; revisit them before 1.0.
- When new work needs a worker's built state, use the harness's state-preserving
  delegation if available, otherwise explicitly hand off the required state.
- Each PR gets a fresh read-only verifier who is not its author. Green checks
  alone never authorize landing.
- Start with one unit through kickoff, owner, verifier and merge (or
  merge-ready when the user reserves landing) before fan-out, so a bad kickoff
  fails once.

## Supervision

- Each kickoff names the goal, allowed and forbidden paths, branch ownership,
  forbidden actions, dependencies, standing orders, landing authority and the
  evidence proving completion. Without that evidence the unit is not scoped.
- Read the diff or artifact, not only the summary. Sample sub-coordinator
  kickoffs while work runs and fix instructions when needed.
- Send back work that drifts or grows beyond the request. Keep fixes that
  block the program and park the rest as follow-ups.
- Check every PR's live state before reporting it. Account for each worker
  as done, replaced or absorbed into another worker's scope.
- Stop or replace stalled or looping workers. Judge artifacts and PR activity,
  not status prose. Retry by cause: smaller scope after a context or memory
  limit, the same kickoff after a dropped connection, a different suitable
  model after a tool error. After two retries drop the unit and replan.
  Reconcile late results against the current PR state and give unique
  findings to a fresh worker.
- Rebase mechanics, retries, flaky checks and review triage stay with owners.
  Replan dead ends and keep independent work moving.

## Reply

Report what landed against the goal (not merely merge-ready), each PR's live
state and verdict, what was dropped and why, and decisions waiting on the user.
