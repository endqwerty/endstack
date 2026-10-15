---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

A change needs evidence from someone who did not write it.

## Author

1. Before editing, write checks on the real surface: command, page, API or
   stored value. A bug gets a failing check first.
2. Run them on the real artifact; keep the deciding lines. Compiling and
   passing tests alone do not prove behaviour.
3. Ask for a read-only verifier from a different provider, never another
   session of your own. Without one, report unverified and do not deliver.
4. Give it the task, checks and exact revision range, not your conclusions.
   A re-review covers what changed since the last verdict and what that can
   affect, with the earlier findings, never your reasons for dismissing them.
5. Fix real findings and rerun affected checks; answer others with a
   reason. A new revision needs a fresh verdict, unless it only rebased the
   change unchanged onto a base touching nothing it uses, or only edited
   prose no tool or agent reads as instructions: then record that evidence
   and rerun the required checks; the verdict carries forward. Deliver only
   on an independent pass of all required checks and the safety fact on the
   current revision, with no unresolved blockers. Report non-blocking limits.
   A review limit is not approval: if review cannot run, stop unverified.

## Verifier

- Run every check yourself. Do not accept the author's output.
- Name the fact the change's safety rests on; prove it by running the real
  code, or mark it unproven.
- Then try to break it: other inputs, failure paths, what else uses the
  changed code, what the diff does not show.
- When a check fails, suspect your method first and reproduce it.
- Answer each check: **pass**, **issues**, or **not checked**, with what you
  ran and the deciding lines. A check you could not run is never a pass.
- Name the revision you judged. An older verdict is stale unless step 5
  carries it.
- Change nothing.

## Never

- Pass on a summary. Read the diff yourself, a subagent's included.
