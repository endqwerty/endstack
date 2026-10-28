# Scoped recheck: fresh context, read-only, Claude Opus 5.5

Judged: endstack d41c92e2080749e6ce6e993e9293038862e26cd5 (tree a3255ec5f2f26ca12cac101bd31c1f7f07824b22, skills tree 8bf47c863115152f2342ebfef10b1df5d6bfb448).
Patch-ids (git patch-id --stable): beed4c3..d41c92e 2b03c94af75bc8a2f2cbcc81ea87e3860b6533fd; be7d5ad..d41c92e 70a560d54a554fe55e74f18b007c12b5e1da4cd3; 6136a6b..d41c92e 61f7896d00610c8aa3341cf0ee5b83f7bb6253c1.
Homelab 25ab4978cb6e04a4a02cfce553cb75d1a535a92e (tree 2ccd376c911ec0c3cc5a96a1428e9051b3050fd0). Patch-ids: cc6b246..25ab497 7dcbf59e0d8540a2db9adc99383032cd33d5b262; c348b51..25ab497 16d3b9b95cb8645d5d785f68d6e7acc71d1a6d20. Both working trees are clean. origin/main: endstack 6136a6b (== PR base), homelab c348b51 (== base). Fetched at the time of this check.
The incremental diff: endstack changes ship/SKILL.md step 2 and adds CHANGELOG, checks.md, 4 decisions.tsv rows and the round-1 verdict copy. Homelab changes route.py, routing.json, test_route.py, agents/AGENTS.md, workstation.md and CHANGELOG.

## Verdict: ISSUES (one should, no blockers)

S2 and S3 are resolved. S1 is only partly resolved (R1 below). Every required check passes. Both-provider exhaustion still blocks.

## Required checks (rerun by me)
- check-skills.py: PASS. "0 problem(s)", rc=0
- check-routing.py: PASS. "0 problem(s)", rc=0. ROUTING.md is unchanged from 6136a6b to d41c92e (0 diff lines).
- endstack unit tests (unittest discover -s scripts): PASS. "Ran 16 tests in 0.016s / OK"
- homelab offline script suite at 25ab497 (Python 3.15.1, unittest discover -s scripts): PASS. "Ran 282 tests in 37.897s / OK (skipped=1)". test_route alone: "Ran 55 tests / OK". The tree was clean afterwards.

## Fail-before evidence for the new homelab test
- The adoption record (checks.md) only states that the test failed first ("first failed twice ... `unexpectedly None`"). No captured output exists in the record or in /tmp/endstack-adopt.LsPF6j: route-tests.txt is the green 55-test run, and homelab-final-tests.txt shows a different intermediate failure (an old assertion at test_route.py:148).
- I reproduced it in a scratch copy: the 25ab497 tests with route.py from cc6b246. Result: PASS.
  "FAIL: test_single_available_provider_gets_a_fresh_native_verifier ... (provider='codex') / AssertionError: unexpectedly None"
  "FAIL: ... (provider='claude') / AssertionError: unexpectedly None"
- Assertion updates are confined to the approved behaviour change: PASS. In both directions, the failing set is exactly the 8 edited tests (plus the new one):
  - new tests with old code: "FAILED (failures=7, errors=3)" across reserve, blocked x2 (Command), blocked (Decide), codex-below-reserve, named/excluded, spent-fable-max, spent-model-window, and the new test x2;
  - old tests with new code: "FAILED (failures=8)" in the same 8 tests.
  Each edit changes an expected verifier from None/exit 3 to the sole available provider. No unrelated assertion moved.
- Both-provider exhaustion still blocks: PASS. test_nothing_left (codex 0%, claude 3%) and test_one_role_prints_one_line_and_none_exits_3 pass unedited in both directions. Direct calls:
  "both spent: None ['no provider can verify: report the work as not independently verified', ...]" and "both excluded: None [...same...]".
