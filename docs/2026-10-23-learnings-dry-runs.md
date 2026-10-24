# Dry runs: classified corrections, dissent and swarm routing (2026-10-23)

Each scenario ran twice on GPT 6.1 Sol (medium effort), once with the skills at
`origin/main` `668f653` and once with this branch at `3b76d4a`, each run seeing
only its own copy and not told which. The scenarios come from Mainworthy's
history. Full outputs were kept outside the repository; the deciding lines are
quoted here. Round 2 of review (`757f496`) then tightened `correct`'s "One
rule", `build`'s guard line and arena's stopping rule; S1, S2 and S3 already
behaved as those edits intend, so they were not rerun.

| Scenario | Before (`668f653`) | After (`3b76d4a`) |
| --- | --- | --- |
| S1. The owner writes "drop old ios support, maybe only current, next and 1 previous? I'm not sure if 1 previous is even needed". | An AGENTS.md rule plus a CI check that "fails when a shipping native target ... lowers its effective minimum", proven to fail first. | A row quoting the owner exactly, labelled "Provisional agent choice", enforced by "Agent judgment ... No automated enforcement added for this tentative preference." |
| S2. Tool descriptions should be "lean"; two reviews flagged growth; the list measures 3,950 tokens. | A CI comparison that warns on "an increase of 1 token relative to the merge base". | "No test, parser, blocking check, or numeric budget"; one preference row, "Reviewer judgment when descriptions change. No automated length limit." |
| S3. Three arena runners and the judge converge on wiping and reseeding the demo on every server start behind the write lock (the design behind a 17-minute outage). | "Apply arena's explicit convergence rule ... Keep the consensus shape ... Do not ... launch another candidate round simply because the outcome is unanimous." | "Do not ship the consensus yet." One dissenter, briefed to examine "the actual scope of the lock, other writers ... whether startup is the right trigger." |
| S4. A one-word typo fix, then a review of two weeks of agent use (commits, transcripts, decisions, issues). | Typo: zero workers. Review: four investigators, reached through `why` and `swarm`. | Typo: "no useful independent parts. Stay serial, with zero workers. Do not open swarm." Review: four investigators, from the routing's swarm decision. |

S4 shows little change: the old routing already reached a fan-out for the large
review. The new line makes the decision explicit on every task, small ones
included, at the cost of one sentence per task.
