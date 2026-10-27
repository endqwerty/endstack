---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

## Author

1. Before editing, write checks on the real surface: command, page, API,
   stored value. A bug gets a failing check first.
2. Run them on the real artifact; keep deciding lines. Green tests
   alone prove no behaviour.
3. Ask a read-only verifier from another provider. Without one, report
   unverified.
4. Give it the task, checks and revision range, not your conclusions;
   for a re-review, the change since the last verdict, what it affects
   and open findings.
5. Re-rank findings. Fix blockers and shoulds with a check that
   catches them again; rerun affected checks. Fix a nit only if small;
   declining one starts no round, and
   [carry-forward](references/carry-forward.md) says what a fix needs.
   Deliver only on an independent pass of every required check and the
   safety fact on the current revision, no blocker or should open.
6. Still open after two rounds: stop and rethink. Would another
   approach or smaller change avoid what findings share? Then at
   most two more; still open, stop delivery, report both sides.

## Verifier

- Run every check yourself; reproduce a failure, suspecting your
  method first. Answer each pass, issues or not checked, with deciding
  lines; an unrun check is not checked.
- Name the fact its safety rests on; prove it on the real code or mark
  it unproven.
- Try to break it: other inputs, failure paths, callers, what the diff
  omits. A base defect is the base's unless the change copies or newly
  reaches it.
- Name what reaches each issue and rank it. Blocker: the intended case
  is wrong. Should: ordinary use, a caller, stored or imported data, a
  race or a setting reaches it. Nit: contrived input giving only a wrong
  result or warning, wording, extra tests or guards, small costs, what
  only later code makes. Data loss, security or a trust boundary is never
  a nit.
- Read the whole diff yourself, a subagent's included, never a summary.
  Name the revision and patch you judged. Change nothing.
