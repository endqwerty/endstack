# Audit F: drift, orchestrate, principles index

Bytes: drift 3654, orchestrate 5976, principles/SKILL.md 5885 (agents/openai.yaml 43 each, untouched).

Provenance notes. `drift` is an endstack skill adapted from EGM's `egm-drift-report` (2db953f, 2026-11-17; evidence docs/egm-port.md case 5 and docs/import-notes/egm.md). `orchestrate` was ported from pstack's `poteto-mode/playbooks/orchestrate.md` at de8ee15 (0822db5, 2026-11-10; docs/new-skills-de8ee15.md, docs/import-notes/W8.md). Upstream has since deleted that playbook, so there is no upstream to track; the text is now only endstack's. The `principles` index is upstream's router restated (026a4d6), regrouped in 1712c13.

## drift

Evidence for the whole skill: docs/egm-port.md case 5, one run per arm on one model. OLD: "I would give each doc to a fresh read-only goldfish" -> Partial (no scenario-by-scenario check). NEW: "I would choose `drift` ..." / "recommend changing the doc for intended changes, the code for supported bugs" -> Pass. Only two things are tested: the skill gets chosen, and the side-to-change rule is applied. The report format, categories, run-the-check and weekly cadence are untested.

| file:line | quote | origin | duplicates | verdict |
|---|---|---|---|---|
| drift/SKILL.md:9-12 | "A design doc is its feature's spec record ... Code changes without the doc, and the doc goes stale with nothing to say so." | 2db953f | build's design-doc section states the spec-record role | shorten to one sentence (the "goes stale" motivation is wording, not a rule); keep "It reports; fixes go through build" |
| :14-17 | "Periodic passes ... (weekly while it is active)" | 2db953f, no evidence | ROUTING.md already routes "check design docs against code" | drop the "When" section; the cadence is unproven and the trigger lives in ROUTING and the description |
| :21-23 | "skip interview briefs (`*.brief.md`)" | 2db953f; briefs are deleted at reconcile (CHANGELOG 2026-11-17) | interview skill deletes the brief | keep, short; it is the only place drift learns the suffix |
| :22-23 | "Take one doc at a time, in order, and read the current files each time, never memory." | EGM "one doc at a time from current files" | none | shorten to "one doc at a time, from current files" |
| :27-29 | "Open questions and alternatives turned down are not claims." | 2db953f | none | keep, changes what gets reported |
| :33-35 | "note the link the doc should carry so the next pass is cheaper" | EGM | none | keep, one clause |
| :37-38 | "does it assert the scenario rather than something weaker that could pass while the scenario is false?" | 2db953f | also the "Broken check" bullet at :53-54 says the same | shorten: state once, drop from one of the two places |
| :39-41 | "Run it when it is local, read-only and cheap ... A check you could not run is `not run` with the reason, never a pass." | 2db953f | verify has the same "unrun is not a pass" rule | shorten to the first sentence plus "unrun is not a pass" (keep the short rule, drop the quoted token `not run`, which only fixes wording) |
| :42-43 | "including its edge and failure cases" | 2db953f | none | keep |
| :45-47 | "Report only differences; what matches is not listed." | EGM | repeated by "or 'No drift'" at :84 | keep once |
| :49-59 | seven category bullets | EGM four (missing, incomplete shape, shortcut, divergent) plus three endstack additions (changed, broken check, unspecified) | Missing/Changed/Incomplete/Shortcut/Divergent are one idea: the code differs from the doc | shorten: merge to Missing or changed behaviour, Incomplete shape or shortcut, Divergent design, Broken check, Unspecified behaviour. Category labels only name the report; the rule is "report each way they differ". Saves about 300 B |
| :61-62 | "A doc with no scenarios ... is reported as not checkable, not as clean." | 2db953f; no dry-run | none | keep, it blocks a false "No drift" |
| :64-77 | doc / code / user decision order | egm-port.md case 5 (Pass) | none | keep, tested and the skill's main addition over EGM |
| :76-77 | "Ask one question at a time, or list it as open when the user is not there." | 2db953f | global rules: "Ask only for credentials ... Ask once in one message"; interview skill asks one at a time | shorten to "ask the user, or list it as open when absent". The one-at-a-time clause conflicts with the global "ask once in one message" |
| :79-86 | Report: "One section per doc ... Write it to a dated file outside the tree unless the project names a place ... doc-only fixes together, each code bug separately." | 2db953f | global rules: no report .md in tree is generic; build covers one change per commit | shorten: keep one-section-per-doc and the quoted evidence fields; drop "dated file outside the tree" (delivery detail) and the final fix-splitting sentence (build covers it) |

Estimate: drop "When" (about 250 B), merge categories (about 300 B), compress prose and Report (about 350 B). After: about 2,750 B (save about 900 B). No reference files.

## orchestrate