- Eligibility, allowance, exclusion and profile rules are kept: PASS. The fallback calls the same ranked("verifier"), so the reserve floors, blocked Codex, exclusion and per-profile model windows still apply (the max/Fable and spent-model tests pass). Because `order` already removed every non-author provider, the fallback can only pick the author's provider. With author=claude and exclude=[codex], the verifier is claude. With both excluded, it is None.
- native_subagent vs self: PASS. The verifier is never "self": parent=claude gives author self / verifier native_subagent; parent=codex or None gives delegate_task. The reason in every case is "same provider: a fresh independent reviewer context is required".

## Prior shoulds
- S1 (ship allowed only nonbehavioral exemptions): PARTLY RESOLVED. See R1.
- S2 (router returned no verifier when one provider was left): RESOLVED. These now agree with each other:
  - route.py:327-334: the fallback;
  - routing.json:5: "different provider preferred, not required";
  - workstation.md:217-219: "exits 3 only when no provider can take the verifier role";
  - the module docstring.
  A grep at 25ab497 for "always a different provider|nobody verifies|no provider other than" finds no stale text.
- S3 (global gate dropped "passing" and "current revision"): RESOLVED. agents/AGENTS.md:127-128 now reads "Otherwise require a passing verdict on the current revision from one fresh read-only reviewer before merging or calling it done."

## Findings

R1 (should, low) skills/ship/SKILL.md:22-24, the unfinished half of S1. Step 3 still reads: "Changed revisions or bases require fresh checks and a current independent verdict (verify says when an earlier one carries forward)." It has no exemption path. babysit/SKILL.md:27-28 has one ("a current independent verdict or valid exemption ... checks rerun if the base has since changed"). An exemption records "the current revision" (review-scope.md), and carry-forward's "Same patch on a new base" covers only verdicts. Two ordinary situations reach this: a validly exempt PR whose base moved before landing (main advanced), and any exempt child in a stack after its parent lands. In both, ship literally demands a fresh model verdict. The failure is conservative, the same class and reach as S1. Fix: "...a current independent verdict or valid exemption (verify says when an earlier one carries forward)". Consider "valid" in step 2 as well; "documented" reads weaker than verify step 5's "valid exemption" (nit). This is an agent-instruction edit, so it needs a scoped fresh recheck, not an exemption. It also changes the skills tree id below.

Nits (no round needed):
- `plan --role verifier` prints only "claude claudeAgent <model>". A one-line caller does not see the "fresh context required" reason; the provider == author signal is implicit.
- The fallback reason drops state["note"], for example the Codex under-reserve resume note.

## Paper ship regression (new; not part of the earlier paired runs)
Method: I applied the d41c92e ship text, together with verify, review-scope and carry-forward, to four cases. I am one reader, single sample, from the same model family as the earlier verifier, and I did not observe any hosted merge. The earlier paired runs (one sample each, old vs new bundle) excluded ship, so this is the first ship check. For the old arm I only read the be7d5ad text; I did not run it.
- A. Valid bounded-behaviour exemption: an exhaustive 3-value enum transform with the revision, contract, deciding outputs and coverage recorded; not an excluded category; required checks green; base unchanged. New ship: lands under step 2 (old text: refuses, because the change is behavioural). If the base moved after the exemption was recorded, step 3 blocks pending "a current independent verdict" (R1).
- B. Auth change. Review scope excludes security/authorization, so no exemption is "under its review scope". Ship needs a fresh passing verdict on the current revision and blocks without one. Same outcome under the old text.
- C. Missing required check. "Required checks and safety evidence must pass", and review-scope says "never required checks" and "no ... missing required evidence". Ship blocks on both paths. Same as the old text.
- D. Unresolved finding. "unresolved blockers ... stop landing" and "Every finding ... has a fix or a written reason". On the exemption path, carry-forward also requires the earlier findings to be resolved by current deterministic evidence. Ship blocks. A should declined with a written reason may land, which matches verify step 5. Same as the old text.
checks.md's own paper ship check agrees on A-D, and it honestly says "not an observed hosted exempt merge". It does not mention the base-moved case.

