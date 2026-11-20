# Audit A: endstack skills vs pstack 0b46ec3

Skills: arena, benchmark-checklist, bro, correct, create-formal-verification-skill, maintain-formal-verification-skill, figure-it-out, how.
Paths below are relative to the endstack worktree. Origin = first commit adding the text (`git log -S`).
Verdict key: keep / drop. Upstream HEAD checked is 0b69428 (2026-11-20); 0b46ec3 is 2026-11-19.

## arena (skills/arena/SKILL.md)

1. Convergence dissenter, line ~40 (Phase E): "If the candidates converge on one shape, do not ship it yet: shared training can make agreement a shared blind spot. Run one dissenter ..." Upstream: "that is strong agreement. Note it and ship the consensus shape." Meaning reversed.
   - Origin: 7257622 2026-10-23 "Drop unused skills, classify corrections, give panels a dissenter".
   - Elsewhere: global rules ("Decide for yourself" dissenter for choices); interrogate's copy was removed 2026-11-02. Not in upstream (upstream grep for "dissent" at 0b46ec3 finds nothing in arena).
   - Judgment: keep. docs/2026-11-02-evidence-over-dissent.md deliberately kept it for arena, citing the dry run S3 in docs/2026-10-23-learnings-dry-runs.md (runners and judge converged on the design behind a 17-minute outage). It is a single-evidence case, but it is the one dissent step with a concrete comparison against a rubric.
2. Outputs line: "the dissenter and what it changed". Same origin as 1. Keep (follows 1).
3. Phase C judge independence: upstream "judge is never from the parent's vendor ... use the first entry from another vendor" became "Use fresh context independent of the candidate authors. A different model family is optional." Meaning loosened from a hard vendor rule to fresh-context.
   - Origin: c26c20b 2026-10-27 (first version "Prefer a different model family ... otherwise say the judge is not independent"; c26c20b made it optional). Note: docs/import-notes/review-defaults.md says this aligns with the approved global definition.
   - Elsewhere: figure-it-out line 41, show-me-your-work references/audit-and-review.md:13, goldfish:28 (same phrasing).
   - Judgment: keep. Documented decision; it matches the global "fresh context" review rule. Not a port edit, it is a deliberate meaning change.
4. Phase C: "the judge ... is required" (upstream "when Phase C ran one" / "or skip the judge, and say so"). Endstack removed the skip option and the "Phase C skipped the judge" output wording; instead it falls back to applying the judge lens in sequence and disclosing.
   - Origin: 026a4d6 2026-10-10 import (fallback), reinforced in c26c20b.
   - Judgment: keep. It is the "otherwise do it yourself and say so" porting fallback, but it also drops the skip path, which is a small meaning change. Low risk.
5. Phase C timing: "It may run alongside your reading in Phase D, never while candidates are writing." Upstream: "After all Phase B candidates complete ... While you read in Phase D, the judge scores".
   - Origin: 026a4d6. Near-restatement of upstream order, "never while candidates are writing" is added emphasis. Judgment: drop-able but harmless (nit); keep as is.
6. Phase B dropout rules: "If a runner cannot start, use an available replacement only when the task and harness permit it; otherwise drop the seat and say why. Keep at least two independent candidates for a comparison unless the user specified one. If that is impossible, report the comparison incomplete."
   - Origin: 0822db5 2026-11-10 "Review upstream through de8ee15 ...". Upstream's version of this (keep at least two runners, replace a rejected slug) is in Phase A of 0b46ec3, so the floor of two is partly upstream ("keep at least two runners"). The "report the comparison incomplete" clause is new.
   - Judgment: keep. Replaces the model-slug fallback that was removed by porting; the incomplete-report clause is a small honest-failure addition.
7. Phase A.3: "the same family can fill several seats for generation-bound work" and "different model families for judgment-sensitive work if available". Upstream has the same ideas ("repeat one model when generation-bound"). Port edit, not an addition.

Endstack-only files: none beyond agents/openai.yaml (standard).

## benchmark-checklist (skills/benchmark-checklist/SKILL.md)

