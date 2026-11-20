# Audit D: build (+design.md), babysit, ship, autopilot-full, verify (+refs)

Read-only. Bytes are `wc -c` now; "after" is an estimate with all drops and shortens applied.
Evidence docs checked: `docs/design-step.md`, `design-doc-specs.md`, `ship-invocation-check.md`, `verify-reachable-findings.md`, `verify-cheapest-check.md`, `verify-carry-forward.md`, `verify-gate-checks.md`, `2026-11-02-evidence-over-dissent.md`, `delivery-dry-runs.md`, `tdd-keep-tests.md`.

Global/ROUTING facts used for "duplicates":
- ROUTING.md: build/babysit/verify roles; ship and autopilot-full only on explicit request; "autopilot"/"full send" is the request; "Full stop"; architect/arena/interrogate/interview/goldfish/drift/correct/test-design/principles routing.
- Global rules: "Own the work end to end", merge authority, "Check the work" (checks before editing, bug fails first, fresh verifiers), "Pull requests stand alone" (PR body contents, decisions and reversal), "Delegating" (task, paths, ownership, completion criteria), "Disk" (release worktree, preserve branches).

---

## build/SKILL.md (2178 B)

1. L10-11 "Reproduce a bug first."
   - Origin: 07b8f99 2026-10-10 (initial add). No doc evidence.
   - Dup: verify Author step 1 ("A bug gets a failing check first"); global "Check the work" ("for bugs, watch one fail first"); tdd.
   - Verdict: **drop** (about 25 B).
2. L11-13 "Resolve engineering questions from evidence; leave product decisions that change the request to the user."
   - Origin: 07b8f99. No evidence.
   - Dup: global "Decide for yourself", "Ask only for credentials, physical presence, money..."; interview skill for taste.
   - Verdict: **drop** (about 150 B). The global rule already says decide yourself and ask only for the listed cases.
3. L13-16 "Before the first edit ... read design.md ... keep its note."
   - Origin: f4d0d6b 2026-10-16, `docs/design-step.md`. Result: "every run with the change read the design step before code (13 of 13)"; Claude briefs told the builder to read it 4 of 4 vs 0 of 4 without.
   - Verdict: **keep**.
4. L15-16 "A delegated builder gets the note and reads the principles index and that file before coding."
   - Origin: f4d0d6b. Dup: design.md "Delegated builders" says the same thing (L111-115), and step 1.
   - Verdict: **drop here, keep in design.md** (about 105 B). The lead reads design.md before any brief, so the instruction reaches it there.
5. L16 "Report each principle that changed a choice."
   - Origin: f4d0d6b. Dup: design.md "The design note" (L57-58) says "Name each principle that changed a choice".
   - Verdict: **drop** (about 45 B). Also a wording/reporting rule.
6. L17-18 "Implement the smallest complete change. Run the checks on the real artifact and keep their deciding output."
   - Origin: 07b8f99. Dup: verify Author step 2 ("Run them first on the real artifact; keep deciding lines"); global PR "each check with its deciding lines quoted".
   - Verdict: **shorten** to "Implement the smallest complete change." (about 80 B saved).
7. L18 "Read the whole diff, including delegated work."
   - Origin: 07b8f99. Dup: verify L8 "Both roles read the whole diff, delegated work too" (build already links verify).
   - Verdict: **drop** (about 50 B).
8. L19-20 "Use verify for independent review and exemptions. Missing evidence or review means unverified, never ready or done."
   - Origin: 07b8f99. Dup of the second sentence: verify Author steps 3 and 5 ("report unverified", "Deliver only with every required check ... proven"); global "If review cannot run, stop unverified".
   - Verdict: **shorten** to "Use verify for independent review." (about 70 B saved).
9. L21-22 "A correction goes through correct: a recurring defect gets a guard, a preference a note."
   - Origin: 959832c 2026-10-23. Dup: ROUTING "Corrected, a mistake recurs ... `correct`"; global.
   - Verdict: **drop** (about 110 B). Not a build job.
10. L23-27 PR bullet, "non-draft pull request that opens with each choice made for the user and how to reverse it, then a standalone brief: why, what changed, where to start reading, why this approach, checks and deciding evidence, reviewer and exact revision, findings and remaining limits. Follow the project's template. Do not bury required context in the conversation."
    - Origin: 959832c ("PR decisions in build"); 07b8f99 had the standalone brief. No dry-run delta found.
    - Dup: global "Pull requests stand alone" lists the same fields (decisions and reversal, why, what, where to start, approach, checks with deciding lines, verifier and findings, project template, "Record needed facts beyond chat").
    - Verdict: **shorten** to "Prepare a non-draft pull request that follows the project's template and your pull request rules." Keep "non-draft" (not in global). About 330 B saved. Caveat: the skill is meant to be portable; if Daniel wants it to stand without his global file, keep a one-line field list instead (about 150 B saved).
11. L28-29 "Report the pull request, current revision, readiness and anything still needed. Preserve its branch; release only project-prescribed local artifacts."
    - Origin: 07b8f99. Dup: global "End with a PR link", "leave branches alone", "Disk" section on worktree release; the report line is wording only.
    - Verdict: **shorten** to "Report the pull request and revision." (about 100 B saved).