Evidence: docs/new-skills-de8ee15.md. Result at lines 276 and 294: "observed uplift on authority, coordinator/owner roles and pilot sequencing ... No uplift claimed on those shared delivery requirements"; the early-question batch occurs before kickoff and unanswered defaults are used. Everything else rests on the pstack playbook's judgment, not on a dry run. Skill is explicit-only (ROUTING "Only when named").

| file:line | quote | origin | duplicates | verdict |
|---|---|---|---|---|
| orchestrate/SKILL.md:9-13 | "You run the program, never the code. ... [Autopilot-full] handles a bounded queue ... [swarm] handles parallel independent parts" | 0822db5, W8 | description already says "multi-day program"; autopilot-full and swarm own their scope | shorten: cut the autopilot-full/swarm contrast sentence (about 200 B); "never the code" is repeated at :31, :53 and :54 |
| :15-18 | "Keep goals, checks, ... in a durable notes file ... trail through show-me-your-work ... On pickup, read those records and reconcile live work before launching replacements." | W8 | show-me-your-work covers the trail; global "Record facts in files" | shorten: keep notes file and the pickup reconcile; drop the list of eleven item names to "state needed to resume" |
| :19-21 | "Use event subscriptions ... Do not build orchestration scripts, run polling loops or relay routine status" | W8, no evidence | repeated by :66-67 "Message a worker only ... never to check on it" and :86 "Do not wake workers for status" | shorten: say no polling or status relay once; drop the other two |
| :21 | "Unavailable delegation is a blocker; do not code yourself." | W8 | "never the code" at :9, :31, :53 | drop the second clause (duplicate) |
| :25-31 | landing authority, "Nothing waits for the user's approval to merge ... You never merge or edit code." | 0822db5; Daniel's instruction, CHANGELOG 2026-11-10 | autopilot-full, ship's gates, global merge rules | keep (user-granted authority, tested), but the last sentence "You never merge or edit code." repeats :9; cut |
| :33-38 | "Ask all known questions early in one message, with stated defaults ... Mid-program ask only for a genuinely new such decision" | W8; tested (new-skills-de8ee15.md:294) | global "Ask once in one message"; repeated at :93-94 "Ask only for a real decision or blocker under the early-question rule" | keep :33-38, drop :93-94 first sentence |
| :40-42 | "Explicit 'don't merge' or 'I'll land it' ... Authority excludes deployment, destructive operations and work outside the program. Planning/help explains without executing." | W8 | global rules cover destructive actions and merge authority | keep the no-merge stop; "Planning/help explains without executing" is generic, drop; destructive/deploy exclusion shortened |
| :44-46 | "Owners compose build, babysit, verify. Use swarm for independent parts; delegation never expands authority." | W8 | ROUTING swarm line; global "Delegating" | shorten: keep the three links, drop the swarm sentence and "delegation never expands authority" (the exclusions at :41 already say it) |
| :50-54 | one owner per PR, only writer, "Closing or retargeting a base can orphan children and needs your call" | W8, upstream | none | keep; "You never author or edit code. Give conflicts ... to owners" is the fourth statement of the same rule, cut |
| :55-60 | fresh worker, self-contained kickoff, "Model, effort and speed choice follow the user's routing rules." | W8 | global "Delegating" owns routing | drop the model/effort clause (global rule); keep rest |
| :61-64 | sub-coordinators, "Stop at three levels", "about ten workers in flight" | W8 | none | keep; numbers are upstream judgment, unproven here. Mark as limits to revisit before 1.0 |
| :65-67 | state-preserving delegation, "Message a worker only for a follow-up" | W8 | global delegating says children message directly | keep first, shorten second |
| :68-70 | "Each PR gets a fresh read-only verifier ... different provider or model family if available ... Green checks alone never authorize landing." | W8 | global "Check the work": two other providers verify; verify skill | drop the provider/family clause and revision rules (global + verify own both); keep "green checks alone never authorize landing" |
| :71-73 | "Start with one unit through ... before fan-out" | W8; tested (pilot sequencing uplift) | none | keep; shorten the trailing justification |
| :77-80 | kickoff contents list | W8 | goldfish/handoff-style briefs; global "Give task, paths, ownership and completion criteria" | shorten to "goal, paths, branch ownership, forbidden actions, completion evidence" (global already lists most) |
| :81-82 | "Read the diff or artifact, not only the summary. Apply verify when revisions change; a type check alone is insufficient. Sample sub-coordinator kickoffs" | W8 | verify | drop "Apply verify ..." clause; keep read-the-diff and sampling |
| :83-84 | "Send back work that drifts ... park the rest as follow-ups." | W8 | build's scope rule | keep, short |
| :85-86 | "Check every PR's live state ... Account for each worker ..." | W8 | none | keep |
| :87-92 | stalled workers, retry by cause, "After two retries drop the unit and replan" | W8 | none | keep; "a different suitable model ... under routing rules" duplicates global, cut |
| :93-95 | ask only for real blockers; "Rebase mechanics, retries, flaky checks and review triage stay with owners" | W8 | babysit | drop the first sentence (duplicate); keep the owner list |
| :97-101 | Reply: "Distinguish merge-ready work from landed work. Link notes and trail. Report unavailable evidence as unknown." | W8 | global "Link every issue and PR", pull-request-standalone rule; reply wording only | shorten to one sentence: what landed against the goal, live state and verdict per PR, drops, waiting decisions. Drop "Link notes and trail" and "unknown" (wording) |

