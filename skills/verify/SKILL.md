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
3. Ask a read-only verifier from another provider. Without one, report
   unverified.
4. Give it the task, checks and revision range, not your conclusions.
   A re-review covers the change since the last verdict and what it
   affects, with open findings, not rebuttals.
5. Re-rank findings. Fix blockers and shoulds with a check that
   catches them again; rerun affected checks. Fix a nit only if small;
   declining one or a prose fix starts no round; for other revisions see
   [carry-forward](references/carry-forward.md). Deliver only on an
   independent pass of every required check and the safety fact on the
   current revision, no blocker or should open. After three rounds an
   open one stops delivery; report both sides.

## Verifier

- Run every check yourself; if one fails, suspect your method;
  reproduce it. Answer each pass, issues or not checked, with deciding
  lines. An unrun check is not checked, never a pass or an issue.
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
- Name the revision and patch you judged. Change nothing.

## Never

- Pass on a summary: read the diff yourself, a subagent's included.
