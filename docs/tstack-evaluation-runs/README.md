# Evidence for tstack-evaluation.md

- `mainworthy.jsonl`, `others.jsonl`: one record per review round, with each
  finding's class (bug, risk, nit, false positive). `others.jsonl` leaves out
  everduet, which is not Daniel's repository; its counts are in
  `others-summary.md`.
- `*-escapes.jsonl`: defects a later pull request fixed, with what would have
  caught them.
- `*-summary.md`: each mining agent's report.
- `replay/`: briefs, the two `verify` texts ("a" is `main`'s, "b" this
  branch's final text) and each verifier's report.
- `dry-run/`: the babysit and ship scenario and the two answers ("x" current
  skills, "y" this branch).
