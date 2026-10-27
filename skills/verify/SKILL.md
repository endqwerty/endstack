---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

A change needs evidence from someone who did not write it.

## Author

1. Before editing, write checks on the real surface: command, page, API,
   stored value. A bug gets a failing check first.
2. Run them on the real artifact; keep deciding lines. Green tests
   alone prove no behaviour.
3. Ask a read-only verifier from another provider, never a session of
   your own. Without one, report unverified.
4. Give it the task, checks and revision range, not your conclusions.
   A re-review covers the change since the last verdict and what it
   affects, with open findings, not rebuttals.
5. Re-rank findings. Fix blockers and shoulds with a check that
   catches them again; rerun affected checks. Fix a nit only if small and
   behaviour-free; nits start no round.
   [Carry-forward](references/carry-forward.md) says when a verdict carries to
   a new revision. Deliver only on an independent pass of every
   required check and the safety fact on the current revision, no blocker
   or should open. After three rounds an open one stops delivery; report
   both sides.

## Verifier

- Run every check yourself.
- Name the fact its safety rests on; prove it by running the real
  code, or mark it unproven.
- Try to break it: other inputs, failure paths, callers of
  changed code, what the diff omits. A defect already in the base
  is the base's unless the change copies or newly reaches it.
- Rank each issue: blocker, the intended case is wrong; should,
  input, a caller, stored or imported data, a race or a setting reaches it
  now; nit, the rest (rare paths, wording, extra tests or guards,
  small costs). What only later code makes is a note.
- A check fails: suspect your method; reproduce it.
- Answer each check: pass, issues or not checked, with the
  deciding lines. One you could not run is not checked, never a pass or an issue.
- Name the revision and patch you judged. Change nothing.

## Never

- Pass on a summary: read the diff yourself, a subagent's included.