12. L31-34 "Opening a pull request does not start babysitting. Do not merge, arm automatic merging, close the request or write directly to the delivery branch. Ownership, 'keep going' and a budget request do not grant landing authority. A later explicit request to land ... belongs to ship."
    - Origin: 07b8f99. Evidence: `delivery-dry-runs.md` cases 1 and 3 (S arm: non-draft PR, not merged; keep-going no merge). The baseline (N arm) also passed case 1, so uplift is unproven.
    - Dup: ROUTING ("`build` implements ... `ship` or `autopilot-full` only on an explicit request"); global "`build` and `babysit` stop before merging"; project AGENTS.md; ship's description says "keep-going".
    - Verdict: **shorten** to "Do not watch, merge, arm automatic merging or write to the delivery branch; landing is ship's." Keep the core stop (it is build's boundary), drop the keep-going/budget sentence (about 190 B saved).
13. L35-36 "A plan or help request explains the workflow without executing it. An explicit stop means no further writes; report the known state of any issued operations."
    - Origin: 07b8f99. Also in babysit, ship, autopilot-full (4 copies). Evidence: `ship-invocation-check.md` case 3 (help question): OLD and NEW both pass, no uplift; no doc tests the stop rule.
    - Dup: each skill's description ("Not a plan"); the harness handles a stop.
    - Verdict: **drop** from build (about 220 B). See cross-skill item X1.

Estimated build/SKILL.md: 2178 -> about 1050 B.

---

## build/references/design.md (7174 B)

14. L3-6 preamble "...one line per step that applies. A fix whose shape is already settled answers steps 2, 6 and 8 in a sentence each and skips the rest."
    - Origin: f4d0d6b / later edits. Evidence: the fix path is what keeps the step cheap; `design-step.md` "port ... baseline already passes".
    - Verdict: **shorten**. Say "one line per step that applies, `n/a` otherwise". Naming steps 2/6/8 breaks if steps merge (item 17).
15. L8-11 Step 1 Principles ("Open the index now and read all of it").
    - Origin: f4d0d6b. Evidence: Claude read the whole index 0 of 4 with first wording, 4 of 4 with "open it now and read all of it"; 0 of 8 without the step.
    - Verdict: **keep** (this is the uplifted rule).
16. L12-16 Step 2 Ground; L35-38 Step 6 Every consumer.
    - Origin: f4d0d6b, from pstack's Feature playbook. Evidence: `design-step.md` "The port task did not discriminate" (baseline fixed both clients; 5 of 5 with, 3 of 3 without). Mainworthy miss motivated it. Step 2 already says "List every consumer"; step 6 repeats it.
    - Dup: tdd step 1/5 ("Find every consumer with the same fault"); principles "Migrate Callers".
    - Verdict: **shorten**: merge 6 into 2 ("List every consumer that does the same job and change each, verified, or say why one is exempt"). About 350 B saved. Drop "Fixing one client and leaving its sibling broken is an unfinished change" (restates).
17. L17-23 Step 3 Shape ("one tagged value over independent flags ... a table over branching, a parse at the boundary ... make them unrepresentable ... redesign the shape as if that state had been there from the start").
    - Origin: f4d0d6b. Evidence: shape task, tagged union in 5 of 5 with vs 2 of 3 without (small sample).
    - Dup: principles index "Type System Discipline" (illegal states unrepresentable, parse at boundaries), which step 1 makes the agent read.
    - Verdict: **shorten**. Keep "name the data shape before logic; list the combinations the domain forbids; when adding a state, redesign as if it had always been there" (the last clause is the unique one). Drop the parenthetical examples (about 260 B).
18. L24-32 Step 4 Alternatives ("run architect ... Several valid shapes with no clear winner go to arena; a contested one to interrogate").
    - Origin: f4d0d6b. Dup: ROUTING architect/arena/interrogate triggers.
    - Verdict: **shorten**: keep "run architect first; code waits for its shape and, under test-first, for the failing test"; drop the arena/interrogate sentence and the `n/a` examples (about 330 B).
19. L33-34 Step 5 Subtract ("Name what this change makes redundant ... delete it in the same change").
    - Origin: f4d0d6b. No dry-run row. Dup: principles "Subtract Before You Add", "Migrate Callers Then Delete Legacy APIs".
    - Verdict: **keep as one line** (it is a trigger for a principle the agent reads anyway). No saving.
20. L39-42 Step 7 Failure ("end state, how the next run reconciles ... Split shared state before serializing it").
    - Origin: f4d0d6b. No dry-run row. Dup: principles "Make Operations Idempotent" and "Separate Before Serializing Shared State" (the last sentence is a near quote).
    - Verdict: **shorten**: drop "Split shared state before serializing it" (about 50 B).
21. L43-46 Step 8 Tests ("Each test calls the code the way its users do ... A test that avoids a failing state, instead of fixing it, is a finding").
    - Origin: f4d0d6b; the "waits past a failing state" case came from the Mainworthy audit. Dup: test-design (prove it, keep rules), tdd.
    - Verdict: **shorten** to the one unique clause (a test that avoids a failing state is a finding). About 200 B saved.
22. L47-50 "A test written only to prove this change ... leaves the suite in its own last commit; keep one that a plausible later change could break ..., including a migration".
    - Origin: 581a9fd 2026-10-31, `docs/tdd-keep-tests.md`. Exact duplicate: test-design/SKILL.md L37-38 ("Drop it when the fault cannot recur ... A migration that new or restored databases still run is code that stays ... remove it in its own last commit"); ROUTING sends test work there.
    - Verdict: **drop** (about 420 B).
23. L51-53 Step 9 Throughput ("Name the blocking first steps, the workstreams with disjoint files, and the smallest safe split. If one worker is best, say why.").
    - Origin: f4d0d6b. No dry-run row (not in the design-step checks).
    - Dup: ROUTING "Every task, first: ... `swarm`"; global "Delegating" (disjoint files, task paths ownership).
    - Verdict: **shorten** to "Order the work as small units that each end in a check" (the doc's Tasks section depends on it). About 170 B saved.
24. L55-60 "The design note" ("...for a reader, not for a check to parse. The note goes into the pull request's 'why this approach' and into every brief.")
    - Origin: f4d0d6b. Dup: build L13-16 and "Delegated builders" say the same; global PR rule ("Why this approach").
    - Verdict: **shorten**. Drop "It is for a reader, not for a check to parse" (wording only) and the PR/brief sentence's duplicate (about 170 B).
25. L62-66 "The design doc ... A new feature or a change of shape also gets a design doc in the repository".
    - Origin: 678d9c4 2026-11-13, `docs/design-doc-specs.md`. Result: NEW passes 6 of 6; OLD fails or half-passes the 5 targeted cases (the doc itself notes failures are true by construction because old text had no *Behaviour* section).
    - Verdict: **keep**; see 26 to 30 for trims.
26. L68-70 "Before. ... run the interview skill before step 1".
    - Origin: 678d9c4. Dup: ROUTING "`interview` first for a feature shaped by the user's intent or taste".
    - Verdict: **drop** (about 190 B).
27. L74-85 Sections list.
    - Origin: 678d9c4, f4024af. Evidence: design-doc-specs cases 1, 3, 5.
    - Verdict: **shorten** the glosses ("a few plain sentences a casual reader understands", "light on jargon", "a block diagram if it helps", "so no later agent reopens it unknowingly", "with the answer assumed meanwhile"). About 300 B saved; keep section names and the "each naming the test or command that proves it" rule.
28. L86-90 "Test it. Before the first edit ... run goldfish on the doc ... a builder that has to depart updates the doc in the same change".
    - Origin: 678d9c4, 24c552a. Dup: ROUTING says goldfish tests a design doc, but not that it must pass before code.
    - Verdict: **keep**, shorten by one clause ("Mark tasks done as they land" is covered by the Tasks line).
29. L91-99 "Finish it" (delete Implementation and Tasks in a commit of its own before final verify).
    - Origin: f4024af, 24c552a. Evidence: design-doc-specs case 3: OLD "update any stale plan, file list..." fails; NEW "remove Implementation and Tasks in the PR's last commit" passes.
    - Verdict: **keep**; trim the "named kept check / PR holding its proof" detail (about 150 B) only if Daniel wants it smaller; it has no result of its own.
30. L100-107 "Later changes" ("...An older doc with *Checks* instead of *Behaviour* is converted when its feature next changes. Where a scenario and its test disagree, intent decides, as drift sets out ...").
    - Origin: f4024af. No dry-run row for the migration sentence or the drift sentence.
    - Dup: drift skill (intent decides); ROUTING `drift`.
    - Verdict: **drop** the *Checks* conversion (a one-time migration, pre-1.0) and the drift sentence; keep "a change to behaviour edits its scenarios in the same change". About 450 B saved.
31. L108-109 "The pull request links the doc and still carries the note: the pull request records what happened, the doc what is true now."
    - Verdict: **shorten** to "The pull request links the doc and carries the note." (about 60 B).
32. L111-117 "Delegated builders" ("gets the design note, files it owns, checks ..., read principles index and this file; reports back instead of redesigning alone; review the returned diff against the note").
    - Origin: f4d0d6b. Evidence: briefs with the note told builders to read the design step 4 of 4 vs 0 of 4; Codex builders given it read it 2 of 2 and changed the outcome (`quarantined` variant vs nullable field).
    - Dup: global "Give task, paths, ownership and completion criteria".
    - Verdict: **keep**, shorten: drop "the files it owns, the checks that prove it done" (global covers). About 120 B saved.

Estimated design.md: 7174 -> about 4300 B. (Bulk in design doc section; no file can go entirely.)

---

## babysit/SKILL.md (2020 B)

33. L10-12 "Identify the scope. 'Is it green?' is one read-only status pass; 'address comments' is feedback only; 'babysit' is work to ready. A pull request opening or a plan request does not start it."
    - Origin: 07b8f99; status-only wording f510ac8. Dup: description ("A status-only question gets one read-only pass") and ROUTING.
    - Verdict: **shorten** to the three scope cases; drop the last sentence (about 90 B).
34. L13-16 "Keep one watcher ... An event that needs nothing gets no message or comment. Stop watching at readiness ... report unavailable monitoring honestly."
    - Origin: "If the harness can watch" 07b8f99; "Keep one watcher", "no message or comment" f510ac8 (2026-10-27, no doc evidence found; CHANGELOG entry mentions fewer rounds). Dup: global shell rules on `homelab watch`/T3 monitor are the Claude mechanism, not the same rule.
    - Verdict: **keep** "one watcher, no polling loop, stop at readiness". **Drop** "report unavailable monitoring honestly" (generic honesty, about 45 B) and "An event that needs nothing gets no message or comment" only if no evidence appears (it targets chatter; unproven; about 70 B).
35. L17-19 "Work the lowest unmerged dependency only if authorized ... Report conflicts or topology changes to the owner; do not rewrite the stack."
    - Origin: 07b8f99. Residual from stacked-PR skills (autopilot-stack is dropped). Dup: ship step 3 "from the lowest unmerged dependency".
    - Verdict: **shorten** to one sentence (about 100 B).
36. L20-25 "Every finding ... gets a fix or a written reason. Treat it as a claim and check it against the code. Fix real bugs ... smallest change, preferring one that deletes or narrows code; decline nits ... list them as follow-ups. Diagnose a failed check before retrying; tell a flake from a real failure."
    - Origin: f510ac8 for "preferring one that deletes", "tell a flake"; 07b8f99 for the rest. Dup: ship step 2 "Every finding, a bot's included, has a fix or a written reason"; verify Author step 5 ("Decline nits without edits or another round"); global ("Reviews need evidence").
    - Verdict: **shorten**. Keep claim-check, smallest change, diagnose-before-retry. Drop "preferring one that deletes or narrows code" (principles Subtract covers) and "list them as follow-ups" (contradicts verify's "decline nits without ... another round" only in spirit; extra reporting). About 130 B.
37. L26-30 "Recheck ... get verify's current verdict ... Ready means a current independent verdict or valid exemption, passing required checks, no unresolved blocker, no conflict, checks rerun if the base has since changed files it touches, and the host reporting it mergeable."
    - Origin: f510ac8 and review-adoption `final-verdict.md` (PR #24 round 2: step 3/babysit parity). Dup: ship steps 2-3 list the same readiness conditions; verify carry-forward "Same patch on a new base".
    - Verdict: **keep**, shorten "checks rerun if the base has since changed files it touches" (carry-forward covers, about 65 B).
38. L32-36 "Report readiness, fixes, declined findings with reasons, and remaining gates. Owner approval is a wait, not a problem to bypass. Never merge, arm automatic merging, close requests or write to the delivery branch. Explicit landing authority routes to ship. An explicit stop means no further writes."
    - Origin: 07b8f99. Dup: ROUTING; global "build and babysit stop before merging"; build L31-33; ship.
    - Verdict: **shorten** to "Never merge or arm automatic merging; landing is ship's." Drop "Owner approval is a wait" (restates), "write to the delivery branch" is already in project rules, "explicit stop" (X1). About 230 B.

Estimated babysit/SKILL.md: 2020 -> about 1300 B.

---

## ship/SKILL.md (2193 B)

39. L10-15 step 1 "The user invoking this skill by name, or asking to merge ... is the merge authority: land without asking whether to. ... Ask only if no target or several fit. Your own choice of this skill, ownership or a budget never counts. Honor holds, later stops and operator-reserved gates."
    - Origin: 0822db5 2026-11-10, `docs/ship-invocation-check.md`. Result: case 1 OLD "I would ask for explicit authorization to merge PR #41" Fail; NEW "`/ship` supplies merge authority, so I would not ask again" Pass. Cases 2-5 no uplift (both arms pass), including case 4 (self-selection) and case 5 (ask which PR).
    - Dup: ROUTING "`ship` ... only on an explicit request ... "; global "ship ... merge only on explicit words".
    - Verdict: **keep** the first sentence and "land without asking whether to" (the only measured uplift) and the target rule. **Drop** "Your own choice of this skill, ownership or a budget never counts" (case 4 baseline passes; ROUTING and description say it; about 90 B) and "Honor holds, later stops and operator-reserved gates" (about 60 B, generic).
40. L16-21 step 2 "Require verify's independent passing verdict ... Required checks and safety evidence must pass; unresolved blockers or unavailable review stop landing: report them, do not ask for approval. Every finding ... Confirm host mergeability and dependency readiness."
    - Origin: 07b8f99; "do not ask for approval" 0822db5. Evidence: delivery-dry-runs case 5 (behaviour, no verdict: holds), ship-invocation case 2 (stale verdict: both stop; baseline passes).
    - Dup: babysit's readiness list; verify Author step 5 (deliver only with every check proven); review-scope ("If required review cannot run, report unverified and stop delivery").
    - Verdict: **shorten**: "Land only with verify's passing verdict or valid exemption on the current revision, required checks passing, every finding fixed or answered, and host mergeability. Otherwise report the gap; do not ask for approval." About 180 B saved.
41. L22-26 step 3 "Land only the contiguous authorized, verified run from the lowest unmerged dependency, one request at a time ... Do not merge a child into an unlanded parent or arm descendants. Changed revisions or bases require fresh checks and a current passing verdict ... including its carry-forward rules."
    - Origin: 07b8f99; last sentence PR #24 round 2 R1 (`review-adoption/final-verdict.md`: made step 3 match step 2 and babysit). Dup: the last sentence repeats step 2 and verify carry-forward.
    - Verdict: **shorten**; drop the last sentence (about 150 B). Keep the stack ordering (unique to ship).
42. L27-29 step 4 "Confirm each landed result in the intended destination ... Reinspect the next request after each landing. If the remote outcome is unknown, inspect it before retrying. Stop at the first gap."
    - Origin: 07b8f99; delivery-dry-runs case 4 ("merges, confirms the landed result", S arm pass).
    - Verdict: **keep** "confirm the landed result", "inspect before retrying". **Drop** "Reinspect the next request after each landing" (step 2 already runs per request; about 55 B).
43. L30-31 step 5 "Report what actually landed ... Preserve unlanded branches and perform prescribed local cleanup."
    - Dup: global "End with the commit and where it landed", "leave branches alone", "Disk".
    - Verdict: **drop** the whole step (about 215 B), except "report what landed" which the global covers.
44. L33-36 "Do not arm automatic merging without explicit merge-when-ready authority and gates that preserve the verified revision. Merge permission does not authorize deployment, destructive operations or unrelated work. Planning and help questions explain this process without executing it; a stop instruction prevents writes."
    - Origin: 07b8f99. Dup: global ("Do not arm auto-merge", project AGENTS.md); help/stop sentence X1 (ship-invocation case 3 no uplift).
    - Verdict: **shorten** to the first two sentences' core: "Do not arm auto-merge. Merge permission does not authorize deployment, destructive operations or unrelated work." Drop the last sentence. About 170 B.

Estimated ship/SKILL.md: 2193 -> about 1250 B.

---

## autopilot-full/SKILL.md (2019 B)

45. L10-14 "Establish the queue, dependencies, completion checks and operator-held items before execution. 'Autopilot' or 'full send' on named work authorizes both the work and its landing, and nothing then waits for the user's approval; 'keep going' or a budget does neither. If the work is unclear, land nothing. Plan/help requests do not execute."
    - Origin: 07b8f99; "full send" f510ac8 (CHANGELOG 2026-10-27). Evidence: delivery-dry-runs case 7 (explicit grant: docs lands, behaviour held), `design-step.md` round 4 (Codex on explicit "full autopilot this queue" opened autopilot-full and build).
    - Dup: ROUTING states "autopilot or full send on a change is that request ... with no waiting for approval" in nearly the same words; description says "Not ... a budget, a keep-going request".
    - Verdict: **shorten**: keep "Establish the queue, dependencies, completion checks and operator-held items before execution; if unclear, land nothing." Drop the autopilot/full send authorization sentence (ROUTING has it) and plan/help. About 280 B.
46. L15-18 "Compose build, babysit and ship. Their boundaries and verify's independent current-revision gate still apply to each item; autonomy removes prompts and the user's approval, never evidence or the host's protections."
    - Origin: 07b8f99. Dup: ROUTING; global "verify is a gate, not merge authority".
    - Verdict: **shorten** to "Compose build, babysit and ship per item; autonomy removes approval prompts, never evidence or the verify gate." About 100 B.
47. L19-22 "Before any code or brief, complete build's design step. Give each participant a bounded change, ownership and that note. The coordinator owns dependency order and delivery. Land only the authorized verified frontier; do not skip blocked prerequisites or delegate away an operator-held decision."
    - Origin: f4d0d6b (design step; design-step.md round 4 and the autopilot brief rows: Claude briefs told builders to read the step 2 of 2; Codex without it 0 of 1). Rest 07b8f99.
    - Dup: build L13-16 and design.md "Delegated builders"; global Delegating ("task, paths, ownership, completion criteria"); ship step 3 ("contiguous run from the lowest unmerged dependency").
    - Verdict: **shorten** to "Complete build's design step before any code or brief and give each participant it with its change. Land only the verified frontier; never delegate an operator-held decision." About 170 B.
48. L23-27 "Keep a show-me-your-work decision log. Track progress by artifacts and current checks, not reassuring status text. Keep independent authorized work moving when one item is blocked. Stop at queue completion, an authority boundary, or an explicit stop. On stop, place all participants on a no-writes hold and report issued operations' known state."
    - Origin: 07b8f99; show-me-your-work link 7257622. Dup: ROUTING "Long, unattended or multi-phase work: `show-me-your-work`"; "Track progress by artifacts ... not reassuring status text" is a wording rule.
    - Verdict: **shorten**: drop the log sentence (ROUTING covers), "not reassuring status text" (about 130 B). Keep "keep independent work moving", stop conditions and the no-writes hold for participants (unique to a multi-agent run).
49. L28-29 "Report each landed revision and destination, remaining requests and gates, evidence and limits. Release only project-prescribed local artifacts."
    - Dup: ship step 5, global "End with the commit and where it landed", "Disk".
    - Verdict: **drop** (about 190 B).
50. L31-33 "Merge authority is not permission to deploy, delete data, override protections or perform unrelated irreversible actions. Never expand the authorized queue merely to consume spare capacity."
    - Origin: 07b8f99 ("Never expand" present from the start). Dup: ship's "Merge permission does not authorize deployment, destructive operations or unrelated work"; global destructive-action rules.
    - Verdict: **shorten** to one sentence; keep "Never expand the authorized queue" (unique, and a cheap guard against the use-gpt-budget pattern). About 100 B.

Estimated autopilot-full/SKILL.md: 2019 -> about 1050 B.

Cross-skill X1: "plan/help requests explain without executing; explicit stop means no writes" appears in build L35-36, babysit L36, ship L35-36, autopilot-full L14 and L26-27. Origin 07b8f99 (all). Evidence: `ship-invocation-check.md` case 3 shows OLD and NEW both pass without the new text ("no measured uplift"); no doc tests the stop rule. Each description already says "Not for ... planning". Verdict: **drop from all four**, keep only autopilot's participant no-writes hold. About 560 B total across the four (counted in the per-skill estimates).

---

## verify/SKILL.md (2196 B)

Cap is 2,200 B; it is at the limit, so every saved byte is headroom, not just tidying.

51. L8-9 "Both roles read the whole diff, delegated work too, and the rubric, never a summary."
    - Origin: 07b8f99 era / c26c20b. Dup: rubric L3-6 (full diff).
    - Verdict: **keep** (this is the one place the rule lives once I drop build's copy).
52. L13 Author 1 "Before editing, write checks on the real surface. A bug gets a failing check first."
    - Origin: early. Dup: global "Check the work before you deliver it" (nearly verbatim) and tdd.
    - Verdict: **shorten** to "Write checks on the real surface before editing." (about 45 B). Do not drop: verify is the skill the gate cites, and global does not name the surface.
53. L14-15 "Run them first on the real artifact; keep deciding lines. Green tests do not prove the contract."
    - Origin: c26c20b ("Green tests do not prove" 2026-10-27, `review-adoption`). Dup: global PR "Each check with its deciding lines quoted"; review-scope L21-22 ("a green test suite ... alone do not justify an exemption").
    - Verdict: **shorten**: drop "Green tests do not prove the contract." (about 40 B; review-scope states the exemption half).
54. L16-18 step 3 "Apply review scope. Unless exempt, ask one fresh read-only verifier. Without one, report unverified."
    - Dup: global ("one verifier from each of the other two providers", "If review cannot run, stop unverified") and review-scope L28-30. Note a conflict: global requires two other-provider verifiers; the skill (c26c20b) says same provider qualifies. Global wins in Daniel's setup, so the skill text is the portable default.
    - Verdict: **keep** (core), **drop** "Without one, report unverified" (review-scope L29 says it; about 30 B).
55. L18-20 step 4 "Give it the task, checks and revision range, not your conclusions; for a re-review, the change since the last verdict, what it affects and open findings."
    - Dup: rubric L3-6 ("Exclude the author's conversation, reasoning and desired verdict"); carry-forward ("Anything else" re-review scope).
    - Verdict: **shorten** to "Give it the task, checks and revision range, not your conclusions." (about 100 B). The re-review scope is in carry-forward L56-59.
56. L21-25 step 5 "Re-rank findings. Fix blockers and shoulds with the cheapest check catching them again; rerun affected checks. Decline nits without edits or another round. Carry-forward governs fixes. Deliver only with every required check and safety fact proven on this revision, a fresh pass or valid exemption, no blocker or should open."
    - Origin: f510ac8 (rank), 6136a6b ("cheapest check", `verify-cheapest-check.md`: new text added only a unit regression and "Add no database or browser tests" vs old adding a Chromium test; one sample), c30a85d (nit fixes follow carry-forward).
    - Dup: global "Check the work" (deliver gates); build/ship/babysit repeat the deliver condition.
    - Verdict: **keep** the cheapest-check clause (measured), "decline nits". **Drop** "Carry-forward governs fixes" (verify already links carry-forward from the first re-review line; about 40 B) and "rerun affected checks" (about 25 B).
57. L26-27 step 6 "Open after two rounds: stop and rethink the approach or scope. At most two more; still open, stop delivery, report both sides."
    - Origin: c26c20b round cap (earlier 12502d8 "rethink after two rounds"; CHANGELOG 2026-10-27 reports it came from three Mainworthy rounds). No dry-run delta.
    - Verdict: **keep** (a cap, real cost in re-verification loops: "173 of 297 rounds were re-verifications", `verify-carry-forward.md`).
58. L31-33 Verifier "Run every check yourself; reproduce a failure, suspecting your method first. Answer each pass, issues or not checked, with deciding lines; unrun is not checked."
    - Origin: ce62399 ("unrun is not checked" 2026-11-02, evidence-over-dissent); 07b8f99. Dup: rubric L11-15 ("The verifier still runs every required check ... Report commands, decisive output"), L38-41.
    - Verdict: **keep** one copy; **drop** the rubric copy of "Report commands, decisive output and revision; omit routine passing logs" (see 64).
59. L34-35 "Name the fact its safety rests on; prove it on the real code or mark it unproven."
    - Origin: f510ac8. Evidence: `verify-gate-checks.md` check 8 (pass with unchecked safety fact is not delivery). Dup: rubric L38-41.
    - Verdict: **keep**.
60. L36-38 "Try to break it: inputs, failure paths, callers, what the diff omits. A base defect is the base's unless the change copies or newly reaches it."
    - Origin: 484dff8 (Try to break it, 2026-10-16); c30a85d (base defect). Dup: rubric L17-19 ("Check ... failure paths, including omissions in the diff").
    - Verdict: **keep** SKILL, **drop** the duplicate rubric sentence (see 64).
61. L39-44 ranking: "Blocker ... Should ... Nit ... Data loss, security or a trust boundary is never a nit."
    - Origin: c30a85d `verify-reachable-findings.md`: of 32 guards, 28 had a real path; the 4 unneeded ones came from 3 findings; the ranking makes "nothing shown reaches it" a nit. Dry-run: new text rated unreachable guard findings as nits (see doc). Evidence is solid.
    - Verdict: **keep**; trim the nit list ("wording, extra tests or guards, small costs, what only later code makes") only if bytes are needed.
62. L45 "Name the revision and patch judged. Change nothing."
    - Dup: "Change nothing" is the read-only role (global verifiers read-only). "Name the revision" is also in rubric L15 and carry-forward L8-9.
    - Verdict: **shorten**: "Name the revision and patch judged." (about 15 B).

Estimated verify/SKILL.md: 2196 -> about 1850 B.

---

## verify/references/review-rubric.md (3317 B)

63. L3-10 "Give the reviewer requirements, project rules, full diff, base/head, checks. Let it inspect surrounding code ... Exclude the author's conversation ... Fresh context does not mean diff-only access." plus "When the change has a design doc, its Behaviour scenarios are requirements ...".
    - Origin: c26c20b (rubric), f4024af (Behaviour sentence, `design-doc-specs.md` case 5: OLD "comparing the implementation with the requirements and design" Fail; NEW names scenarios).
    - Dup: SKILL step 4 ("not your conclusions"); review-scope L3-8.
    - Verdict: **keep**; shorten "Fresh context does not mean diff-only access" (restates "Let it inspect surrounding code"; about 45 B).
64. L11-15 "Run required deterministic checks before review. Fix their failures first; if one cannot run, record that gap. A requested review can investigate the gap, but cannot turn it into a pass. The verifier still runs every required check ... Report commands, decisive output and revision; omit routine passing logs, while retaining full logs when needed to diagnose."
    - Dup: review-scope L3 ("Run deterministic checks first"); SKILL L31-33 and L16-18; global "Run deterministic checks first".
    - Verdict: **shorten**; drop the deterministic-first sentence and the "omit routine passing logs" clause (a reporting/wording rule, about 190 B).
65. L17-23 "Check the requirements and ... paths, including omissions in the diff. Do not limit safety review to a flawed or incomplete spec. For each candidate finding, trace ... Supply the location, trigger, expected and actual behavior, and a reproducer or a concrete code trace. A code trace supports a finding; it does not replace an unrun required check."
    - Origin: c26c20b; evidence rule ce62399 (`2026-11-02-evidence-over-dissent.md`: "rank as a nit any review finding that no failing check or code trace backs"). Dup: SKILL L36-38 ("Try to break it ... what the diff omits") and ranking L39-44.
    - Verdict: **keep** evidence/format ("location, trigger, expected and actual"); **drop** the first sentence (SKILL covers; about 190 B).
66. L25-31 "That evidence is what 'show what reaches it' means ... A finding with neither is a nit ... One on data loss ... goes under not checked".
    - Origin: ce62399. Evidence: doc above. Dup: SKILL L39-44 and L34-35.
    - Verdict: **keep** (defines "shown"); shorten the sentence "however serious it sounds, and the author declines it" (about 40 B).
67. L33-37 "Skip style, naming, optional refactors, redundant tests and guards for hypothetical future code. A required compatibility or safety property is not style. Factual errors in evidence or requirements are correctness defects, not wording nits. Report blockers and shoulds with evidence, not a minimum count."
    - Origin: c26c20b. Dup: SKILL nit definition ("wording, extra tests or guards"); the "not a minimum count" line is wording.
    - Verdict: **shorten** to "Skip style, naming and optional refactors. A required compatibility or safety property is not style; factual errors in evidence are defects." About 120 B.
68. L38-41 "Put a missing check or unresolved safety fact under not checked, not among confirmed defects. Do not label an evidenced security or data-loss path a nit because it is unusual. No findings is a valid result, but not checked still prevents a passing verdict when evidence is required."
    - Origin: c26c20b; c30a85d ("reachability wins over rarity", `verify-reachable-findings.md`). Dup: SKILL L34-35 and L44 ("never a nit"); "No findings is a valid result" is reassurance wording.
    - Verdict: **shorten**: drop the middle sentence (SKILL L44) and "No findings is a valid result" (about 150 B).
69. L43-48 "One first pass is the default, not a one-pass approval guarantee. Re-review only for fixes or new evidence that the carry-forward rules require ... Preserve stricter project review requirements and the existing round cap. Do not add a reviewer just to seek more findings or reconsider a declined style suggestion."
    - Origin: c26c20b. Dup: SKILL step 6 (round cap); review-scope L4 ("One fresh initial reviewer is the default") and L15 ("A project may require stricter review"); carry-forward.
    - Verdict: **shorten** to "Re-review only as carry-forward requires, scoped to the change and its dependents; do not add a reviewer to seek more findings." About 380 B saved.
70. L50-55 "For validation, helpers and catches, apply the boundary and reader-load rules. Name the existing guarantee before removing validation ..."
    - Origin: c26c20b ("boundary defaults"). Evidence: `verify-reachable-findings.md` motivation (guards with no path). Dup: the two principle references themselves.
    - Verdict: **shorten**: keep the links and the "name the guarantee/reachable path/benefit" rule; this is the only place the verifier is told to look at these principles (design-step turned down adding a design check to verify). About 120 B.

Estimated review-rubric.md: 3317 -> about 2150 B.

---

## verify/references/review-scope.md (1862 B)

71. L3-8 "Run deterministic checks first. One fresh initial reviewer is the default. Independent means a separate read-only context ... same provider or model family qualifies. A different family is optional ...; it is not a gate. The author reviewing their own work never substitutes."
    - Origin: c26c20b ("same provider"). Dup: global "Check the work" requires verifiers from the other two providers and says self-review never qualifies; SKILL step 3.
    - Verdict: **shorten**; drop "Run deterministic checks first" (rubric has it) and "The author reviewing their own work never substitutes" (global; and Independent already defines it). About 120 B. Keep the same-provider clause: it is the portable default that global overrides.
72. L12-16 Exemptions "An exemption skips model review, never required checks or host protections. Record the current revision, changed contract, why the risk is low, exact checks and deciding outputs, and why they cover all affected behavior. Name any assumptions and show they hold. A project may require stricter review. An explicit request to review still gets a review."
    - Origin: c26c20b; `review-adoption/` (paired old/new policy results). Dup: global "Its justified review exemptions require the current revision, low-risk scope and complete deciding evidence; they never skip checks or stricter project rules" (a near paraphrase).
    - Verdict: **shorten** by dropping "never required checks or host protections" and "A project may require stricter review" (global has both; about 110 B). Keep the record fields and "An explicit request to review still gets a review".
73. L18-23 "Exempt changes may include ordinary prose ... Size, a green test suite, a snapshot, static types or the author's confidence alone do not justify an exemption. An exemption has no unresolved safety fact or missing required evidence."
    - Origin: c26c20b. Evidence: review-adoption/policy-new vs policy-old results.
    - Verdict: **keep**.
74. L25-30 "Do not exempt changes to agent instructions, security or authorization, money, persistent data or migrations, production deployment, concurrency, or external contracts. Use a fresh reviewer whenever coverage ... needs unresolved judgment. If required review cannot run, report unverified and stop delivery. Do not lower the risk merely to bypass an unavailable reviewer."
    - Origin: c26c20b. Dup: global "If review cannot run, stop unverified"; SKILL step 3 ("Without one, report unverified"); description of verify (behaviour, data, auth, money, deployment).
    - Verdict: **shorten**: keep the do-not-exempt list; drop "report unverified and stop delivery" here OR in SKILL (one copy) and "Do not lower the risk merely to bypass" (about 130 B).
75. L32-33 "A new behavior change needs a new exemption decision or a fresh verdict. A verdict already obtained follows the existing carry-forward rules."
    - Dup: carry-forward "Anything else" (L51-59) says the same.
    - Verdict: **drop** (about 170 B).

Estimated review-scope.md: 1862 -> about 1250 B.

---

## verify/references/carry-forward.md (3102 B)

76. L3-6 "A verdict covers a patch ... judging verdicts by revision re-verifies code nobody changed. Judge by patch instead."
    - Origin: 58983af 2026-10-21, `verify-carry-forward.md`: 173 of 297 rounds were re-verifications; 23 re-checked code the verifier itself called unchanged ($26). Evidence solid.
    - Verdict: **keep**; shorten the first two sentences (the "why" is in the doc, not needed by the agent; about 120 B).
77. L8-16 "At each verdict, record the revision, the base and the patch identity: a fingerprint ... ignores line offsets and commit metadata ... keep every byte of the changed lines, whitespace included ... The author does the comparison and records it; a claim that 'nothing changed' without it carries nothing."
    - Origin: 58983af plus whitespace fix. Verdict: **keep**; trim the whitespace example sentence to "keep whitespace" (about 100 B).
78. L18-25 "Same patch on a new base ... A rebase that needed a conflict resolution changed the patch."
    - Verdict: **keep**.
79. L27-43 "Patch changed only in tests, docs or lint configuration" (two parts; noise definition; "An agent's rules or skills ... are behaviour here").
    - Origin: 58983af. Evidence: `verify-carry-forward.md` dry run (scenarios). Dup: "An agent's rules or skills ... are behaviour" repeats review-scope L25 ("agent instructions") and carry-forward L47-48.
    - Verdict: **keep**; drop the "agent's rules or skills" sentence here and keep it once in "Prose nothing reads as instructions" (about 150 B).
80. L45-49 "Prose nothing reads as instructions ... keeps the verdict. Record that evidence and rerun the required checks."
    - Origin: 8e53f1f 2026-10-14, `verify-carry-forward.md` dry run (lint directive row added after review).
    - Verdict: **keep**.
81. L51-59 "Anything else ... A documented low-risk exemption may replace a new model verdict only when its full affected contract and earlier findings are resolved by current deterministic evidence. ... One verifier is enough after a conflict resolution or a small fix; a full review again is for new behaviour, a redesign or a large new diff."
    - Origin: 58983af; exemption sentence PR #24 (final-verdict R1). Dup: review-scope L18-23, L32-33.
    - Verdict: **shorten**; drop the exemption sentence (review-scope has it) and "a full review again is for ..." (SKILL/rubric already say fresh review for new behaviour; about 260 B).
82. L61-62 "Never stand in for the comparison with matching commit messages, a summary of the change, or a passing check from an older revision."
    - Origin: 58983af. Dup: L14-16 "a claim that 'nothing changed' without it carries nothing".
    - Verdict: **drop** (about 190 B), or fold to "or an older revision's check" in L14-16.

Estimated carry-forward.md: 3102 -> about 2200 B.

---

## Totals

| Skill | Now | After (est.) | Files that could go |
| --- | ---: | ---: | --- |
| build/SKILL.md | 2178 | 1050 | none |
| build/references/design.md | 7174 | 4300 | none (the design doc section is the only home of that rule, and design-doc-specs shows it works) |
| babysit/SKILL.md | 2020 | 1300 | none |
| ship/SKILL.md | 2193 | 1250 | none |
| autopilot-full/SKILL.md | 2019 | 1050 | none |
| verify/SKILL.md | 2196 | 1850 | none |
| verify/references/review-rubric.md | 3317 | 2150 | none |
| verify/references/review-scope.md | 1862 | 1250 | none |
| verify/references/carry-forward.md | 3102 | 2200 | none |

No reference file can go entirely: carry-forward is backed by measured waste (173 of 297 rounds), review-scope carries the exemption list the global rules point to, review-rubric defines "shown", and design.md is the only holder of the design step and design-doc rules.

## Most notable

1. Duplicated tail across the four delivery skills: "plan/help explains without executing", "explicit stop means no writes", "release prescribed local artifacts", "preserve branch", "report what landed" repeat in build, babysit, ship and autopilot-full, and the global rules and descriptions already say them. `ship-invocation-check.md` case 3 shows no uplift. About 560 to 900 B across the four.
2. design.md duplicates other skills: the test-keep paragraph (L47-50) is a near copy of test-design L37-38; steps 3, 5, 7 restate principles the agent is told to read in step 1; the interview/arena/interrogate/drift lines repeat ROUTING. About 1,700 B of the 2,900 B saving is here, and none of it has a dry-run result of its own (the measured uplift is step 1, the design-step read, the shape result, and the doc/scenario rules).
3. Only three rules in these skills have a measured deciding result that a drop would break: ship's "land without asking whether to" (case 1: "I would ask for explicit authorization" vs "`/ship` supplies merge authority"), verify's reachability ranking (28 of 32 guards had a real path) and cheapest-check clause, and the carry-forward patch comparison (173 of 297 re-verification rounds). The rest of the unmeasured wording, notably the PR bullet in build that duplicates global "Pull requests stand alone", is the best shortening target.
