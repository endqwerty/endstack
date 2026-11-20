# Audit E: test-design, interview, goldfish

Read-only. Repo: endstack worktree. Always-loaded context read first (AGENTS.md, ROUTING.md, global CLAUDE.md).

Caveat on the brief: `goldfish` and `interview` are not purely endstack-written. Commit 2db953f (2026-11-17) ported Google's EGM into them (docs/egm-port.md, docs/import-notes/egm.md). docs/egm-port.md says of EGM's numbers: "Most numbers have no stated reason (eight reviewers, five rounds, two instances per reviewer) and no recorded measurements", and of the port: "A full design-doc review now starts at least eight reviewer runs plus merging workers ... That cost is not measured yet". The dry runs there test only that the model reads the text as intended (OLD arm fails by construction because it lacks the stage, brief or skill). They show no outcome difference.

Evidence key:
- TD = docs/test-design.md (one dry run per arm, Sonnet 5.5, one fixture; "both arms chose the unit layer").
- LM = docs/landmines-lessons.md (flaky task: "shows little uplift").
- IG = docs/interview-goldfish.md (4 cases, codex, one sample each).
- EGM = docs/egm-port.md (7 cases, one sample each).

---

## test-design (5,711 B)

First commit for all rules unless noted: `8e90caf 2026-11-16 Add test-design` (source: Daniel's Mainworthy complaints 2026-10-25..11-16, TD "Why": too many tests, e2e reach, non-actionable tests, duplicates).

| # | Rule (file:line) | Origin / evidence | Duplicates | Verdict |
|---|---|---|---|---|
| 1 | L9 "Proving a change and keeping a test are separate decisions." | 8e90caf; TD review finding | tdd SKILL step 7 ("It has proved the fix; joining the suite is a separate call"); build design.md step 8 | shorten: say it once; tdd already carries it |
| 2 | L11 "Read the project's testing guide ... it wins where it is more specific" | 8e90caf; TD "Why": guide had the rules but agents met them late | AGENTS-level "project rules first" (global CLAUDE.md, Merge authority) | shorten to "Read the project's testing guide first" (the "wins" clause is the general precedence rule) |
| 3 | L15 "If nothing reaches that state yet, write no test. If you cannot say who acts on the failure and what they would do, write no test." | 8e90caf; TD dry run "With" dropped tests that pass on base | L36 keep-condition "its failure is actionable" says it again | shorten: one sentence; delete the L36 repeat |
| 4 | L16 "Find the existing holder ... Search by what it observes" | 8e90caf; Daniel's duplicate-test complaint. TD fixture could not test it ("A layer-choice difference needs a larger repository") | L36 "no other kept test catches the same fault"; L43 "whose fact a cheaper kept test holds" | keep (the core duplicate-test rule), delete the two restatements |
| 5 | L17 "Make the code cheap to check ... move the decision into a pure function" | 8e90caf; no dry run | principles skill (structure) covers separation generally | drop: unproven, scope-qualified into mush ("when the change's scope allows ... note the extraction as follow-up") |
| 6 | L18-22 layer menu (unit / operation against real store / server test starts process once / browser only for engine) | 8e90caf; TD: dry run "separates the arms on proof and keep discipline, not on layer choice" | project testing guides (L11 already defers to them) | shorten to the one load-bearing line (cheapest layer; a browser only for what needs its engine, one journey per flow). The storage/process bullets are Mainworthy's guide restated |
| 7 | L23 "Prefer an invariant ... generated histories" | 8e90caf; no run | none | drop: property testing is project-specific and unmeasured; "write an example when..." hedge shows it is marginal |
| 8 | L24 "Place it by cost ... every change, daily, or only when its code changes" | 8e90caf; no run | L44 scale checks; L53 report "time added" | shorten: merge into layer step as one clause |
| 9 | L28 link to test-behavior-not-implementation | 8e90caf | L35 and L36 reproduce that principle's two edits (break, change internals) | keep the link; drop the restatement at L35 second sentence and L36 parenthetical |
| 10 | L29 "The title states the promise; a failure shows expected and actual in the user's terms" | 8e90caf; no run | none | drop: affects test wording, not whether a test exists or survives; unproven |
| 11 | L30 "No sleeps, wall-clock deadlines, fixed ports, shared directories or order dependence. A test that fails only beside others shares something..." | 8e90caf; global rules ("Fix tests needing quiet, fixed ports or wall-clock limits") | global CLAUDE.md Delegating section (fixed ports, wall-clock); tdd "depends on timing or unrelated global state" | keep, but delete the second sentence (restates the flaky rule at L42) |
| 12 | L31 "Wait on a signal, not a deadline ... Polling a recorder or spy until a timeout fails under load. To move time, use the framework's fake clock." | `b6ff55d 2026-11-17 Take three lessons from landmines`; LM | L30 "no sleeps, wall-clock deadlines"; L42 "(wait on the signal instead)" | shorten: LM flaky task: "Every run read test-design and ended on join()" and "one sample cannot say whether the new wording caused that". Keep fake-clock half-sentence; fold into L30. Third mention at L42 goes |
| 13 | L35 "must fail without the change for the intended reason, not because a symbol is missing" | 8e90caf; TD: "Without ... did not run the tests against the old code" vs "With ... ran them on the old code first". Only rule with a measured uplift | global CLAUDE.md ("for bugs watch one fail first"); tdd step 4 | keep (only measured effect) but cut to one sentence; mark tdd step 4 as the home for bug fixes |
| 14 | L36 five keep conditions | 8e90caf; TD review fixed contradictions | tdd step 7 points here; build design.md step 8 restates a shorter keep rule | keep (canonical list). Remove duplicated clauses (actionable, other kept test, principle's edits) so it reads as 3 conditions |
| 15 | L37 Drop rules incl. migration exception | 8e90caf; TD review ("One-time scripts lost the migration exception; it is back") | build design.md step 8 end repeats it nearly verbatim | keep here; replace the build copy with a pointer (outside my scope, flagging) |
| 16 | L38 how a dropped proof leaves | 8e90caf; TD review ("first draft ... contradicted tdd") | tdd Final Response; sequence-verifiable-units principle; build design.md step 8 | keep one sentence, point to sequence-verifiable-units |
| 17 | L42 flaky = defect; "Retrying it or raising its timeout hides the defect" | 8e90caf sentence on flakiness; retry/timeout clause added b6ff55d; LM "little uplift", only Claude/N added a timeout and removed it on review | tdd Guardrails ("If the bug is flaky, make the test deterministic"); global CLAUDE.md ("Never queue loops...", fix tests needing quiet) | shorten: keep "no retries or longer timeouts; fix the cause"; drop "With no cause found, delete it or move it to a schedule" and the security-boundary carve-out (unproven; contradicts "delete is normal") |
| 18 | L43 "Deleting is normal ... name the holder" | 8e90caf; Daniel's prune complaint | L37 drop rules | keep one sentence |
| 19 | L43 "When reading cannot tell which overlapping tests matter, measure: make small edits to the code ... smallest set that still fails on every edit" | 8e90caf; no run | none | drop: manual mutation testing, unproven, expensive for an agent |
| 20 | L44 "Scale checks to what a failure costs. Production paths and stored data get the strongest checks. Internal tooling gets a proof, not a kept test" | 8e90caf; no run | global CLAUDE.md "Check the work" (scale to risk), verify skill | shorten to the internal-tooling line (the only non-obvious part) |
| 21 | L46-53 Report (four bullets) | 8e90caf; TD dry run: "With" produced the report | tdd Final Response bullets 1, 2, 3 and 5 overlap; global CLAUDE.md "Pull requests stand alone" ("Each check with its deciding lines quoted") | shorten: keep only "dropped tests with holder/reason/commit" and "time added"; the proof and kept-test bullets are in the PR rules and tdd |

Bytes: current 5,711. After drops/shortens (rows 1-3, 5-8, 10-12, 14, 17, 19-21): about 4,000. Reference files: none.

---

## interview (4,324 B)

Origins: `678d9c4 2026-11-13 Add interview and goldfish` (IG), `2db953f 2026-11-17 Port EGM's staged goldfish review...` (EGM, brief, concept review, reconcile).

| # | Rule | Origin / evidence | Duplicates | Verdict |
|---|---|---|---|---|
| 1 | L9-12 "A feature's design rests on judgment only the user holds ... Asking for it after the code exists is too late." | 678d9c4 | description (L3) says the same | drop: description already states it |
| 2 | L16-19 When: "Not for a bug with a clear fix, a mechanical change, a chore ... or when the user opts out." | 678d9c4; IG case 2 guard: "OLD ... Pass", "NEW ... Pass". Both arms already skipped the interview, so the exclusion list changed nothing | ROUTING.md ("`interview` first for a feature shaped by the user's intent or taste"); ROUTING.md preamble covers opt-outs; build design.md "Before" bullet | shorten to one line; the exclusions are the routing line's own scope |
| 3 | L23-26 Ground: read docs and code; tell the user how you understand the system | 678d9c4; no run | build design.md step 2 Ground; `how` skill | shorten: keep the "tell the user your understanding so they can correct it" (not elsewhere), drop the read-the-code half |
| 4 | L30-33 "one question at a time, the one that would change the design most first ... why it matters and the answer you would assume" | 678d9c4 (assume-answer); 2db953f (one at a time). EGM case 1: "OLD ... Fail: batch"; "NEW ... Pass". IG case 1 shows assumed answer line | none | keep (measured against OLD; core job) |
| 5 | L34-36 "Challenge assumptions. Name edges the user has not covered: failure, scale, who else uses it..." | 678d9c4; no run | goldfish-prompt critic/ design-critic cover the same edges later | shorten to one line |
| 6 | L36-38 "Disagree when the evidence says so ... If you notice yourself praising, ask a harder question instead." | 678d9c4; egm notes say "agreeing is not help" replaced EGM's tone charter | unslop; goldfish-prompt L58 "Agreeing with the document is not help" | shorten: keep "disagree, show the evidence"; drop the praising sentence (wording only) |
| 7 | L38-39 "When an answer looks weak, ask why. When you are unsure of a fact, read the file rather than guess." | 678d9c4 | global agent behaviour; step 1 already says read the files | drop |
| 8 | L41 Stop when user says so or answers stop changing the design | 678d9c4 | none | keep |
| 9 | L43-46 How done is judged -> scenarios and checks | f4024af 2026-11-16 (design docs carry behaviour scenarios); docs/design-doc-specs.md | build design.md Behaviour section requires scenarios with named checks | keep (the only place the user is asked this) |
| 10 | L48-60 Brief file with five sections, "credited to whoever turned it down", "The design doc copies these, adding options turned down later, such as architect's sketches" | 2db953f; EGM cases 1 and 2 (OLD no brief) | standards.md L16-19 (credit rule); build design.md Alternatives; L75-76 repeats "Each option turned down ... goes into the brief" | shorten: the credit rule and "design doc copies these" live in standards/build; keep the five section names |
| 11 | L62-68 seven concept reviewers, show "two or three strongest objections", settle each one at a time "until no objection would change the design" | 2db953f; EGM case 1 only shows the text is read ("I'll write the interview brief, then have a separate merging worker run all seven"). Cost "not measured yet" | goldfish reviewers.md Merging worker (L190-192) restates the seven-role fan-out | shorten: keep one concept review with a reviewer count taken from reviewers.md, not repeated; this is the costly, unmeasured step (seven runs per feature) and the best candidate to cut to the 2-3 roles whose concept mode is distinct (zoom-out, comprehension, design critic) |
| 12 | L70-76 "You propose the first design ... Proposing first shows whether you understood" | 678d9c4; egm notes: "keeps endstack's evidence that proposing first exposes misunderstanding". No isolated run | L75-76 repeat | keep (core), shorten the pseudocode/diagram clause |
| 13 | L78-89 write doc, reconcile with brief, user decides each contradiction, delete brief | 2db953f; EGM case 2: OLD "keeps both files", NEW "quote both ... delete the brief" | build design.md steps | keep reconcile + delete |
| 14 | L87-89 "test the doc with goldfish before implementation starts; an answer the user gave only in chat goes into the doc" | 678d9c4 / 2db953f | build design.md ("tested with goldfish before the first production edit", IG "What changed"); goldfish L25-27 and L99-102 ("answer goes into the document") | drop both clauses |
| 15 | L91-97 Without the user: assume answers, write under open questions, name them in the PR | 678d9c4; IG case 3: "OLD ... Fail: blocks on the parent"; "NEW ... Pass" | goldfish Escalate (L99-102) records open questions the same way | keep (measured); goldfish can point here |

Bytes: current 4,324. After drops (rows 1, 2, 3, 5, 6, 7, 10, 11, 12, 14): about 3,000. No reference files.

---

## goldfish (SKILL 5,561 B; references 14,540 B)

Origins: `678d9c4 2026-11-13` (agent-file passes, IG), `2db953f 2026-11-17` (stages, reviewers, loops, resolve; EGM). IG results: cases 1, 3, 4 pass NEW; EGM results: cases 3, 4, 5, 7.

### SKILL.md

| # | Rule | Origin / evidence | Duplicates | Verdict |
|---|---|---|---|---|
| 1 | L9-13 goldfish "gets only the document's paths and the files the document references, never the conversation, your conclusions or the answers" | 678d9c4; IG case 4: OLD "treat as review ... verify" Fail, NEW "withholding this conversation" Pass | goldfish-prompt L3-4 ("no conversation, no summary of the document") | keep in SKILL; delete the prompt's repeat |
| 2 | L15-21 When: includes "periodic passes over a project" | 678d9c4; IG: run on 6 projects 2026-11-13 | ROUTING.md ("`goldfish` to test a design doc or agent rules on a fresh agent") | shorten to two bullets |
| 3 | L25-27 "You never answer a goldfish in chat; an answer goes into the document or it does not exist." | 678d9c4/2db953f | L99-102 Escalate ("Either way the answer goes into the document"); interview L88-89 | keep once (here), drop at Escalate |
| 4 | L28-31 different model family if available; "Each stage and round gets new ones; a goldfish that has seen an earlier draft is no longer a goldfish" | 678d9c4 | L73 Loops ("repeat with new reviewers"); L78-79; global CLAUDE.md verifier-provider rules | shorten: keep new-reader-each-round once |
| 5 | L32-36 Merging worker paragraph | 2db953f; EGM "retry-once, `not run`"; cost "not measured" | reviewers.md L163-192 describes it in full | shorten to one pointer line |
| 6 | L38-41 cannot start workers: hand off or report untested | 678d9c4 fix after IG case 3 ("NEW said that without separate workers it would stop"); "Not re-run after that wording change" | none | keep (fixed a measured failure) |
| 7 | L43-49 agent instruction files: one goldfish, three passes, realistic tasks, cut candidates | 678d9c4; IG "One goldfish per pass in every case" turned down; EGM case 7 NEW "keep the initial review with one fresh reader" Pass | goldfish-prompt L26-43 and reviewers.md "Implementation readiness" repeat the readiness-task spec | keep; shorten readiness sentence (stated in the prompt) |
| 8 | L51-69 five stages incl. stage 4 "Zoom out again ... not reopening what stage 1 settled" | 2db953f; EGM case 3 shows read-as-written only | stage 1 and 4 run the same role; EGM: "no recorded measurements" | shorten: drop stage 4 (a second pass of the stage-1 reviewer, no evidence it finds anything the readiness loop would not). Stage 1 + comprehension + critic loop + readiness loop remain |
| 9 | L71-86 Loops: clean round, "Converged is two clean rounds", settled/reopened findings, "Stop at five rounds, or on churn" | 2db953f; EGM egm-port.md names the reason for two clean rounds ("fresh reviewers sample differently"); case 4: OLD "one clean round ends the loop" Fail, NEW Pass | none | keep two-clean-rounds and settled/reopened; shorten five-round cap and churn: reason for 5 is none ("no stated reason"), "churn" definition and the ask-the-user branch are long for a case never observed |
| 10 | L88-93 ranks defined (blocker, should, nit) | 2db953f; ranks shared with verify | goldfish-prompt L50-53 defines the same three ranks | keep one (prompt, since reviewers read it); SKILL refers to it |
| 11 | L95-98 Contest: "'This was intentional' is not evidence. You wrote the document; wanting to contest is not proof." | 2db953f | EGM resolve rule | shorten: second sentence says the first again |
| 12 | L99-103 Escalate | 2db953f | interview "Without the user" (open questions); L25-27 | shorten: drop the answer-goes-in-the-doc tail and point to interview |
| 13 | L105 "Never contest a comprehension gap" | 2db953f; EGM case 4: OLD "dismiss the finding" Fail, NEW "treat ... as Fix" Pass | none | keep (measured) |
| 14 | L105-106 "Never change a rank; contest it instead" | 2db953f (EGM resolve) | none | drop: no endstack failure behind it, no run; the author can already contest the finding |
| 15 | L106-108 "Prefer cutting and reordering to adding" | 678d9c4 | goldfish-prompt L55 ("Prefer cutting or moving text to adding it") | keep once, in the prompt (reviewer-facing); drop here |
| 16 | L108-109 "A rule that keeps being missed belongs in a check, not more prose (correct)" | 678d9c4 | ROUTING.md `correct` route; AGENTS.md "Deterministic work belongs in the homelab CLI" | drop |
| 17 | L111-115 Report list | 2db953f | global CLAUDE.md PR rules ("each verifier's provider and model, findings, unchecked scope") | shorten to one line or drop; reports go to the PR, already specified |

SKILL bytes: 5,561 -> about 4,000.

### references/reviewers.md (9,211 B)

| # | Rule | Origin / evidence | Duplicates | Verdict |
|---|---|---|---|---|
| 1 | L10-12 "A role has two modes. Review ... Concept ..." and all seven Concept bullets | 2db953f; cost "not measured yet" (egm-port.md) | interview L62-68 (the only caller) | shorten: Concept mode is only used by interview and costs seven runs; keep for 3 roles or drop; unproven |
| 2 | L29-73 Design pattern role + 10-pattern catalog with costs | 2db953f; egm-port.md "the separate design-pattern reviewer (EGM expects that merging it into the critic would give conflicting directions)" — an EGM expectation, not an endstack measurement | principles / architect skills (alternatives, trade-offs) | drop the catalog (about 1,900 B); keep the role as three sentences incl. "No false compromise detected" exit. Whole role is a candidate to remove |
| 3 | L119-129 Style role (hyperbole, buzzwords, filler, synonyms) | 2db953f | unslop and technical-writing (egm notes: tone charter "dropped ... unslop covers them"); ROUTING.md prose route | drop the hyperbole list; keep only the DROP/CALIBRATE/RELOCATE/KEEP caveat classification |
| 4 | L108-117 Structure role: heading nesting, tables, links resolve | 2db953f | AGENTS.md "Deterministic work belongs in the homelab CLI ... not a skill"; scripts/check-skills.py already checks links | drop: mechanical check an LLM reviewer should not carry |
| 5 | L146-161 Codebase details role | 2db953f | `drift` skill (checks doc against code, scenario by scenario); goldfish-prompt critic L33-37 ("Check claims against the referenced files") | shorten: overlap with critic pass and drift; keep the "contradiction is a blocker" line only |
| 6 | L131-144 Implementation readiness role (task steps) | 2db953f | goldfish-prompt L38-43 readiness pass (same tasks, steps, questions, guesses); standards.md L33-34 (zero decisions) | shorten: the last sentence of the role repeats the prompt |
| 7 | L14-27 Zoom out role | 2db953f | standards.md Zoom out (L41-64) near-verbatim: speculative features, caching before bottleneck, altitude, search existing utility | merge with standards (see below) |
| 8 | L163-192 Merging worker, "two independent instances of each reviewer" | 2db953f; EGM "two instances per reviewer" has no stated reason | SKILL L32-36 | drop the two-instance sentence; keep retry-once, `not run`, template; the template is load-bearing |

reviewers.md bytes: 9,211 -> about 5,500 (catalog 1,900, structure 450, style list 400, concept bullets 700, merge overlap 250).

### references/standards.md (3,076 B)

Whole file can go. Feature spec and Implementation readiness standards restate the roles' questions (reviewers.md L98-102, L135-141); Zoom out standard (L41-64) restates the Zoom out role and the principles/architect skills (fix-root-causes, simplicity). Unique content is small: the alternatives-credit rule (L16-19; also in interview L57) and phases (L35-36). Fold those two into the design-critic and readiness roles (about 400 B) and delete the file. Net -2,600 B and one less file every reviewer brief must name. Origin `2db953f`; no evidence beyond read-as-written.

### references/goldfish-prompt.md (2,253 B)

| Rule | Verdict |
|---|---|
| L3-4 "no conversation, no summary of the document, no hint about what you expect" | drop (SKILL L9-13 states it) |
| L50-53 rank definitions | keep (reviewer-facing, only copy after SKILL drops its own) |
| L55 "Prefer cutting or moving text to adding it" | keep (only copy) |
| L58-60 "Every gap you find makes you more useful. Agreeing ... is not help. Report a pass ... only if you looked" | keep: origin 678d9c4, anti-sycophancy for the reviewer; reasoned, short |
| L26-27 sentence on three agent-file passes vs design-doc roles | shorten (explains the template to the author, not to the goldfish) |

Bytes 2,253 -> about 1,900.

### goldfish totals
SKILL 5,561 -> ~4,000; references 14,540 -> ~7,800 (standards removed; reviewers ~5,500; prompt ~1,900... with merged standards text ~400). Whole goldfish about 20,100 -> about 11,800.

---

## Summary table

| Skill | Items flagged | Drop | Shorten | Keep | Bytes now | Bytes after |
|---|---|---|---|---|---|---|
| test-design | 21 | 5 (rows 5, 7, 10, 19, plus the L43 mutation clause) | 12 | 4 | 5,711 | ~4,000 |
| interview | 15 | 3 (rows 1, 7, 14) | 7 | 5 | 4,324 | ~3,000 |
| goldfish SKILL | 17 | 3 (rows 14, 15, 16) | 8 | 6 | 5,561 | ~4,000 |
| goldfish references | 16 | catalog, structure role, style hyperbole list, 2-instance rule, standards.md | 6 | 3 | 14,540 | ~7,800 |

Entire reference file that can go: `skills/goldfish/references/standards.md`.

## Most notable
1. goldfish's design-pattern 10-pattern catalog (about 1,900 B) and the structure/style/concept-mode machinery have only EGM's say-so; egm-port.md records "no recorded measurements" and unmeasured cost; structure checks are deterministic work that AGENTS.md says belongs in tooling.
2. standards.md restates reviewers.md (zoom out nearly verbatim; readiness and feature spec in the roles) and can be deleted.
3. test-design's flaky/signal rule appears three times (L30, L31, L42) and LM shows "little uplift"; layers, invariant, mutation-measure and make-it-pure rules have no dry run, and TD admits the fixture did not separate layer choice. The one measured effect is "watch it fail first" (L35).
