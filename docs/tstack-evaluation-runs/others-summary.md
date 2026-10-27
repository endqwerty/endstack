# How much the independent review loop catches, round by round

Sample: 108 merged PRs (agent-factory 25, endstack 21, crosspoint-reader last 20, codex-reset-watch 17, everduet last 25).
Source: PR descriptions, PR comments, inline review comments; for agent-factory also the `.audit/*review*.md` files the descriptions cite.
Raw data: `others.jsonl` (186 lines, one per review pass), `others-escapes.jsonl` (17), full per-repo tables in `analysis-tables.txt`.
"Round" means an independent verify round on a revision (the `verify` loop). Review-bot passes, audits, design panels and same-family reviews are counted separately.

## Answer

The claim holds from round 3 on and is half true for round 2.

- Round 1 does most of the work: 41 bugs, 53 risks, 37 nits, 7 false positives across 67 PRs.
- Round 2 (35 rounds): 7 bugs in 6 PRs, 14 risks, 19 nits; 18 of the 35 rounds found nothing. Nits are 48% of round-2 findings (27% in round 1).
- Round 3 and later (17 rounds): 0 bugs, 1 risk, 10 nits. Every finding past round 3 was a nit (CRLF line endings, a failing `printf`, a broken `git`).
- The 6 round-2 bugs were mostly in the round-1 fix or what it left behind (endstack #1, crosspoint #29, crosspoint #40, endstack #20); 2 PRs had genuinely new ones (endstack #8, agent-factory #3).
- None of the 17 escapes needed a fourth round. Only endstack #1 needed a third, and that round would only have re-checked the round-2 fix. Most escapes came from review-bot findings nobody acted on, PRs with no review, and reviews that never ran the build or check that later broke.

## Coverage

| Repo | PRs | verify rounds 0/1/2/3/4/5 | no review of any kind | bot only | total verify rounds |
|---|---|---|---|---|---|
| agent-factory | 25 | 8/10/5/2/0/0 | 6 | 0 (1 panel, 1 same-family) | 26 |
| endstack | 21 | 2/4/9/4/1/1 | 1 | 1 | 43 |
| crosspoint-reader | 20 | 8/4/5/2/0/1 | 3 | 4 (+1 audit) | 25 |
| codex-reset-watch | 17 | 13/3/0/1/0/0 | 1 | 12 | 6 |
| everduet | 25 | 10/11/4/0/0/0 | 10 | 0 | 19 |
| **All** | **108** | **41/32/23/9/1/2** | **21** | **17** | **119** |

## Findings by verify round, all repos

| Round | rounds | rounds with no findings | bug | risk | nit | false positive |
|---|---|---|---|---|---|---|
| 1 | 67 | 16 | 41 | 53 | 37 | 7 |
| 2 | 35 | 18 | 7 | 14 | 19 | 0 |
| 3 | 12 | 6 | 0 | 1 | 6 | 0 |
| 4+ | 5 | 2 | 0 | 0 | 4 | 0 |

Plus 3 round-1 findings (codex-reset-watch #9) that the description does not describe.

Per repo (bug/risk/nit/fp):

| Repo | Round 1 | Round 2 | Round 3 | Round 4+ |
|---|---|---|---|---|
| agent-factory | 9/15/6/0 | 1/3/4/0 | 0/0/0/0 (2 rounds) | none |
| endstack | 15/12/18/0 | 4/5/10/0 | 0/0/5/0 | 0/0/1/0 (3 rounds) |
| crosspoint-reader | 9/19/10/4 | 2/5/4/0 | 0/1/0/0 | 0/0/3/0 (2 rounds) |
| codex-reset-watch | 2/3/1/0 (+3 undescribed) | 0/1/1/0 | 0/0/1/0 | none |
| everduet | 6/4/2/3 | 0/0/0/0 (4 rounds) | none | none |

Fix rates for verify findings: bugs 48/48, risks 64/68, nits 41/66, false positives 0/7 (all 7 rightly rejected).

## Last verify round that found a bug (PRs with verify rounds, n=67)

| none | round 1 | round 2 | round 3+ |
|---|---|---|---|
| 37 | 24 | 6 | 0 |

The 6 round-2 PRs: agent-factory [#3](https://github.com/endqwerty/agent-factory/pull/3); endstack [#1](https://github.com/endqwerty/endstack/pull/1), [#8](https://github.com/endqwerty/endstack/pull/8), [#20](https://github.com/endqwerty/endstack/pull/20); crosspoint-reader [#29](https://github.com/endqwerty/crosspoint-reader/pull/29), [#40](https://github.com/endqwerty/crosspoint-reader/pull/40).

## Stopping rules replayed on the sample

| Rule | PRs that would have shipped a known bug | verify rounds saved (of 119) |
|---|---|---|
| (a) stop after round 1 | 6 (the six above) | 52 |
| (b) stop after the first round that finds no bug (only nits/risks or nothing) | 0 | 25 |
| (c) cap at 3 rounds | 0 | 5 |

Rule (b) also asks for something the loop often skipped: 9 PRs ended on a round that found a bug, fixed it, and never re-checked the fix (agent-factory #12, #24; endstack #1; crosspoint-reader #25, #29; codex-reset-watch #1; everduet #434, #444, #445). Under (b) each would need one more round, so the net saving is about 16 rounds (25 − 9), not 25. In endstack #1 that missing round is exactly the escape fixed by #2.

## Escapes (17 recorded)

| Origin → fix | What | Round that would have caught it |
|---|---|---|
| agent-factory [#15](https://github.com/endqwerty/agent-factory/pull/15) → [#16](https://github.com/endqwerty/agent-factory/pull/16) | graphical capture/record checks asserted 26 stages; broke on main | round 1, had the verifier run those scripts (test-only) |
| agent-factory #21 → [#23](https://github.com/endqwerty/agent-factory/pull/23) | "Run finished never fired outside tests" (live companion reports `idle`) | none run; #21 had no review |
| agent-factory #19 → #23 | exhausted coal stranded the train for good | none run; #19 had no review |
| agent-factory #20 → #23 | observer orders took the locomotive's engines | #20 had only a same-family review, whose round 1 partly fixed it |
| agent-factory #18–22 → #23 | eleven doc statements the code contradicted | nit, any round |
| endstack [#1](https://github.com/endqwerty/endstack/pull/1) → [#2](https://github.com/endqwerty/endstack/pull/2) | final verify wording merged without a current verdict | round 3 of #1: re-checking the round-2 fix |
| endstack #10 → #12 | tracked `.pyc` | review bot flagged it, nobody acted (nit) |
| endstack [#9](https://github.com/endqwerty/endstack/pull/9) → not fixed | fixture committed as a live `AGENTS.md` ("no remote, no PR"), still on main | review bot flagged it on the only commit; Gemini verify passed |
| endstack #15 → #20 | `correct` forces a guard even for judgment-only rules | review bot flagged it; 2 verify rounds did not |
| crosspoint-reader [#32](https://github.com/endqwerty/crosspoint-reader/pull/32) → [#34](https://github.com/endqwerty/crosspoint-reader/pull/34) | README said squash; "Agents read it and merged with --squash" | review bot flagged it; docs PR, no verify |
| crosspoint-reader #26 → #29 | checklist still called cleanup optional | review bot flagged it; #29's round 1 caught it again |
| codex-reset-watch #1 → #2 | `.dockerignore` broke the Docker check stage | round 1, had it built the image |
| codex-reset-watch #1 → #3–6, #11 | backup concurrency test flaky on the deploy VM | none (environment-specific) |
| codex-reset-watch #6 → #11 | bunfig timeout ignored; #6 did nothing | round 1, with a check that the timeout took effect |
| codex-reset-watch [#7](https://github.com/endqwerty/codex-reset-watch/pull/7) → #9 | stale teasers boost the outlook forever | review bot flagged it; no verify round |
| codex-reset-watch [#14](https://github.com/endqwerty/codex-reset-watch/pull/14) → [#16](https://github.com/endqwerty/codex-reset-watch/pull/16) | new test needs `git` in the Docker check stage; every deploy failed | none of 3 rounds ran the Docker build |
| codex-reset-watch [#1](https://github.com/endqwerty/codex-reset-watch/pull/1) → not fixed | retry batch is limited before the eligibility filter, so after an outage newer posts never reach Claude; still on main | review bot flagged it on #1, #2 and #3 |

Escape sources: 7 review-bot findings nobody acted on, 4 where the review never ran the build or check that later failed, 2 PRs with no review at all, 1 same-family review that fixed only part of a defect, 1 unverified last fix (endstack #1), 1 environment-only, 1 docs drift. None needed a 4th round. Only endstack #1 needed a 3rd round, and that round would have re-checked the fix.

## Review bot (separate from the loop)

38 Codex review-bot passes (endstack, crosspoint-reader, codex-reset-watch) raised 11 bugs (3 fixed), 22 risks (4 fixed), 12 nits (0 fixed), 1 false positive. Bot findings nobody acted on account for 7 of the 17 escapes. The bot reviews the PR as opened, so findings on later commits are often never seen.

## Representative later-round findings (verbatim from the PR descriptions)

**Bug (round ≥2)**
1. endstack [#1](https://github.com/endqwerty/endstack/pull/1), round 2: "Issues: the no-verifier fallback still let an author deliver, and DISTILL still stated the old exemption."
2. endstack [#8](https://github.com/endqwerty/endstack/pull/8), round 2: ""quick factual lookup" could swallow "how does X work?" or "is it safe to merge?"; "asks to merge" missed "land"/"ship"."
3. endstack [#20](https://github.com/endqwerty/endstack/pull/20), round 2: "Round 2: ISSUES, one finding. Arena's base switch ignored the rest of the rubric."
4. crosspoint-reader [#29](https://github.com/endqwerty/crosspoint-reader/pull/29), round 2: "| 2, r2-1 | Handoff cycle: commit gated by the PR it publishes |"
5. crosspoint-reader [#40](https://github.com/endqwerty/crosspoint-reader/pull/40), round 2: "the clamped chapter kept the old text offset."
   (agent-factory [#3](https://github.com/endqwerty/agent-factory/pull/3), round 2, appears only in `.audit/frontier-integration-review.md`: "online working work_count=0 followed by needs-input work_count=32 produces pressure=32, so a later tick can spawn an activity wave caused by the input-request snapshot.")

**Risk (round ≥2)**
1. agent-factory [#25](https://github.com/endqwerty/agent-factory/pull/25), round 2: "One P2: a train started before a schedule change kept the old Refuel stop after a reload."
2. endstack [#11](https://github.com/endqwerty/endstack/pull/11), round 2: "FAIL on the checker accepting malformed policy files (a nested `false` under a direct `true`, duplicate keys, …"
3. crosspoint-reader [#35](https://github.com/endqwerty/crosspoint-reader/pull/35), round 3: "**issues** with the guard: a failing `git log` inside a process substitution did not stop the push."
4. codex-reset-watch [#14](https://github.com/endqwerty/codex-reset-watch/pull/14), round 2: "`075f602` FAIL: inherited `GIT_DIR`-style variables, and a git that echoes unknown options with exit 0, both got past the comparison."
5. endstack [#15](https://github.com/endqwerty/endstack/pull/15), round 2: "`correct`'s "Drop a rule once its mistake can't happen" could be read as permission to delete a rule the user just asked for, once its guard exists."

**Nit (round ≥2)**
1. endstack [#7](https://github.com/endqwerty/endstack/pull/7), round 3: "`ca49b2b`: wording fix passed; issues (dry-run entry did not say which wording it tested)."
2. endstack [#11](https://github.com/endqwerty/endstack/pull/11), rounds 3–4: "quoted `"false"`, tabs, trailing text, then CRLF and bare CR"
3. crosspoint-reader [#35](https://github.com/endqwerty/crosspoint-reader/pull/35), round 4: "Round 4 (`4e48950a`): **issues**: a failing nested `git merge-base` still published."
4. crosspoint-reader [#35](https://github.com/endqwerty/crosspoint-reader/pull/35), round 5: "A failure of the guard's `printf` (shown only by replacing the shell builtin with a function that fails) lets a missing subject pass."
5. codex-reset-watch [#14](https://github.com/endqwerty/codex-reset-watch/pull/14), round 3: "a copy of the script placed in a non-repository folder inside another linked worktree would clear that folder. It needs a misplaced copy of the script."

**False positive (round ≥2):** none in the sample. All 7 were in round 1 and were rejected with reasons, e.g. crosspoint-reader [#28](https://github.com/endqwerty/crosspoint-reader/pull/28): "dismissed Library delete ignoring a clipping-sidecar cleanup failure after the book is gone".

## Who merged

- agent-factory: the agent, under the standing ship permission recorded in AGENTS.md (#1 says so; later PRs assume it).
- endstack: Daniel from #3 on (review-first); #1–#2 not stated.
- crosspoint-reader: the agent, under the 2026-10-06 standing authorization (#21, #28 and #35 say it merged).
- everduet: the agent for #410–#428 ("Proceeding with rebase merge and production verification"); #429–#446 not stated.
- codex-reset-watch: not stated.
- No description names a ship or autopilot-full run.

## What the descriptions don't let me determine

- Severity is not recorded. A "bug" here can be low-impact (the director camera's two low-severity bugs in agent-factory #24) or data-losing (agent-factory #9's save deletion).
- Rounds are not uniform. agent-factory reviewers work as one continuous session that rechecks fixes as they land, crosspoint-reader runs up to four parallel "axis" reviews as one round, everduet pairs Codex and Sonnet reviews, and some PRs cite reviews of a sync on `develop` rather than the PR diff. Round boundaries for agent-factory #3/#5 and endstack #11 rounds 2–4 come from commit order and audit files, not explicit labels.
- Descriptions summarise. Many say only "no blockers", "four real problems", "three points addressed" or "pass with notes" without listing them, so findings that the author dropped from the description are invisible and undercounted in every round.
- Classes are mine, from one or two sentences. I did not read diffs to confirm that a "bug" was reachable, and for skill text "bug" is a judgment about what an agent would do.
- Escapes are only those a later PR names or that I could confirm on main (endstack #9, the codex-reset-watch retry limit). The crosspoint-reader #35 bot finding (`sort -u` hides a dropped duplicate-subject commit) is also still on `develop`; it is logged as an unfixed risk, not an escape. I did not search issue trackers or later history systematically, and there are no production incident records.
- Cost per round (time, tokens) is not in the descriptions, so "rounds saved" is a count, not a cost.
- Whether a merge was a ship/autopilot run is not recorded anywhere in the sample.
