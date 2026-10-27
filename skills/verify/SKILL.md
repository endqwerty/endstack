---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

A change needs evidence from someone who did not write it.

## Author

1. Before editing, write checks on the real surface: command, page, API,
   stored value. A bug gets a failing check first.
2. Run them on the real artifact; keep the deciding lines. Passing tests
   alone do not prove behaviour.
3. Ask for a read-only verifier from a different provider, never another
   session of your own. Without one, report unverified; do not deliver.
4. Give it the task, checks and exact revision range, not your conclusions.
   A re-review covers what changed since the last verdict and what it can
   affect, with earlier findings, never why you dismiss them.
5. Fix each reachable finding with a check that catches it again; rerun
   affected checks; answer others with a reason. A verdict covers a patch:
   [carry-forward](references/carry-forward.md) says when it, or a result,
   still stands on a new revision; otherwise get a fresh one. Deliver only
   on an independent pass of every required check and the safety fact on the
   current revision, with no open blocker. Report non-blocking limits.
   A review limit is not approval.

## Verifier

- Run every check yourself.
- Name the fact the change's safety rests on; prove it by running the real
  code, or mark it unproven.
- Try to break it: other inputs, failure paths, what else uses the
  changed code, what the diff omits. A defect already in the base
  is the base's, unless the change copies it or newly reaches it.
- An issue names what reaches it in this revision: input, a caller, stored
  or imported data, a race, a setting it accepts. What only later code makes
  is a note.
- A check fails: suspect your method; reproduce it.
- Answer each check: **pass**, **issues** or **not checked**, with what you
  ran and the deciding lines. A check you could not run is never a pass.
- Name the revision and patch you judged.
- Change nothing.

## Never

- Pass on a summary. Read the diff yourself, a subagent's included.
