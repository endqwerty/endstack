---
name: verify
description: Get an independent check before a change is merged or called done. Use for a feature, bug fix, or anything touching auth, data, money, credentials or deployment, and when asked to verify, double-check, sign off on or break someone else's change. Not for docs, comments, or mechanical edits that change no behaviour, data or contract.
---

# Verify

A change needs evidence from someone who did not write it.

## Author

1. Before editing, write checks on the real surface: command, page, API or
   stored value. A bug gets a failing check first.
2. Run them on the real artifact; keep the deciding lines. Compiling and
   passing tests alone do not prove behaviour.
3. Ask for a read-only verifier from a different provider, never another
   session of your own. Without one, report unverified; do not merge or call
   the change done.
4. Give it the task, checks and exact revision range, not your conclusions.
5. Fix real findings; answer the rest with a concrete reason. Rerun affected
   checks after material fixes. Any revision change needs a fresh verdict.
   Deliver only when an independent verdict passes all required checks and
   the safety fact on the current revision, with no unresolved blockers.
   Report non-blocking limits. A review limit is not approval: if review
   cannot run, stop unverified.

## Verifier

- Run every check yourself. Do not accept the author's output.
- Name the fact the change's safety rests on; prove it by running the real
  code, or mark it unproven.
- Then try to break it: other inputs, failure paths, what else uses the
  changed code, what the diff does not show.
- Suspect your method before the system when a check fails. Reproduce it.
- Answer each check: **pass**, **issues**, or **not checked**, with what you
  ran and the deciding lines. A check you could not run is never a pass.
- Name the revision you judged. A verdict on an older revision is stale.
- Change nothing.

## Never

- Verify your own work and call it independent.
- Pass on a summary. Read the diff yourself, a subagent's included.
