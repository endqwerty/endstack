# Audit B: endstack additions vs pstack 0b46ec3

Skills: interrogate, ketchup, ketchup-video, no-comments, recall, reflect, sharpen, show-me-your-work.
Paths below are relative to the endstack worktree. "Origin" is the first endstack commit that added the phrase (`git log -S`, which includes imported upstream history).

## interrogate

Context: upstream rewrote interrogate before 0b46ec3 into a short run-proven skill (2,314 bytes: adversaries run repros in worktrees, arena Phases A/B/F, only run-proven findings survive, no references). Endstack kept the older upstream panel design (c493c25, ba74fc3) plus its own edits. Every reference file below is endstack-only relative to 0b46ec3, and all four are older upstream text. The meaning differs from upstream's: upstream drops any finding a run does not prove, while endstack allows a trace as evidence and keeps Noted/Dismissed buckets.

1. Whole panel structure (Steps 1-5, four buckets, Agreement Map). `skills/interrogate/SKILL.md:9-69`, "The deliverable is a synthesized verdict".
   - Origin: c493c25 (2026-05-22, older upstream text), ported 026a4d6.
   - Elsewhere: upstream has a different design (no buckets, no agreement map). Arena (`skills/arena`) covers fan-out.
   - Judgment: DROP the old design if following upstream. Upstream's author judged read-only review mostly wasted tokens, so reviewers that only read code produce nitpicks. Endstack's evidence filter (item 2) is a partial patch for that.
