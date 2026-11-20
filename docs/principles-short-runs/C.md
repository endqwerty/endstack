# Audit C: swarm, tdd, teach, technical-writing, typescript-best-practices, unslop, why, architect

Compared endstack `skills/<name>/` against upstream pstack at 0b46ec3. Porting edits (tool/model names, links, fallbacks, frontmatter wording) are excluded. `Origin` is the first endstack-history commit that added the phrase (`git log -S`). Items 1-3 (swarm) and the tdd cuts are "older upstream text" where noted.

## swarm

Endstack-only files: `agents/openai.yaml` (porting rule, not an addition).

1. skills/swarm/SKILL.md:24 "Set N from the user or derive it from the shape. N is total workers, not the cloud concurrency limit."
   - Origin: 54b0c6e 2026-07-30 (pstack, "Add swarm skill"); carried by 8a6e905 and 026a4d6. **Older upstream text**: 0b46ec3 replaced the step with a model-pick step tied to Cursor rules.
   - Elsewhere: not in upstream 0b46ec3; not elsewhere in endstack.
   - Judgment: keep, harmless. It is a neutral replacement for upstream's removed model-pick step; the "not the cloud concurrency limit" clause is only mildly useful.
2. skills/swarm/SKILL.md:42 "Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts."
   - Origin: 54b0c6e (pstack). **Older upstream text**.
   - Elsewhere: restated by line 46 "Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts".
   - Judgment: drop. It duplicates the final-report sentence two paragraphs below.
3. skills/swarm/SKILL.md:9 "Coordinate N workers in parallel when the harness supports them. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report."
   - Origin: 026a4d6 2026-10-10 (import).
   - Elsewhere: restates the frontmatter and step 2 (slices/race/mix).
   - Judgment: drop. Redundant lead paragraph; it keeps the 2,200-ish budget busy for nothing.
4. skills/swarm/SKILL.md:30 "Specify the starting revision or branch when it differs from the default." and "respecting available concurrency"
   - Origin: 026a4d6. Tool-neutral rewrite of upstream's `cloud_base_branch` line, so mostly porting.
   - Judgment: keep (it is the port of an upstream rule).
5. skills/swarm/SKILL.md:32 "Otherwise do the work yourself in sequence and say so; this does not provide independent race arms."
   - Origin: 026a4d6. The fallback is a required porting edit. The clause "this does not provide independent race arms" is the only new meaning.
   - Judgment: keep. It stops a sequential run being reported as a race.

## tdd

Endstack-only files: `agents/openai.yaml` (porting rule). tdd is the largest divergence: 3,143 -> 5,158 bytes. Evidence docs: `docs/tdd-design-checks.md`, `docs/design-step.md`, `docs/tdd-keep-tests.md`, `docs/principle-citations.md`, `docs/test-design.md`.

1. skills/tdd/SKILL.md:15 "When a step names a principle, read that reference before doing the step."
   - Origin: 1712c13 2026-10-12 "cite principles from build and tdd".
   - Elsewhere: same line in build; upstream has it only in its poteto-mode playbooks, not in tdd.
   - Judgment: keep. 1712c13 points to docs/principle-citations.md (replies now name the principle; code the agent wrote did not change), so the evidence is weak: it changes citations, not output. Marginal, but cheap.
2. skills/tdd/SKILL.md:17 "Trace the symptom to its cause per the fix-root-causes principle." Also line 25 "Fix the cause, not a guard downstream, in every consumer listed in step 1, or say why one is exempt."
   - Origin: line 17 1712c13; line 25 f4d0d6b 2026-10-16 ("build: a design step before code").
   - Elsewhere: fix-root-causes principle and build/references/design.md:14.
   - Judgment: keep (design-step.md evidence: audit found one-client-only fixes). Line 17 pointer is duplicated by the line 25 rule; either alone would do.
3. skills/tdd/SKILL.md:18 "Find every consumer with the same fault ... Search by what the faulty code does ... List each place you find."
   - Origin: 26fcbf9 2026-10-16.
   - Elsewhere: build/references/design.md:14 (same job, pointer form).
   - Judgment: keep. docs/tdd-design-checks.md: fixed all three consumers in 7/7 runs with it, 3/7 without; a pointer to build's design step was opened in 0/5 runs.
4. skills/tdd/SKILL.md:19 "Name the shape if the fix changes a type or a state ... type-system-discipline principle."
   - Origin: 26fcbf9.
   - Elsewhere: build design step, type-system-discipline principle.
   - Judgment: keep with doubt. The same doc's table shows "with" 0 of 7 on the shape row; no measured effect. Candidate to drop.
