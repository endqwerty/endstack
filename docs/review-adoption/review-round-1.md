# Verdict (in progress) — independent fresh-context review, Claude Opus 5.5, read-only

Endstack head beed4c3b5149ccda3890a7afba9f99032b13add9 (tree af6cd6808a1fca993681a531f24efc13888f657f, skills tree 9a44aa6ae6880729daf8564a08d77409f5a5504d)
Adoption patch-id (be7d5ad..beed4c3): b7473c940dc213df8f2b05d651a0b3c19dda799e
Full PR patch-id (6136a6b..beed4c3): aa81e5f626e38b0de006f3d71d28b7ba8404d839

## Required checks
- check-skills.py: PASS — "0 problem(s)" rc=0
- check-routing.py: PASS — "0 problem(s)" rc=0
- endstack unit tests: PASS — "Ran 16 tests ... OK"
- homelab offline unit suite at cc6b2460c6ec468f44d87e4ebc77dca4b995eeab (clean tree, rerun by me): PASS — "Ran 281 tests in 39.351s / OK (skipped=1)"
Homelab diff c348b51..cc6b246 patch-id: 55810ee9d361d8b852d72ae49645975127fec114 (3 files: CHANGELOG.md, agents/AGENTS.md, workstation.md); homelab main is 1 commit ahead of origin/main (unpushed, as expected).
- Paired paper evidence: PASS — policy-old.md sha256 4ceb20e6…97f5 == /tmp old.md; policy-new.md 8fea4893…9751 == /tmp new.md; scenarios 0d88aeff…050e5; result-old 3bf0bea6…d57d6 and result-new 94593d2d…0f9d byte-identical to /tmp copies. Reconstructed bundles: every old file MATCHES be7d5ad; every new file MATCHES beed4c3 except carry-forward.md "Anything else" (post-run clarification), which checks.md discloses. Limits stated honestly (one sample per side, no token/reliability claim, ship/build/babysit/arena/trail workflows not exercised).
- Quoted user words: PASS — "I'm okay with lifting it" and "definitely allow exemptions when appropriate" verbatim user messages (activity pos 190/191); coding statements came from user message pos 168 ("thoughts on these statements?"), approved at pos 185; checks.md records the refinement honestly.
- Routing copy: PASS — ROUTING.md unchanged 6136a6b..beed4c3; all 13 bullets present in homelab agents/AGENTS.md.
- Changed skills selected for install: PASS — verify, principles, arena, figure-it-out, show-me-your-work all in skill-sources.json endstack list.
- Exemption vs required-review decisions (review-scope.md): PASS on text — sensitive/agent-instruction/deployment/concurrency/external-contract excluded; missing required evidence blocks; author self-review never qualifies; same-provider fresh context qualifies; explicit review request and stricter project rules survive.
- Consistency with build/babysit/ship/carry-forward: ISSUES — see S1.
- Homelab global gate + workstation docs: ISSUES — see S2, S3.

## Findings (ranked by demonstrated impact; no blockers)

S1 (should) skills/ship/SKILL.md:15-16 (unchanged, from 07b8f99): "Require verify's independent passing verdict on the current revision, or its applicable nonbehavioral exemption." review-scope.md now permits exempting "small bounded behavior changes whose full affected contract is established by deterministic evidence". Trace: dry-run case 2 (three-value enum transform, exhaustively checked) is exempt under verify, build and babysit ("valid exemption"), but ship — and autopilot-full, which composes ship — must refuse to land it because it is behavioural. Fails toward more review (not unsafe), but contradicts the approved "allow exemptions when appropriate" and checks.md's "All delivery skills already consume verify". The dry-run bundle excluded ship, so it never saw this. Fix: "or verify's valid exemption"; ship is a core delivery skill, so the PR needs a dry-run note for it.

S2 (should) homelab scripts/homelab_cli/route.py:328-329 and scripts/homelab_cli/routing.json:5 (not in the reviewed diff, but still emitted to agents): `route plan` warns "no provider other than the author can verify: report the work as not independently verified" and `--role verifier` exits 3 (EXIT_NONE, route.py:526) whenever the author's provider is the only routable one; `route models` prints "verifier: the independent check, always a different provider from the author". The global rule tells every agent to run this command to name the verifier. When the other provider is out of allowance (ordinary), the tool tells the agent to stop unverified, though the new policy says a fresh same-provider reviewer qualifies. agents/AGENTS.md:134-135 ("its cross-provider preference is not a requirement") mitigates for a careful reader. Fails conservative. Fix: reword the warning and class text (deterministic output, covered by homelab tests), or record it as a known follow-up.