2. Evidence gate. `SKILL.md:44`, "A finding goes in Act on or Consider only with evidence a reader can check"; also the structural-vs-defect split ("A changed contract or behaviour is a defect, not structure") and "unproven" marking for data-loss/security/trust-boundary findings.
   - Origin: ce62399, acf05f9, 83313dc (2026-11-02).
   - Elsewhere: same rule in `skills/verify/references/review-rubric.md:19-30`. Upstream's run-only rule covers it more strictly.
   - Judgment: KEEP the rule, with caveat. It is backed by `docs/2026-11-02-evidence-over-dissent.md` (cites the upstream author's complaint about nitpicks). It is a weaker, endstack-specific version of upstream's "a run proves it". If interrogate is cut to upstream's form, this goes away with no loss.
3. Reviewer-prompt evidence field and nit-downgrade. `references/reviewer-prompt.md:40`, "A finding without this is a nit, unless it concerns data loss, security or a trust boundary".
   - Origin: ce62399, 83313dc.
   - Elsewhere: duplicates item 2 in two places, and again in verify's rubric.
   - Judgment: DROP as a duplicate if SKILL.md keeps item 2. The same rule is stated three times in endstack.
4. Dissenter removal and "Agreement ... is not evidence". `SKILL.md:44`.
   - Origin: dissenter added 7257622 (2026-10-23), removed ce62399. Removal is documented in `docs/2026-11-02-evidence-over-dissent.md`. The "not evidence" sentence is in ce62399.
   - Judgment: KEEP the removal (recorded, deliberate). Upstream has no dissenter either.
5. `references/code-quality-review.md` (5,217 bytes): "code judo", ">1k lines" file-size rule, "presumptive blockers", "Review Tone ... demanding".
   - Origin: ba74fc3 (2026-05-28, older upstream text); upstream later removed it.
   - Elsewhere: upstream has no equivalent. `skills/principles` covers structure and simplicity.
   - Judgment: DROP. It is a "be ambitious about restructuring" lens that pushes reviewers toward the nitpick and "I would do it differently" findings that `lead-judgment.md` tells the lead to dismiss. The 1k-line rule is arbitrary and unproven. The skill also contradicts itself: Approval Bar says "do not approve merely because behavior seems correct", and the evidence gate says opinions without evidence are Noted.
6. `references/rubric.md` (Correctness, Root Causes, Structural Integrity, Verification, Complexity Budget, Security).
   - Origin: c493c25 (older upstream text).
   - Elsewhere: overlaps `skills/verify/references/review-rubric.md` (same lens set) and `skills/principles`.
   - Judgment: DROP as a duplicate of verify's rubric, unless interrogate stays as a read-only panel.
7. `references/lead-judgment.md` ("Nitpick Gravity", "Hypothetical vs. Actual", "Premature Abstraction Warnings", "Missing Context Signals", "Verdict Calibration").
   - Origin: c493c25. ea2a8c8 (2026-10-21) removed the numeric "more than 5 items" cap. That removal is endstack's own edit and is fine.
   - Elsewhere: partly in the SKILL.md bucket definitions and in verify.
   - Judgment: DROP (older upstream text, unproven). Its valid core (trace the call site before accepting) is in item 2.
8. `references/reviewer-prompt.md` template (severity levels critical/warning/nit, output block).
   - Origin: c493c25.
   - Judgment: DROP with the panel design. Upstream's brief is one paragraph.
9. Output sections Reviewers, Noted, Dismissed, Agreement Map. `SKILL.md:48-67`.
   - Origin: c493c25.
   - Judgment: DROP. Upstream's output is Intent, Findings (command, output, break), Dropped (counts). It is smaller and tied to runs.
10. Closing pointer to verify. `SKILL.md:69`, "For the single independent delivery check, use verify".
    - Origin: 026a4d6 (port edit, replaces upstream's single-reviewer link).
    - Judgment: KEEP. Routing glue, not a rule.

## ketchup

Context: endstack text is a mix of upstream's first ketchup (aafd77f) and later upstream-synced edits. Upstream's 0b46ec3 version is longer and different: it adds word budgets, the "plain words" voice rules, a six-box visual cap, an "opening sentence names what waits" opener, and per-item fields (link, change, evidence, risk, pick). Items below are endstack text that upstream no longer has or that changed meaning.

1. Opener counts items. `skills/ketchup/SKILL.md:21`, "Open with one sentence that says how many action items there are".
   - Origin: aafd77f (older upstream text). Upstream now says "names what waits on the user, or says nothing does".
   - Judgment: DROP. A count tells the reader nothing, and upstream replaced it.
2. Per-item "short executive summary" with "why it matters now ... and what happens if the user does not answer". `SKILL.md:25`.
   - Origin: aafd77f (older upstream text). Upstream replaced it with call/pick/evidence/risk and says to state the cost of waiting "only when it is more than a delay".
   - Elsewhere: lines 26-27 overlap (shared-call bullets with risk, evidence, user impact).
   - Judgment: DROP the cost-of-not-answering requirement. It makes every item carry a filler clause, and upstream decided against it. Lines 25 and 27 describe the item shape twice.
3. "Say which are still running and which you could not check." `SKILL.md:13`.
   - Origin: aafd77f (older upstream text, removed upstream).
   - Judgment: DROP. Upstream moved status into the "done, still running, failed, or not checked" summary lines. The same fact is also stated by "Check the current state".
4. "Use the bro style: plain, direct, conversational language". `SKILL.md:9`.
   - Origin: aafd77f, port edit (bro link dropped because bro is not imported, per `docs/import-notes/W1.md:17`).
   - Judgment: KEEP as port. It is much weaker than upstream's voice rules ("no jargon, say the tests pass, not CI is green, no hashes or paths").
5. Frame "Never invent a call to fill the reply" and the irreversible-step exception. `SKILL.md:15, 25`.
   - Origin: 0c59d0a (2026-10-21), ported from upstream 190d287. Upstream 0b46ec3 has the same rule.
   - Judgment: KEEP (not an addition; upstream text). Dry runs in `docs/upstream-190d287-role-skills.md`.
6. Visuals section (reuse captures, "No screenshot yet", no faked screens, no repeated facts, option gain/cost under each capture). `SKILL.md:29-33`.
   - Origin: e5c8739 (2026-10-21), but all of it exists upstream in 0b46ec3 in fuller form.
   - Judgment: KEEP (not an addition).

Net: nothing endstack invented beyond upstream except the omissions. Items 1-3 are stale upstream wording.

## ketchup-video

no additions. Differences are porting only: the slash trigger is replaced by prose, "Choose the rendering tools." replaces upstream's "Render one silent landscape video..." framing, and "burned-in subtitles" moves from a later sentence into the first. The content is otherwise identical to upstream (all rules, the hold math, and the render check are present).
- Origin: 0822db5 (2026-11-10), `docs/import-notes/W8.md`.

## no-comments

Context: upstream relies on a separate `comment-sicko` agent definition that endstack deleted at 8a6e905. Endstack's SKILL.md therefore points at a role definition that does not exist. `docs/import-notes/W3.md:13` admits this.

1. "What may stay" section (whole). `skills/no-comments/SKILL.md:17-23`, "These are the exceptions step 2 means".
   - Origin: b6ff55d (2026-11-17), refined in 88e25bf. Taken from the landmines lint package, not from the lost Sicko catalog (`docs/landmines-lessons.md`).
   - Elsewhere: upstream's `agents/comment-sicko.md` has its own exception list (legal headers, forced external behaviour, prettier-ignore, public API docs, issue/RFC links). Not in any endstack skill.
   - Differences from the upstream list: adds tool directives (formatter and coverage ignores, bundler hints, shebangs). Drops issue/RFC links. Changes the meaning of "forced external behaviour": upstream keeps it as a free-form comment, endstack keeps only a one-line `WARNING:` hazard comment.
   - Judgment: KEEP the list, since without the agent file the skill has no exception catalog. The dry run is in `docs/landmines-lessons.md`. But it is one source's list, not upstream's, and was never run against the real Sicko.
2. `WARNING:` one-line format ("Rewrite each surviving hazard comment into this form, so a lint can tell keeps from prose"). `SKILL.md:22`.
   - Origin: b6ff55d, scoped by 88e25bf.
   - Elsewhere: nowhere else. Upstream has no keep format.
   - Judgment: KEEP, weakly. It is a new convention with no lint behind it in endstack ("so a lint can tell" refers to a lint that does not exist here). Drop the clause if no project adopts the lint.
3. "A constraint encoded in step 5 keeps no comment; its check's failure message carries the reason." `SKILL.md:22`.
   - Origin: 88e25bf (verifier finding fix).
   - Judgment: KEEP. It resolves a real conflict between step 5 and the WARNING rule, found by a verifier.
4. "the proof applies to hazard comments ... Directives and interface docs stay without step 2's proof". `SKILL.md:19`.
   - Origin: 88e25bf.
   - Judgment: KEEP. Same reason: scopes the proof rule to hazard comments.
5. Step 1 fallback "If that role definition is unavailable, use the acceptance contract below and what may stay, and report that limitation". `SKILL.md:27`.
   - Origin: 026a4d6, b6ff55d (the link).
   - Judgment: KEEP. Port fallback for the missing agent file.
6. Step 2 `/why` replaced by "trace how their symbol works or why it exists from source". `SKILL.md:28`.
   - Origin: 026a4d6. Port edit, not an addition.
7. Step 6 "Report ... architect sketch" and the architect/fix-root-causes links. `SKILL.md:29-30`.
   - Port edits, same meaning as upstream.

## recall

no additions. Differences are porting only: transcript path text replaced by "Find transcripts through the harness's available history access ... Do not assume a particular filesystem layout" (`skills/recall/SKILL.md:15`), subagent and model language replaced by the worker fallback, `git`/`gh` replaced by "live repository, PR and ticket state", the automate-me line dropped (85f8272), and the poteto-mode reference dropped. The capsule/threads/problems/next-move contract is unchanged.
- Origin: 229f1dc (upstream), 026a4d6 (port), 7257622, 85f8272.
- Minor: the new "If history is unavailable, report the gap and use the supplied context and live record" sentence is endstack's own. KEEP, a harmless port fallback.

## reflect

Endstack text is a tight 1,591 bytes, close to upstream's 1,396.

1. Defect vs preference/experiment sort. `skills/reflect/SKILL.md:13`, "A recurring defect that a lint, script or check could enforce goes to the backlog ...; a preference or an experiment stays a revisable note (the correct skill says which is which)".
   - Origin: 7257622 (2026-10-23), reworded 959832c. Upstream says only "What a lint, script or check could enforce goes to the backlog, not into prose".
   - Elsewhere: `skills/correct/SKILL.md:15, 21` states the same classification (defect/preference/experiment) and "A preference or experiment ends with its note".
   - Judgment: KEEP. It prevents a recorded failure mode (a first preference being promoted to a guard); the dry run is in `docs/2026-10-23-learnings-dry-runs.md`. It is a meaning change from upstream but a deliberate one tied to `correct`. Could be shortened to a pointer, since `correct` already owns the rule.
2. "If the skill already lives in its maintained source, edit that source." `SKILL.md:17`.
   - Origin: 0822db5 (2026-11-10, port of upstream's `.cursor/skills` copy-then-edit rule).
   - Judgment: KEEP. It follows from removing the Cursor path and plugin-cache assumption, but it is a new branch of behaviour. It is not recorded as a deliberate change in the import notes. Low risk.
3. Replaces "Never open a PR or push" with "Never open a pull request or publish changes as part of reflection." `SKILL.md:17`.
   - Port edit. Slightly broader ("publish") but equivalent in spirit.

## sharpen

Heaviest divergence: 2,247 bytes vs upstream 816. Upstream is a four-question prompt plus one sentence about prototyping. Nearly everything beyond that is endstack's addition, from `docs/sharpen-scope.md` (evidence: 15 transcripts from 2026-10-25 to 2026-11-14 where rewrites grew; user pushbacks quoted such as "remove the currencies" and "why do you need to run tests"; a three-prompt dry run with one sample per prompt).

1. "Deeper changes how my result is made ... Bigger adds more things to make." `skills/sharpen/SKILL.md:7-9`.
   - Origin: d362277 (2026-11-16). Elsewhere: upstream's title line only says "deeper, not bigger".
   - Judgment: KEEP. Defines the term that the recorded overreach violated.
2. Goal sentence plus single relevance test ("would it change that result, or how far I can trust it?"), most important first, drop the rest unlisted, "nothing here would change the result" allowed. `SKILL.md:11-15`.
   - Origin: 6a5518c. Doc: `docs/sharpen-scope.md` (Root cause: every question answered with 3-8 bullets, none said "nothing to add"). Upstream has no such filter.
   - Judgment: KEEP. It is the main fix; a count cap was tried and dropped, per the doc.
3. Item 3 "Say in plain words what each does for this task." `SKILL.md:23-24`.
   - Origin: 6a5518c. Doc limit: the CI run still listed six methods.
   - Judgment: KEEP, minor.
4. New deliverables become proposals that stay out of the prompt until taken; "Approving the rewrite approves the prompt, not the proposals." `SKILL.md:29-31, 46`.
   - Origin: 6a5518c; last sentence d362277. Doc: added deliverables/frameworks overreach.
   - Elsewhere: upstream keeps "rewrite my prompt to ask for exactly that", i.e. the opposite.
   - Judgment: KEEP. Changes upstream's meaning on purpose, backed by the transcripts.
5. "Keep how firm I was ... a 'maybe' ... stays an option ... What I asked for stays required." `SKILL.md:32-34`.
   - Origin: d362277, d35b5fd. Doc: the "idk" ownership-model case and the CI "optional goals" miss.
   - Elsewhere: same principle is in the user's global rules ("Preserve firmness") and `skills/correct/SKILL.md:15`, not in other skills.
   - Judgment: KEEP. Cited failure.
6. "A question or research stays that: the rewrite adds no code, tests, commits or audits I did not ask for." `SKILL.md:35-36`.
   - Origin: 6a5518c. Doc: "Research turned into delivery".
   - Judgment: KEEP.
7. "Decide what evidence and my known preferences can settle, and say what you assumed. Ask me only what changes the outcome and only I can answer, with your recommendation." `SKILL.md:37-39`.
   - Origin: 6a5518c. Replaces older "Leave choices that are mine to make open" (88cf6f4). Upstream, after its own rewrite, keeps open only product/preference choices.
   - Doc: "Too many open choices".
   - Judgment: KEEP. Overlaps item 8's last sentence ("Product and preference choices ... stay with me"); line 37-39 and 40-42 together say it twice.
8. Prototype-an-experiment sentence. `SKILL.md:40-42`.
   - Origin: 85f8272 (2026-11-20), taken from upstream. Not an addition.
9. Output order "the goal; proposals and questions for me ...; the four answers; the rewritten prompt. Do not carry out the task." `SKILL.md:44-46`.
   - Origin: order 6a5518c. "Do not carry out the task" 88cf6f4 (older upstream text, later dropped upstream). Four answers returned: 5e80966.
   - Judgment: KEEP. Upstream's text no longer says "do not carry out the task" at all. Note that 2,247 bytes costs tokens on every use, and limits stated in the doc are one sample per prompt.

## show-me-your-work

Endstack-only file: `skills/show-me-your-work/references/audit-and-review.md` (2,570 bytes).
It holds upstream's "Audit the log against the transcript", "Cross-model review of the trail", "Reviewing the trail" and "Composing this skill" sections, moved out of SKILL.md to save bytes (`docs/import-notes/W2.md:5`, "Moved the complete audit/review section to an on-demand reference"). `log.sh` and `decision-log-template.tsv` are byte-identical to upstream.

1. Split into reference file. `SKILL.md:55-57`, "Read audit and review at the end of the run".
   - Origin: 026a4d6.
   - Judgment: KEEP as a size control, but note the risk: the audit and the mandatory Attention section now depend on the agent opening a second file at the end of a long run. No check records that it does. Upstream keeps them inline.
2. Cross-model review made optional. `references/audit-and-review.md:13`, "in fresh context independent of the author. A different model family is optional. If no separate reviewer can run, say the review is not independent."
   - Origin: 026a4d6 wrote "different model family ... if available"; c26c20b (2026-10-27) changed it to "optional".
   - Elsewhere: same wording in `skills/arena/SKILL.md:28`, `skills/figure-it-out/SKILL.md:41`, and the global rule on independent review.
   - Doc: `docs/import-notes/review-defaults.md`, `docs/review-adoption/`.
   - Judgment: KEEP. Deliberate meaning change from upstream's mandatory "another vendor's model"; the global CLAUDE.md defines independence as fresh context.
3. Attention line: "Lead with the reviewer identity and independence limits ... An unnamed or falsely independent reviewer is not [a valid value]." `references/audit-and-review.md:20`.
   - Origin: 026a4d6, c26c20b. Upstream: "reviewed by <model>". Port edit tied to item 2.
   - Judgment: KEEP.
4. Transcript audit: "If the transcript is unavailable, disclose that this audit could not be completed." `references/audit-and-review.md:3`.
   - Origin: 026a4d6. Port fallback, replaces the Cursor path rule.
   - Judgment: KEEP.
5. "Use a tabular viewer for the TSV" replaces the `column` command, "leave it out of version control" replaces "git". Port edits only.

## Totals

Items listed above, counting each judged line: interrogate 10, ketchup 6, ketchup-video 0, no-comments 7, recall 1, reflect 3, sharpen 9, show-me-your-work 5. Excluding port-edit-only lines (interrogate 10; ketchup 4-6; no-comments 6-7; reflect 3; sharpen 8; show-me-your-work 5 and parts of 4): substantive items about 30, drop about 11.
