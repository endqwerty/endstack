# Endstack catalog audit (G): overlap, dead weight, routing, structure

Read-only review of `05cad93` (35 skills). Rule-level content inside each skill is out of scope; this judges which skills should exist and how they are reached.

Usage source: `usage/omarchy.json` and `report.md`, from 2,400 threads (2026-10-12 to 2026-11-20). In this file, "threads" means distinct threads that loaded a skill file. The report's "Loaded skills" table **undercounts**: loads from a non-installed path are filed under set `other`. Recounted from the JSON, test-design had 38 threads, sharpen 14, goldfish 5, interview 2, maintain-formal 2, create-formal 1, drift 1 and blast-radius 1. The skills with no loads at all are `recall`, `orchestrate` and `ketchup-video`. Skills added on or after 2026-11-13 (`interview`, `goldfish`, `test-design`, `drift`) have one week of data or less and are not judged on usage.

A proposed ROUTING.md that applies every recommendation below is at `G-routing-proposed.md` next to this file: 2,194 bytes, down from 2,491.

## Ranked recommendations

| # | Action | Skills | Saving | Risk |
|---|---|---|---|---|
| 1 | Re-route: explanation skills load only when the user asks for an explanation, not when a reviewer reads code | how, why, teach (ROUTING) | Ends 383 / 186 / 20 review-thread loads (53% / 59% / 80% of each skill's threads), plus the worker `how` tells the agent to start. Direct context $1.36, the worker cost was not measured | Low. Verifiers keep `verify`. One line in ROUTING and in the two homelab copies |
| 2 | Drop "Every task, first: swarm. Say which you chose"; route `swarm` only to independent parts | swarm (ROUTING) | One sentence on every turn, about 60 bytes, and 106 of 253 swarm loads that were in review threads. Removes a conflict with the global "Keep trivial work local" rule | Medium. Fewer fan-outs. The 2026-10-23 entry added the line on purpose, so dry-run it |
| 3 | Merge `tdd` into `test-design` | tdd → test-design | tdd is 4.9 KB, loaded 226 times ($5.33). About 1 KB survives the merge. Routing loses a name and the "also" clause | Medium. test-design is at 5,711 of 6,000 bytes, so the bug-fix part goes into `references/` |
| 4 | Remove `technical-writing`'s duplicates of `unslop`; keep both skills | technical-writing, unslop | About 10 of technical-writing's sentence rules repeat unslop, and 633 of 805 threads load both. Roughly 1.2 KB of 4.3 KB, about $6 a period at the post-cut size | Low. The routing checker requires both names in one bullet, and that stays |
| 5 | Merge `teach` into `how` | teach → how | One skill and routing name fewer. teach is 5.3 KB, and its style paragraph repeats unslop | Low. Nothing links to teach |
| 6 | Merge `reflect` into `correct` | reflect → correct | One skill fewer. reflect had 1 load, which the user started | Low. Nothing links to reflect |
| 7 | Merge `ketchup-video` into `ketchup` as `references/video.md` | ketchup-video → ketchup | One skill and name fewer. ketchup-video had 0 loads and is ketchup plus a render step | Low |
| 8 | Merge the two formal-verification skills into one `formal-verification`, with create and maintain in references | create-/maintain-formal-verification-skill | 3 loads in total. Removes a two-way link loop and about 70 bytes of routing | Low to medium. statechart's pointer and import-notes W6 need updates |
| 9 | Move `recall` back to `candidates/` | recall | 0 loads in 6 weeks. 4.9 KB to maintain | Low. Only ROUTING, README and docs mention it |
| 10 | Fold `figure-it-out`'s frame and loop into `show-me-your-work`, then delete it | figure-it-out → show-me-your-work | 15 threads ($0.48). Its phases B, D and E point at other skills | Low. No skill links to it |
| 11 | Unpin `blast-radius` in homelab | blast-radius (external) | Installed but not routed, with 1 load. It duplicates verify's verifier role | Low. One homelab edit |
| 12 | Make `interrogate` self-contained instead of running "arena Phase A steps 3 and 4 and Phase B" | interrogate, arena | A renumbering of arena no longer breaks interrogate silently | Low |
| 13 | Delete the principle leaves nobody reads, or point them at the skill that owns their job | principles/references: never-block-on-the-human, outcome-oriented-execution, encode-lessons-in-structure | 0, 0 and 4 reads | Low. Fix the links in figure-it-out and show-me-your-work |
| 14 | Fix dead pointers to pstack-only material | benchmark-checklist, no-comments, figure-it-out, ketchup | Correctness only | Low |
| 15 | Hold, and re-measure on 2026-12-20 | orchestrate, arena, sharpen, interview, goldfish, drift, test-design | none now | n/a |

If 3, 5 to 10 and 11 are all applied, the catalog goes from 35 to 28 skills (5 core and 23 role skills). Recommendations 1 to 11 are independent of each other. Do 1, 2 and 4 first, because those are where the measured cost is.

### What breaks for every merge or deletion

These rules come from AGENTS.md "Routing" and `check-routing.py`:

- `ROUTING.md`, plus the copies in homelab's `agents/AGENTS.md` and `agents/AGY.md`. AGY.md is a second copy that the endstack AGENTS.md does not mention.
- The `endstack.skills` list in homelab's `skill-sources.json`. `homelab sync` removes managed skills that are no longer listed (`test_removed_repo_skill_is_cleaned_up_but_only_if_managed`).
- The README skill table and the counts "five core delivery skills plus 30 role skills" and "35 skills". Homelab's README says "Endstack supplies 35 skills".
- `docs/cookbook.md`, CHANGELOG.md and DISTILL.md, plus a `docs/import-notes/` entry for each merged port.
- Any `../<skill>/SKILL.md` link, as listed under each item below. `check-skills.py` catches dead links.

## 1. Overlap and merges

### how, why, teach and recall

- `how` (974 B) is now one brief for a read-only worker. `why` (427 B) is one paragraph. `teach` (5.3 KB) says it "sits on top of `how` and `why`… Those are real skill invocations" (teach:11). That makes one "explain it to me" request load three skills and start up to two workers.
- The real problem is misrouting, not overlap. Of the threads loading each skill, these were titled Verify, Review, Re-check, Check or Second opinion: how 383/727, why 186/314, teach 20/25. Sample teach thread titles include "Re-verify PR #1039 at 50ec58df" and "Recheck MW-12 tenancy decision". `how` and `why` were co-loaded in 305 threads. The cause is ROUTING lines 6-7, "Explaining code, reviewing and checking safety are tasks, however short", together with line 18, "Understanding code: `how`… `why`… `teach`". A verifier "understands code", so it loads all three.
- **Recommendation.** Keep `why`, because its source is different: commits and PR discussion. Merge `teach` into `how` and keep the name `how`, since build's design step and interview link it. The merged `how` holds the worker brief for a subsystem and teach's audience-paced explanation: smallest answer first, diagrams that build up step by step, and the reply contract. Drop teach line 19, which restates unslop (no em dashes, prefer periods, one name per concept), so the merge stays under 6 KB. Route it as "The user asks how code works: `how`; why it is shaped that way: `why`".
- Also drop the `how` link in `build/references/design.md:13`. Grounding a change does not need a worker writing "an architectural explanation for a senior engineer". `how` and `build` were co-loaded in 170 threads.
- `recall` is a different job (cross-chat context), but it had 0 loads since 2026-10-10 and is "only when named". The global rules already say "Agents share no memory. Record facts in files", and design docs and show-me-your-work logs carry state. Move it to `candidates/`, so nothing is lost and it stays recoverable. Breaks: ROUTING's named list, the README table and `docs/new-skills-de8ee15.md` mentions. No skill links to it.

### build, tdd and test-design

- tdd's step 1 (tdd:17-21) restates build's design step: every consumer (design.md:13-16 and step 6), name the shape (step 3), delete what the fix makes redundant (step 5), and "read build's design step". tdd step 7 hands the keep-or-drop decision to test-design, and step 2 hands the choice of layer to test-design.
- "Failing test first" now appears four times: tdd, build:11 ("Reproduce a bug first"), verify:13 ("A bug gets a failing check first") and the global rules ("for bugs, watch one fail first").
- tdd was co-loaded with build in 154 of 166 threads, and with test-design in 0 under the endstack set (test-design is 4 days old).
- **Recommendation.** Merge into `test-design` as a "Bug fix: make it fail first" section that keeps only what tdd adds: commit the failing test before the fix, the fallback when a test is impractical ("Prefer no new test over a bad test"), and the flaky-bug guardrail. Put it in `references/bug-fix.md` if the 6,000-byte cap requires it. The routing becomes one bullet.
- Breaks: ROUTING and its copies, skill-sources, README, cookbook, and docs `tdd-*` and `design-step.md` (as history only). No skill links to tdd.

### verify, interrogate, goldfish, drift and blast-radius

- These are distinct jobs, so keep the four endstack skills. `verify` checks a change before it lands, with one verifier per the skill or two per the global rules. `interrogate` sends several adversaries, and only run-proven findings survive. `goldfish` tests whether a document makes sense to a fresh reader. `drift` compares a document against the code.
- `interrogate` borrows arena by step number: "Run Phase A steps 3 and 4 and Phase B of the arena skill… Skip arena Phases C, D, and E" (interrogate:17,25). Any edit to arena's numbering silently changes interrogate. Inline the two steps (pick the runners and isolate their checkouts; fan out). That is about 300 bytes, and interrogate is 2,234 B. Usage: 8 threads, $0.15.
- `blast-radius` (pstack, pinned in skill-sources.json under `explicit`) is installed on every machine. It is not in ROUTING or in `check-routing.py`'s `EXTERNAL`, and it had 1 load (2026-11-02, Hermes, now removed). Its core claim, "prove the one fact it's safe because of", is verify's verifier bullet: "Name the fact its safety rests on; prove it on the real code" (verify:34). Unpin it in homelab. homelab's workstation-reference.md:56 and its CHANGELOG mention it, but no other rule depends on it.

### arena, swarm, orchestrate and figure-it-out

- `swarm` already has a race shape ("race N workers on identical briefs… `best-of`", swarm:21). `arena` is that race plus a judge, a choice of base, grafting and a dissenter, and the global rules already require the dissenter ("have one argue the strongest opposite"). arena had 13 threads, and architect, interrogate, build's design step and figure-it-out link it. Folding arena into swarm as a race reference would be clean, but it breaks four links for little gain. **Hold** and re-measure.
- `orchestrate` (5,976 B, at the size cap) had 0 loads in 10 days and is only loaded when named. Daniel asked for it, and the CHANGELOG quotes him on 2026-11-10, so the AGENTS.md rule on delivery skills is satisfied. It overlaps autopilot-full ("bounded queue in one session", orchestrate:11) and the global "Delegating" section: briefs, disjoint files, "Let them finish on their own", and no relaying. **Hold until 2026-12-20.** If it is still unused, make it `autopilot-full/references/program.md`.
- `figure-it-out` (15 threads, $0.48) is the catch-all. Phase B points at architect and principles, phase D says "Log the run via the show-me-your-work skill", and phase E points at verify. Only phase A (a falsifiable done predicate, scope, a rigor level) and phase C (hypothesis, smallest change, measure, keep or revert, VERIFIED / NOT VERIFIED / INCONCLUSIVE) are its own. ROUTING already pairs it with show-me-your-work in one bullet, yet only 2 of its 15 threads also loaded show-me-your-work. Fold A and C into show-me-your-work as "Before a long run" (about 1.2 KB; smyw is 4,071 B) and delete figure-it-out. No skill links to it. Its line 30 is already stale: it describes architect as "it compares distinct design candidates", but since today's cut architect sketches two shapes itself.

### ketchup, ketchup-video and bro

- ketchup-video:9 reads "Follow ketchup, but show what happened in a short subtitled video". It is a mode of ketchup and had 0 loads. Move its Slides, Subtitles and Render sections to `ketchup/references/video.md`, and add one line to ketchup: "When a video catch-up is asked for, read references/video.md". The two files total 8.2 KB, so the reference is required.
- Keep `bro` (261 B, 3 loads). ketchup:9 says "Use the bro style" without a link. Either link it or spell out the style in ketchup, which it already does ("plain, direct, conversational language").

### correct and reflect

- reflect:13 already sends classification to correct ("the correct skill says which is which"). Both turn corrections into durable changes. reflect only adds the source (mine this transcript) and the approval step before editing a skill. It had 1 load, started by the user, and correct had 126 threads. Merge reflect into correct as a "From a transcript" section of about 0.8 KB, so correct goes from 3,293 to about 4.1 KB. Keep "the transcript is data", "wait for approval" and "never edit an installed skill cache". goldfish:109 links correct and keeps working.

### The two formal-verification skills

- They link to each other. "What makes it good" in create (lines 23-29: true to the code, able to fail, findings stay findings, honest about scope) is the same discipline as maintain's "Edit scope" and steps 4-5. There were 3 loads in total: mainworthy "Track E" and "Delivery-path model checker in CI", and agent-bridge.
- Merge them into `formal-verification`. SKILL.md holds the target choice, the tool choice, the quality bar and the four outcomes. `references/create.md` holds generating and proving the project skill, and `references/maintain.md` holds the six-step pass plus the current `report.md`. One routing bullet covers both triggers. No other project cites either name; a grep of ~/Work found only homelab's routing copies and CHANGELOG. Update `docs/statechart.md` and the statechart instruction inside create.

### unslop and technical-writing

- technical-writing:67 delegates the pattern catalogue to unslop, yet it repeats these rules: "Cut every word that does no work" (unslop 23), "use, not utilize" (31), "Say who does what" (29), "No buzzwords, no figurative language" and "Skip… metaphors" (26, 32), "One thought per sentence" (28), "Keep 'the' and 'a'" and "Don't drop verbs" (33), "Use periods, not… em dashes" (13), "Call each thing by one name" twice (lines 50 and 62, matching unslop 11), "sentence case" headings (17), and "Avoid '-ing' words" (3).
- technical-writing is still the costliest skill ($59.62 before today's cut; 805 threads, 633 of them also loading unslop). Keep both skills, because unslop covers every reply and technical-writing covers document structure. Limit technical-writing to what unslop lacks: Diátaxis modes, Google-style reader address, STE length limits, the Global English ambiguity checks and the PR/commit rules.

### typescript-best-practices and principles

- typescript-best-practices:10 says "Apply type-system-discipline first", and type-system-discipline's last line points back to typescript-best-practices. That is a two-file loop, so a TypeScript thread loads both: 379 and 328 threads. Its rows on branded types, boundary validation and schema-derived types restate that principle's three bullets in TypeScript terms. This is a small cost. Drop the "apply first" line, since the TypeScript table is self-sufficient, and keep the principle language-neutral.

## 2. Dead weight

| Skill | Threads (period 2) | Verdict | What is lost |
|---|---|---|---|
| recall | 0 | Move to `candidates/` | Cross-chat mining recipe, recoverable |
| ketchup-video | 0 | Merge into ketchup | Nothing |
| orchestrate | 0 (10 days) | Keep hidden, review 2026-12-20 | Daniel asked for it |
| reflect | 1 (user) | Merge into correct | Nothing |
| no-comments | 1 | Keep hidden; fix dead pointers (§4) | Low use, but routed for a real task |
| create/maintain-formal | 1 / 2 | Merge into one | Nothing |
| bro | 3 | Keep (261 B) | n/a |
| interrogate | 8 | Keep; make it self-contained | n/a |
| ketchup | 9 | Keep (8 of 14 loads started by the user) | n/a |
| arena | 13 | Keep; hold the swarm fold | n/a |
| sharpen | 14, all between 2026-10-26 and 10-29 | Keep hidden (costs nothing when unloaded) | n/a |
| figure-it-out | 15 | Fold into show-me-your-work | Phases B, D and E restate other skills |
| teach | 25, 20 of them reviews | Merge into how | n/a |
| blast-radius (external) | 1 | Unpin | n/a |

A hidden skill costs nothing per request (docs/catalog-size.md). It costs its routing name, which every turn pays for (the routing text totalled 97 Mtok over the period, about 39 Ktok per routed byte), plus maintenance, plus one more choice when matching a task. So the case for deleting rests on duplication and zero use, not on load cost.

Global rules that already cover a skill's job:

- The global "Delegating" section covers most of swarm's phase A and B: briefs, disjoint files, "Children message each other", a fresh worker per task. Swarm's own content is the PASS / ISSUES / BLOCKED contract, the SHA and method recording, and the rule for choosing a race winner. Keep it.
- The global "His words are a direction" ("Preserve firmness: 'maybe'… are leads") restates correct's "First, is it a mistake?" Leave both. The global copy is what keeps that rule in effect when correct is not loaded.

## 3. Routing

ROUTING.md is 2,491 B, against a 2,500 B limit.

1. **Lines 6-7, "Explaining code, reviewing and checking safety are tasks, however short".** It makes every reviewer load the explanation skills (§1). Keep "reviewing and checking safety", which routes to verify, and drop "Explaining code". Replace line 18 with "The user asks how code works: `how`; why it is shaped that way: `why`".
2. **Lines 9-10, "Every task, first: … `swarm`. Say which you chose."** It conflicts with the global "Keep trivial work local; otherwise delegate at your discretion". It costs a decision and a sentence on every turn, and swarm is not installed for Gemini (homelab workstation.md:129, `AGY_SKIP`), although AGY.md carries the same line. Change it to "Independent parts worth running at once: `swarm`."
3. **Lines 10-14, ship and autopilot-full.** The global "Merge authority" paragraph already says "`ship` and `autopilot-full` merge only on explicit words". The routing line is required by the checker (it must say "explicit"), so keep it. Drop the duplicate in homelab's global text instead.
4. **The `tdd` clause on line 27, "also `tdd`".** It goes with the merge.
5. **"Nothing narrower fits: `figure-it-out`" (lines 33-34).** It goes with the merge.
6. **The formal-verification bullet (lines 37-39).** It becomes one name.
7. **"Only when named".** It loses `ketchup-video`, `recall` and `reflect`.
8. **"Editing .ts or .tsx: `typescript-best-practices`".** It is correctly narrower than the skill's description ("for reading or editing"), yet 40% of its loads (151 threads) were in review threads. Make the description say "editing", or accept that reviewers read it. Reviewers arguably benefit, so this is low priority.
9. **`benchmark-checklist`.** 100 of its 280 threads were reviews ($1.45). The broad trigger ("any timing number… limit") was a deliberate 2026-10-23 choice, made because a first measurement had become a ceiling. Keep it.

The proposed text is `G-routing-proposed.md`. It passes the checker's structural rules: casual skip, the "explicit" merge bullet, unslop and technical-writing in one docs bullet, every remaining skill once, and the "Only when named" line. Run `check-routing.py` against the real tree once the skills are renamed.

## 4. Structural

- **Link loops.** Each of these is harmless alone, but each one makes a skill load a second file:
  - create-formal ↔ maintain-formal (fixed by the merge)
  - typescript-best-practices ↔ type-system-discipline
  - build/design.md → interview → build/design.md (interview:80)
  - build/design.md → drift → build (drift:12)
  - interview → goldfish → interview (goldfish's reviewer roles are defined for interview's concept review)
  - teach → how, why (fixed by the merge)
  - interrogate → arena by step number (§1, the fragile one)
- **References that point at nothing.**
  - benchmark-checklist:38-39 points at "the **Perf issue** playbook" and "the **Hillclimb** playbook", and line 34 at "the pull-request briefing guidance". endstack has no playbooks (upstream-0b46ec3-review.md: "endstack has no mode or playbooks").
  - no-comments:9-11 and 29 point at "Comment Sicko" and "the available Comment Sicko role rules". No such role exists. Step 1's fallback names "the acceptance contract below", but the only section below is *What may stay*.
  - figure-it-out:13, "without depending on an unavailable mode or its playbooks", is a pstack leftover.
- **Reference files nobody reads.** Over the period, principle leaves were read as follows: never-block-on-the-human 0, outcome-oriented-execution 0, guard-the-context-window 2, encode-lessons-in-structure 4. encode-lessons-in-structure's job is `correct`, and never-block-on-the-human is the global "Decide for yourself… Ask only for credentials…". Delete those two leaves and point their citers at correct and at nothing (figure-it-out:23,50; show-me-your-work:53). Fold outcome-oriented-execution into migrate-callers-then-delete-legacy-apis, which has the same rule: no throwaway compatibility state. That is an index-level change. The other auditors own the wording of the leaves.
- **Descriptions that trigger wrongly.**
  - `how`: "where a change belongs" invites builders into a worker-spawning explainer. Drop that phrase after the teach merge.
  - `typescript-best-practices`: "reading or editing" (above).
  - The rest match their routes.
- **ROUTING copies.** AGENTS.md here says the homelab copy is `agents/AGENTS.md`. There is a second copy in `agents/AGY.md` (line 14). Name both in AGENTS.md "Routing", or the Gemini copy drifts.
- **Usage report bug.** `report.md` files loads from a non-installed path under `other`, so test-design (38 threads), sharpen (14) and goldfish (5) look unused. Fix the classifier, matching on the skill name against `skills/`, before the 2026-12-20 re-measure.
