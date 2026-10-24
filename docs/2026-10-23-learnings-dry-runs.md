# Dry runs: classified corrections, dissent and swarm routing (2026-10-23)

Each scenario ran twice on GPT 6.1 Sol (medium effort), once with the skills at
`origin/main` `668f653` and once with this branch at `3b76d4a`, each run seeing
only its own copy and not told which. The scenarios come from Mainworthy's
history. Full outputs were kept outside the repository; the deciding lines are
quoted here. Review then tightened `correct`'s "One rule" and `build`'s guard line
(`757f496`), which S1 and S2 already followed, and arena's stopping and
base-switch rules (`757f496`, `ebb2e33`). S3 shows the single dissenter and a
criterion-by-criterion comparison; its later rules (reframe only for a
requirement the rubric missed, at most once; switch base only on the full
rubric) were not exercised by a new run. All outputs are proposed actions; no
check, dissenter or arena was actually run.

| Scenario | Before (`668f653`) | After (`3b76d4a`) |
| --- | --- | --- |
| S1. The owner writes "drop old ios support, maybe only current, next and 1 previous? I'm not sure if 1 previous is even needed". | An AGENTS.md rule plus a proposed CI check that "fails when a shipping native target ... lowers its effective minimum", to be shown failing before it lands. | A row quoting the owner exactly, labelled "Provisional agent choice", enforced by "Agent judgment ... No automated enforcement added for this tentative preference." |
| S2. Tool descriptions should be "lean"; two reviews flagged growth; the list measures 3,950 tokens. | A CI comparison that warns on "an increase of 1 token relative to the merge base". | "No test, parser, blocking check, or numeric budget"; one preference row, "Reviewer judgment when descriptions change. No automated length limit." |
| S3. Three arena runners and the judge converge on wiping and reseeding the demo on every server start behind the write lock (the design behind a 17-minute outage). | "Apply arena's explicit convergence rule ... Keep the consensus shape ... Do not ... launch another candidate round simply because the outcome is unanimous." | "Do not ship the consensus yet." One dissenter, briefed to examine "the actual scope of the lock, other writers ... whether startup is the right trigger." |
| S4. A one-word typo fix, then a review of two weeks of agent use (commits, transcripts, decisions, issues). | Typo: zero workers. Review: four investigators, reached through `why` and `swarm`. | Typo: "no useful independent parts. Stay serial, with zero workers. Do not open swarm." Review: four investigators, from the routing's swarm decision. |

S4 shows little change: the old routing already reached a fan-out for the large
review. The new line makes the decision explicit on every task, small ones
included, at the cost of one sentence per task.