5. skills/tdd/SKILL.md:20 "Name what the fix makes redundant ... Delete it in the fix, but not an interface callers outside the repository may use."
   - Origin: 26fcbf9; exemption added 3f88a8d.
   - Elsewhere: build design step "subtraction".
   - Judgment: keep. Rows in tdd-design-checks.md show 7/7 vs 3/7.
6. skills/tdd/SKILL.md:21 "A fix that crosses a function boundary or adds a module: read build's design step and do it."
   - Origin: 26fcbf9, reworded 3f88a8d.
   - Elsewhere: build.
   - Judgment: keep; it is the escape hatch to the full design step.
7. skills/tdd/SKILL.md:22 "test-design decides the layer and whether an existing test already holds the case."
   - Origin: 8e90caf 2026-11-16.
   - Elsewhere: test-design/SKILL.md.
   - Judgment: keep (pointer only; docs/test-design.md).
8. skills/tdd/SKILL.md:23 "for each independently faulty place found in step 1. Consumers that share one faulty implementation share one regression check"
   - Origin: 3f88a8d 2026-10-16 (review of cfa930f: 60 callers should not need 60 tests).
   - Judgment: keep; it corrects a flaw the previous addition would have caused.
9. skills/tdd/SKILL.md:23 "per the test-behavior-not-implementation principle."
   - Origin: 1712c13.
   - Elsewhere: duplicates the sentence it hangs on ("encode intended behavior, not mirror the current implementation") and the "Prefer no new test" list.
   - Judgment: drop, pure citation of a rule already stated inline.
10. skills/tdd/SKILL.md:24 "Where the history allows, commit the failing test before the fix. That is the canonical order of the sequence-verifiable-units principle."
    - Origin: 1712c13.
    - Elsewhere: sequence-verifiable-units reference; test-design keeps "history still shows red then green".
    - Judgment: keep, small. Note it conflicts a little with item 12 (dropped tests leave in a later commit) but consistently.
11. skills/tdd/SKILL.md:27 "7. Decide whether the test stays, by the keep and drop rules of test-design."
    - Origin: 47e6a6b 2026-10-31, rewritten 8e90caf.
    - Elsewhere: test-design/SKILL.md:37 owns the rules.
    - Judgment: keep. docs/tdd-keep-tests.md has a dry run.
12. skills/tdd/SKILL.md:33 **Removed** upstream text: "or would be deleted immediately after proving the fix" in the bad-test definition.
    - Origin: removal in 47e6a6b/8e90caf era (the phrase is present in c493c25 and 8a6e905 pstack text).
    - Meaning change: upstream calls such a test bad; endstack now writes it first and drops it in step 7.
    - Judgment: keep the removal; consistent with step 7 and docs/tdd-keep-tests.md.
13. skills/tdd/SKILL.md:49 "Say which new tests stay and which were dropped, why, and the commit that dropped them."
    - Origin: 47e6a6b.
    - Judgment: keep; report line for step 7.
14. skills/tdd/SKILL.md:51 "List the consumers checked for the same fault, which ones changed, and why any was left."
    - Origin: 26fcbf9. Judgment: keep (design-checks doc, 7/7 listed consumers).
15. skills/tdd/SKILL.md:52 "Name each principle that changed a choice, and the choice."
    - Origin: 1712c13. Elsewhere: build and the router rule in endstack's principles index.
    - Judgment: drop. docs/principle-citations.md shows it changed replies only, and the same final-report rule lives in build and principles; per Daniel's rules, citation theatre.

## teach

Endstack-only files: `agents/openai.yaml` only.

No additions. Differences are porting: "Run them in parallel if separate workers are available; otherwise ... in sequence and say so" (line 14) and the image-generation fallback "If image generation is unavailable, use a spatial drawing in an available medium and state the limitation" (line 17). Both added in 026a4d6 and are exactly the required fallback pattern.

## technical-writing

Endstack-only files: `agents/openai.yaml` only. Upstream 0b46ec3 has no references dir either; endstack matches upstream's shortened body (taken in 85f8272).