Estimate: after cuts about 4,700 B (save about 1,250 B). No reference files. Recommend noting in the skill's import note that the pstack source is gone, so future edits do not need to track upstream.

## principles (index only)

Evidence: docs/principle-citations.md dry run 2026-10-12. With the "name each principle" rule plus build/tdd cites: replies named the principle with its choice 4 of 4 against 0 of 4; code shape did not change (both arms chose one state field and fixed the cause in both methods). So the naming rule changes reply wording and the reading behaviour, not the code. Later docs/principles-short-runs measured shortening the reference bodies; the index was not part of that test.

| file:line | quote | origin | duplicates | verdict |
|---|---|---|---|---|
| principles/SKILL.md:9 | "Read this whole index before ... each entry says when the principle applies and states its rule. When one applies, read its reference before the step it governs; do not preload the references." | 026a4d6 (upstream) | build bullet ("read a principle before the step it governs") and tdd step; global rules "Skill routing" cover opening the skill | keep the read-before-the-step rule (the tested one: "A link alone is not followed; an instruction to read is."). Shorten: drop "each entry says when ... states its rule" |
| :11 | "In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose reference you read this session." | 1712c13; evidence 4 of 4 vs 0 of 4 | build and tdd repeat it ("reports each one that changed a choice", "The reply names each principle that changed a choice"); global rules require "say which skill shaped a decision" | shorten or move: this is reply wording only, with no change in code in the dry run. Keep one copy (here) and delete from build and tdd, or drop it entirely. The "cite only if read" half prevents invented citations (no reply cited an unread principle in the test, so the guard was never exercised) |
| :13, :26, :35, :43, :48 | group headings Core, Architecture, Verification, Delegation, Meta | 1712c13 restored upstream groups | none | keep; they are the lookup structure (about 70 B) |
| :15-24 | Core entries: "when ... . rule" two-part lines | 026a4d6 | each repeats the rule that the reference body already states | shorten: keep the trigger clause only for entries whose title is not self-explanatory; the rule sentence duplicates the first line of the reference (about 40 B per entry, 1 KB across 23). Reading the reference is the instruction, so the index only needs the trigger |
| :41 | "Prove It Works is the verify skill." | 1712c13 | ROUTING.md routes verify | drop (verify is already routed; this line points to a skill that is not a principle) |
| :37 | Fix Root Causes: "A guard is a fix only when the state it handles is legitimate." | newer than 79f2b56 revert? the line survived, see git blame | fix-root-causes.md | check against upstream; if this is an endstack addition it contradicts the "take upstream verbatim" change |
| :40 | Explain the Number | upstream | benchmark-checklist skill is routed for timing numbers | keep; different scope (any number) |
| :45-46, :49-50 | Guard the Context Window, Never Block on the Human, Encode Lessons in Structure | upstream | global rules: "Own the work end to end", `correct` skill, "Record facts in files" | candidates for drop as already covered by always-loaded global rules: Never Block on the Human (global "Decide for yourself ... Leave no ... for Daniel"), Encode Lessons in Structure (`correct`). This is an index-only decision; reference files were out of scope, and removing an entry means removing its reference |

Estimate: current 5885 B. After shortening the intro, trimming the rule half of each entry for the self-explanatory ones, and dropping the Prove It Works line: about 4,800 B. Dropping the two global-duplicate entries would save another about 500 B. No reference files assessed per brief.

## Most notable

1. `orchestrate` states "the coordinator never edits code" four times and the early-question rule twice; cutting repeats and global-duplicated routing/provider rules saves about 1.2 KB with no loss of tested behaviour. The skill's source (pstack playbook) is deleted upstream, so there is nothing to keep in sync.
2. `drift`: only the doc/code/user decision rule has dry-run evidence (docs/egm-port.md case 5, one run); the "weekly" cadence, report-file location and seven-way category list are unproven. Its "ask one question at a time" conflicts with the global "ask once in one message".
3. `principles` naming rule: the only measured effect is on reply wording (4 of 4 vs 0 of 4); code did not change. It is repeated in build and tdd. The index also names `Prove It Works` (verify, already in ROUTING) and entries that global rules already cover.