## Delivery and deployment conditions
1. PR [#24](https://github.com/endqwerty/endstack/pull/24) body is stale at head d41c92e. It still says "Ran 281 tests" and "Fresh independent final verification: in progress", and it lacks the ship dry-run note that AGENTS.md requires for a core delivery skill change. Update it before landing.
2. Endstack pin: after the rebase merge, fetch, take the actual origin/main commit (its SHA will differ from d41c92e) and require `git rev-parse <main>:skills` == 8bf47c863115152f2342ebfef10b1df5d6bfb448. Compare the whole skills tree. If R1 is fixed, the tree id of the rechecked head replaces this one. Any other mismatch voids the carry-forward. Expected blobs: verify/references/review-scope.md dc9773e882b65234a7edc6daed01d43b6ca6f693, ship/SKILL.md 1cd16b75c78d01889ba89caea78ff5758e56f0f1 (pre-R1).
3. Homelab pin commit: its diff is exactly skill-sources.json's endstack "revision" string (currently 6136a6b5…). The skill list (29) and the archify entry (208acba8…) stay unchanged. Current skill-sources.json blob: 2195bba6f0a281548153003eff7feead3dda5a4a. A pin-only change whose pinned skills tree equals the reviewed tree is a deterministic mechanical edit, so no new model pass is needed for it.
4. Homelab code identity to push (2 commits ahead of origin/main c348b51, plus the pin commit): 25ab497 code with these blobs:
   - agents/AGENTS.md 0ba450e916deb781f5d60c1dc64ac686ff8b6aa9
   - workstation.md 7793428232f0aa4dde85032fc37de3154c448c55
   - scripts/homelab_cli/route.py 340b77fb5821f424891904a45fdad023ec90ef69
   - scripts/homelab_cli/routing.json 413e32d2aea7fa857924d6cdd0c76bc711fe867d
   - scripts tree 6d6c40bca5fdedf296bfd4e1db5e1ca37e629524
   If origin/main has moved, rebase and rerun the 282-test offline suite.
5. On both machines (on omarchy, pull homelab first):
   - `homelab install`; the installed copy under ~/.local/share/homelab-cli/homelab_cli must have route.py and routing.json matching the blobs above, or `route models` keeps the old class text;
   - then `homelab sync` and a clean `homelab sync --check`;
   - the installed global rules file matches agents/AGENTS.md 0ba450e9…, and the installed verify/review-scope.md matches dc9773e8….
   The Mac's current ~/.claude/CLAUDE.md still has the pre-adoption gate, as expected before sync. If omarchy cannot be reached, record that.

## Decision-trail scan (new rows vs file history; flags only)
All four new rows (07:02:03Z-07:02:04Z) first appear in d41c92e (committed 07:03:09Z). None of them is in beed4c3 (06:52:59Z).
- A1(a) reversal: addressed (row "steering"). Logged about 20 minutes after the fact with no retrospective mark.
- A1(b) single author: addressed (row "design").
- A1(c) homelab gate rewrite and its Daniel-quote table: still not logged.
- A1(d) verify trimming: the row says the "detailed real-surface examples and rethink question remain in the existing design reference" (skills/build/references/design.md). That is false against the file. design.md is unchanged since 7257622 (2026-10-23) and contains neither "command, page, API, stored value" nor "Would another approach or smaller change avoid what findings share?". A grep of the d41c92e skills tree finds the examples nowhere. Only verify step 6's compressed "rethink the approach or scope" remains.
- A1(e) carry-forward edit after the paired runs: addressed (row "consistency").
- A1(f) ship and router left unchanged: addressed by the "correction" row. Its result is "fixing", although the fixes landed in the same commit. No row records the outcome (282 OK, fail-before reproduced).
- A2: row 1's result is still "open", with no closing row.
- A3: still no dry run for the arena, figure-it-out and trail edits. checks.md continues to disclose this.
- Sequencing: the homelab full suite failed at 07:02:41Z (old assertion at :148). That assertion was fixed before both commits (07:03:09Z), and the green full run came at 07:04:18Z, after the commits. My rerun on the committed tree is green, so this does not affect the verdict.

Not checked: hosted merge behaviour, the installed state on omarchy, and a live run of the ship skill.
