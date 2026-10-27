# Evidence for tstack-evaluation.md

- `mainworthy.jsonl`, `others.jsonl`: one record per review round, with each
  finding's class (bug, risk, nit, false positive). `others.jsonl` leaves out
  everduet, which is not Daniel's repository; its counts are in
  `others-summary.md`.
- `*-escapes.jsonl`: defects a later pull request fixed, with what would have
  caught them.
- `*-summary.md`: each mining agent's report.
- `replay/`: briefs, the `verify` texts and each verifier's report.
  `skill-a-SKILL.md` is `main`'s; `skill-b-SKILL.md` is the draft the #983
  run 2 replay used (the earlier b runs used a version before its last two
  edits); `skill-final-SKILL.md` is the branch's text after the independent
  review.
- `tables.py`: recomputes the round tables from the records.
- `dry-run/`: the babysit and ship scenario and the two answers ("x" current
  skills, "y" this branch).