S3 (should, low) homelab agents/AGENTS.md:128-129: the always-loaded gate went from "without a passing independent verdict on the current revision" to "require one fresh read-only reviewer before merging or calling it done". "Passing" and "current revision" are gone; only the verify skill keeps them. An agent reading only the global rule can treat having a reviewer as enough. One-phrase fix: "require a passing verdict on the current revision from one fresh read-only reviewer".

Nits (no round needed): skills/show-me-your-work/references/audit-and-review.md:11 heading still says "Cross-model review of the trail"; endstack AGENTS.md:23-24 still says reviewer roles "ask for a different provider or model family 'if available'", now softer than skills that call it optional. Historical homelab delivery-policy.md:54 is marked superseded; ignore it.

## Deployment plan judgment
Sufficient without another model pass, under these conditions:
1. Before pinning, fetch endstack and confirm the merged revision is on origin/main and that `git rev-parse <merged>:skills` == 9a44aa6ae6880729daf8564a08d77409f5a5504d. Compare the whole skills/ tree id, not just the selected folders. Today origin/main == 6136a6b == the PR base (skills tree 8f4baa98…), so a rebase merge should reproduce the trees; any mismatch voids this carry-forward and needs a fresh scoped review.
2. The homelab pin commit's diff is exactly the endstack "revision" string in skill-sources.json, with no change to the skill list or the archify entry.
3. The homelab tree that gets pushed has agents/AGENTS.md and workstation.md byte-identical to cc6b2460 (patch-id 55810ee9…), or origin/main has not moved. If homelab must rebase over new upstream commits, rerun the offline suite.
4. If S1-S3 get fixed: the S1 and S3 edits are agent-instruction changes, so they need a scoped fresh recheck (carry-forward "Anything else"), not an exemption. The tree id in (1) then becomes the new reviewed one.
5. After sync, on both machines: `homelab sync --check` is clean, the installed verify/review-scope.md matches the pinned blob, and the installed global rules file matches agents/AGENTS.md at the pushed head. Sync already enforces cache HEAD == pin and compares blob by blob (skill_sources.py:114-148). If omarchy cannot be reached, record that.

S2 addendum: homelab workstation.md:217-219, in a file this diff touches but in lines it left alone, still reads "With two providers, when one cannot work the other writes and nobody verifies: `plan` says so (`--role verifier` exits 3) and the work is reported as not independently verified." That contradicts the new rule at workstation.md:190-192 and agents/AGENTS.md. The 06:49 grep (activity pos 206) matched line 218, but the line was left as is.

## Overall
ISSUES — 3 shoulds open (S1 ship exemption wording; S2 homelab route output and workstation.md:217-219 still say "nobody verifies"; S3 the global gate lost "passing" and "current revision"). No blockers. All three fail toward more review or looser wording, not toward unsafe merges. Per verify step 5, delivery waits until they are fixed or declined with a written reason. Every required check ran and passed. Judged: endstack beed4c3b5149ccda3890a7afba9f99032b13add9, patch-ids b7473c94… (adoption) / aa81e5f6… (full); homelab cc6b2460c6ec468f44d87e4ebc77dca4b995eeab, patch-id 55810ee9….

## Decision-trail audit (decisions.tsv vs activity.json pos 185-224; attention flags only)
A1. The trail is thin: 2 rows for a run with at least 6 consequential choices. Not logged:
    (a) the reversal from "I'll keep the current cross-provider requirement and review exemptions" (pos 186) to lifting both (pos 192), folded into row 1's "why";
    (b) the single-author choice (pos 195, chat only);
    (c) the homelab gate rewrite and its Daniel-quote table;
    (d) trimming verify/SKILL.md to fit the 2200-byte limit (reasoning pos 197; now 2198 B). This dropped the "command, page, API, stored value" examples and the "Would another approach or smaller change avoid what findings share?" prompt;
    (e) editing carry-forward after the paired run (disclosed in checks.md, not in the tsv);
    (f) leaving ship/SKILL.md "nonbehavioral exemption" and homelab route output unchanged. There is no evidence these were considered: ship was read at pos 187, and the pos 206 grep matched workstation.md:218, but neither was changed or logged.
A2. Row 1's evidence is checks.md, a plan, not a proof. Its result is still "open" at the snapshot.
A3. Row 2 (06:51:52Z): the arena, figure-it-out and trail edits landed at pos 217 (06:51:53Z), after both paired runs finished (pos 205 06:50:33Z, pos 213 06:51:46Z). Those edits have no dry run. checks.md says so, which is correct.
A4. Claim checks: "The skill and routing checks pass" (pos 212, 06:50:14Z) is backed by checker runs at pos 202 and pos 215/218, and my rerun reproduces it. The homelab suite claim (pos 207) is backed by homelab-tests.txt, and my rerun matches it: 281 tests OK, skipped=1.
A5. Both paper arms used the same model, the same family as this verifier, one sample each. This is disclosed. The quotes are verified verbatim.