1. Line ~15: "Before measuring, apply [explain the number](../principles/references/explain-the-number.md): record the decision, the result that would change it, and the noise floor."
   - Origin: 0822db5 2026-11-10 (upstream review through de8ee15; W7/W8 import notes).
   - Elsewhere: skills/principles/SKILL.md lists it; upstream has principle-explain-the-number as a separate skill but 0b46ec3's benchmark-checklist does not link it with this wording ("decision, the result that would change it, noise floor" is endstack-side summary of that principle).
   - Judgment: keep. It is a link plus a pre-measurement step that the principle already holds; check that the three terms match references/explain-the-number.md (not verified here). Mild duplication, low cost.
2. Last bullet: "following the pull-request briefing guidance". Port rewrite of a link; not an addition.
3. Removed command names (top, pidstat, py-spy, strace, uptime, nproc). Port edit.

Endstack-only files: none.

## bro

No additions. Only the description changed ("plain human language" to "plain language"). Port edit.

## correct (skills/correct/SKILL.md)

Largest divergence. Upstream is 2,478 bytes; endstack is 3,771.

1. Section "First, is it a mistake?" (lines ~13-18): classify a correction as defect, preference or experiment; only defects get a guard; record preferences with how firm; give experiments an end condition; "Never freeze a first measurement or an agent's own choice into a limit"; "Before a project's 1.0, any product or technical rule may go once it stops serving".
   - Origin: 7257622 2026-10-23.
   - Elsewhere: global CLAUDE.md ("His words are a direction, not a contract") carries the same rules, loaded every turn. Not in upstream.
   - Judgment: keep the classification step (it changes what `correct` does and is the skill's defence against over-guarding), but drop the sentences that restate global rules verbatim (1.0 sentence, "never credit the user", "never freeze a first measurement"). Those are duplicated in the always-on rules.
2. "A guard taxes every later change. Add one only when the mistake recurs and costs more than the guard; a correction about wording or presentation does not justify a parser or a blocking check."
   - Origin: 7257622. Not elsewhere. Judgment: keep. It is the counterweight to upstream's "make each one impossible", and docs/2026-10-23-learnings-dry-runs.md S1/S2 followed it. Single-use evidence though.
3. Section "One rule": "When you are about to add a rule to an agent instruction file, or were just corrected, classify it first ... A rule the user asked for is still written, as one row in the rule table ... State it as a plain instruction, without the user's quotes or dates; name the user only when the rule grants authority or settles credentials, money or safety. A later user instruction may replace it."
   - Origin: a78b8b5 2026-10-16 "Lessons go into code" (heading and core); the "user asked for" line in 484dff8 2026-10-16. Later reworded in 7257622.
   - Evidence: docs/lessons-in-code.md and docs/lessons-in-code-runs/ (scored run).
   - Elsewhere: the "plain instruction, no quotes or dates, attribute only for authority/credentials/money/safety" clause is verbatim in global CLAUDE.md; the table rule is in upstream's "Keep the rule table".
   - Judgment: keep the section (it has recorded dry-run evidence and replaces upstream's "fix the mistake and add the rule"); drop the attribution sentences as duplicated global text.
4. Rule-table paragraph: "When the operator corrects you, follow One rule above." Replaces upstream "fix the mistake and add the rule". Follows 3; keep.
5. Description rewritten (drops /correct trigger and "prove each check fails" wording from the description). Port edit, though it loses "Prove each check fails on a real past mistake" from the description; body still has it.

Endstack-only files: none.

## create-formal-verification-skill (skills/create-formal-verification-skill/SKILL.md)

1. Line ~11: "An ordinary bug fix with a reproducible test belongs to [tdd](../tdd/SKILL.md), not this skill."
   - Origin: 1d964d4 2026-10-21 "Clarify formal verification routing and port evidence".
   - Elsewhere: ROUTING.md lines 27 and 38 already route bug fixes to tdd and formal checks to this skill. Not upstream.
   - Judgment: drop. Duplicated by ROUTING.md, and a skill that was already opened has been chosen.
2. Tool paragraph: "with explicit correspondence between model actions and code" (added) and the removal of "TLA+ is the default for that in any language".
   - Origin: 88cf6f4 2026-10-21. Removing TLA+ as the default is a meaning change, though TLA+ is still named in the statechart paragraph. Judgment: keep the correspondence phrase (it is also in the "what makes it good" section already, so near-duplicate; nit). The removal of the TLA+ default looks like tool-name porting; fine.
3. "Label this fallback property-based testing, not proof or formal verification."
   - Origin: 88cf6f4. Not upstream, not elsewhere. Judgment: keep. It stops a fallback being reported as verification; cheap, honesty rule, but no recorded failure behind it (W6 import notes mention it as a port clarification).
4. Final line: "This skill checks a property within stated assumptions; a scripted journey through the real app is a different job."
   - Origin: line first came with the 2026-10-21 port as a pointer to a sibling `create-verification-skill`; 7257622 2026-10-23 rewrote it after that sibling was dropped. Upstream at 0b46ec3 does not have it: older upstream text (upstream later removed the pointer). Judgment: drop. With no sibling skill it points at nothing; the opening paragraph already scopes the skill.
5. statechart paragraph: "pstack [`/statechart`]" became "the `statechart` skill"; "when the check passes it draws how the system moves". Port edit.

Endstack-only files: none.

## maintain-formal-verification-skill (skills/maintain-formal-verification-skill/SKILL.md)

1. Report section moved to references/report.md (853 bytes) with SKILL.md saying "Open the report requirements now and use them for the hand-off".
   - Origin: 88cf6f4 2026-10-21. Content of report.md is byte-for-byte the upstream "Report" section (bullets plus the "stale description" and "separate change" lines). Not an addition of substance, but a structural change that makes the report step depend on a second read.
   - Judgment: keep (SKILL.md is under 6,000 bytes at 5,835; upstream is 7,012, which exceeds the role-skill cap). Risk: an agent may skip the reference; the SKILL.md wording ("now") mitigates.
2. Intro and outcomes sentences tightened; "This is a code finding, not drift". Meaning unchanged; compression only.
3. Step 1 "find verify skills by function, not name": unchanged meaning.

Endstack-only files: skills/maintain-formal-verification-skill/references/report.md (see 1).

## figure-it-out (skills/figure-it-out/SKILL.md)

1. Line 41: "Pair delegated work with a judge in fresh context independent of the author. A different model family is optional."
   - Origin: c26c20b 2026-10-27 (first as "judge from a different model family ... otherwise say the judge is not independent" in the 026a4d6/0822db5 port). Upstream: "Pair delegated work with a judge." with no independence condition.
   - Elsewhere: arena line 28, show-me-your-work references/audit-and-review.md:13, goldfish:28.
   - Judgment: keep. Documented in docs/import-notes/review-defaults.md; it is an added requirement of independent context for judges.
2. "Give work to separate workers if the harness has them; otherwise do it yourself in sequence and say so." Porting fallback, not an addition.
3. Start: "Use the named principles as judgment guides, without depending on an unavailable mode or its playbooks." Replaces a poteto-mode instruction; port edit. Link rewrites to ../principles/references/*.md (all exist). The architect link line says "(it compares distinct design candidates)" in place of "(it runs arena)"; a port rewrite that changes nothing of meaning, though architect does use arena (CHANGELOG line 14 says it sends contested designs to arena).
4. Definition-of-done link: upstream "prove-it-works principle skill" became [verify](../verify/SKILL.md). Meaning shift (verify is the independent-check skill, not the prove-it-works principle). Judgment: nit; keep, but note it points at a heavier skill than the principle.

Endstack-only files: none.

## how (skills/how/SKILL.md)

No additions. Subagent spawn became "one read-only worker ... otherwise follow the brief yourself and say so". Port fallback. The brief text is unchanged.

Endstack-only files: none.

---

## Item count and tally

Substantive items (additions or meaning changes), counting each numbered entry above that is not purely a port edit:
- arena: 6 (1, 3, 4, 5, 6 plus output-line 2)
- benchmark-checklist: 1
- correct: 4
- create-formal-verification-skill: 4
- maintain-formal-verification-skill: 1
- figure-it-out: 2 (plus one nit)
- bro, how: 0

Total 18. Drop: 4 whole items (create-FV #1 tdd pointer, create-FV #4 journey line, arena #5 "never while writing" emphasis, and correct #1/#3 global-duplicate sentences counted as 1 partial). Older upstream text: create-FV #4 only.
