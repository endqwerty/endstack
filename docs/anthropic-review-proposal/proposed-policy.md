---
name: verify
description: Independent check before a behaviour, data, auth, money or deployment change is merged or called done, or of someone else's. Not for edits that change none of these.
---

# Verify

Both roles read the full diff and [rubric](references/review-rubric.md).

## Author

1. Before editing, write checks on the real surface: command, page, API,
   stored value. A bug gets a failing check first.
2. Run the checks first on the real artifact; keep deciding lines.
   Green tests alone do not prove the contract.
3. Ask one read-only verifier from another provider in fresh context.
   Without one, report unverified.
4. Give it the task, checks and revision range, not your conclusions;
   for a re-review, the change since the last verdict, what it affects
   and open findings.
5. Re-rank findings. Fix blockers and shoulds with the cheapest check
   catching them again; rerun affected checks. Decline nits without edits or another round.
   [Carry-forward](references/carry-forward.md) governs fixes.
   Deliver only on an independent pass of every required check and the
   safety fact on this revision, no blocker or should open.
6. Still open after two rounds: stop and rethink the approach or scope.
   Then at most two more; still open, stop delivery, report both sides.

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
- Name the revision and patch you judged. Change nothing.