1. skills/technical-writing/SKILL.md:17-19 section "Keep the goal visible": "On the first task message, restate the user's goal and problem in your own words and, for a change, the smallest expected solution. Proceed without waiting for confirmation. Carry the goal into each delegated brief, the opening of the pull request's rationale, and the final report. Skip the final restatement for a fully specified one-line edit. If evidence rules out the requested change, show it and stop."
   - Origin: 0822db5 2026-11-10 (port of upstream ab1f702's poteto-mode goal reminder).
   - This is an addition and a move: upstream puts the rule in poteto-mode and `in-your-own-words`, not in technical-writing; endstack made technical-writing the single owner. The "skip the final restatement for a one-line edit" and "if evidence rules out the change, show it and stop" clauses are endstack's.
   - Elsewhere: not in any other endstack skill (only docs/upstream-de8ee15-review.md:74 and docs/import-notes/W7.md). Upstream has no equivalent in technical-writing.
   - Judgment: drop (or at least question). docs/upstream-de8ee15-review.md:132 records the dry run: "both arms preserve the goal in all four requested artifacts. No uplift." The home is also odd: a prose-style skill now carries a behavioural rule.

## typescript-best-practices

Endstack-only files: `agents/openai.yaml`. `references/patterns.md` exists upstream too.

1. skills/typescript-best-practices/SKILL.md:15 Branded types row: "Validate once at the boundary through a verifying type guard, not a cast. Respect existing validated opaque-type constructors and schema validators." Upstream: "`& { readonly __brand: "X" }` ... A brand comes from a verifying type guard (`input is AgentId`), never from `as`."
   - Origin: 47abd1b 2026-10-21 "fix: validate branded values through narrowing".
   - Meaning change: drops the literal `__brand` spelling and adds "respect existing opaque types".
   - Elsewhere: same in patterns.md:26-28; upstream already had the guard rule, so only the opaque-type clause is new.
   - Judgment: keep. It prevents introducing a second brand convention in repos that have one. No doc under docs/ backs it; the commit has no message body.
2. skills/typescript-best-practices/SKILL.md:25 row "Return types at the boundary": "Annotate the return type of exported functions and public methods ... Let local helpers and callbacks infer, except type predicates, assertion functions and recursive functions. A project's lint or convention on return types wins."
   - Origin: d121651 2026-11-17. Not in upstream.
   - Elsewhere: docs/landmines-lessons.md records it as the "middle ground" with a dry run; "both providers already follow it".
   - Judgment: drop (or fold). Its own dry run says both providers already did this without the rule, so it adds no measured behaviour. The row is the longest in the table.
3. skills/typescript-best-practices/references/patterns.md:26 "The guard delegates to the project's runtime UUID validator. Its body must verify the brand's invariant. TypeScript trusts a user-written predicate's return type ... `return true` would lie just as a cast can."
   - Origin: 47abd1b.
   - Elsewhere: partially restates SKILL.md:15.
   - Judgment: keep; the "predicate bodies are trusted" fact is what makes the rule non-obvious.
4. skills/typescript-best-practices/references/patterns.md:28 "Use the project's existing opaque-type constructor or schema validator ... The `readonly __brand` shape above is an example, not a required spelling. Don't introduce a second convention."
   - Origin: 47abd1b. Replaces upstream's "Match the `readonly __brand: 'X'` shape. Don't invent a new convention."
   - Meaning change: reverses upstream's guidance (match the brand spelling) into "match whatever the project uses".
   - Judgment: keep (consistent with item 1, but duplicates it).
5. patterns.md:36, 41: `GitDiff` renamed `Diff` in the examples. Cosmetic, not an addition.

## unslop

Endstack-only files: none (no `agents/openai.yaml`).

1. skills/unslop/SKILL.md frontmatter: upstream has `disable-model-invocation: true`; endstack removed it and made the description trigger-bearing ("Use on any prose you write before sending it").
   - Origin: 27df1e0 2026-11-11 "make unslop visible".
   - Meaning change: from explicit-only to visible-always. AGENTS.md says keep the flag where the source has it, so this is a deliberate exception.
   - Elsewhere: ROUTING.md says unslop applies to any prose; docs/hidden-skill-loads.md evidence: loaded in 4% of Claude sessions while hidden (81% Codex).
   - Judgment: keep. Fixes a recorded failure with numbers.
2. Body is byte-identical to upstream apart from frontmatter. No other additions. (The rule-numbers sentence is upstream's.)

## why

Endstack-only files: `agents/openai.yaml` only. Body identical to upstream except "PR" spelled out as "pull request" (porting/style).

No additions.

## architect

Endstack-only files: `agents/openai.yaml` only. Body identical to upstream except the arena link and the description.

No additions.

# Summary counts

- swarm: 5 items (2 older upstream text, 2 drop-leaning)
- tdd: 15 items
- technical-writing: 1
- typescript-best-practices: 4 (plus 1 cosmetic)
- unslop: 1
- teach, why, architect: no additions
- Total: 26 items; drop: 6 (swarm 2, 3; tdd 9, 15; technical-writing goal section; ts return types)
