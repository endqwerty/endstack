# Final scoped recheck: fresh context, read-only, Claude Opus 5.5

## Verdict: PASS

R1 (the ship step 3 should from review-round-2) is resolved. No blocker, should or new finding.

## Identity judged
- endstack head 52296e7baf78b8db9cda9af7ba41336e006b8b81 (tree f83019b57b3a425434a6ded060fe058aced052db), previous d41c92e2080749e6ce6e993e9293038862e26cd5. Working tree clean.
- **Skills tree for the post-merge pin attestation: b358f1920ea97329a5486b834c0f4c3637949f0a.** This supersedes 8bf47c86… from round 2.
  - ship/SKILL.md 56b8f937861389a96e40e61c41736d8735e3d32d
  - verify/SKILL.md 0b28d3bdb2bf4692e5b205d5cfac927b46020463
  - verify/references/review-scope.md dc9773e882b65234a7edc6daed01d43b6ca6f693
  - verify/references/carry-forward.md ecca5e2a047b46b1590cf39cf0c7fab9d9f5067a
- The incremental skills diff is only the two lines of ship/SKILL.md step 3. Every other blob under skills/ matches d41c92e (ls-tree diff is empty). ROUTING.md is unchanged.
- origin/main is 6136a6b5cf83cf4361ddda03c8b445375d22aa5a (== PR base). PR #24 head is 52296e7, reported MERGEABLE.
- homelab: HEAD 25ab4978cb6e04a4a02cfce553cb75d1a535a92e, tree 2ccd376c…, clean. agents/AGENTS.md 0ba450e9… and scripts tree 6d6c40bc… match round 2. origin/main is c348b51. skill-sources.json 2195bba6…, which still pins endstack 6136a6b. The 282-test suite and routing results carry forward from round 2; I did not rerun them.

## Checks I ran
- check-skills.py: "0 problem(s)", rc=0
- check-routing.py: "0 problem(s)", rc=0

## R1 resolution
New step 3 text: "Changed revisions or bases require fresh checks and a current passing verdict or documented exemption under verify, including its carry-forward rules."
- Step 3 now matches step 2 ("passing verdict ... or a documented exemption under its review scope") and babysit ("current independent verdict or valid exemption ... checks rerun if the base has since changed").
- How verify routes it: carry-forward's "Same patch on a new base" covers verdicts. For an exemption, a reader reaches "Anything else", which says to apply review scope to the current revision. There, a documented exemption replaces a model verdict only when current deterministic evidence resolves the contract and the earlier findings. review-scope makes the exemption record the current revision. So the author re-records it on the new revision with rerun checks, and no model is needed. A changed patch (a conflict resolution) is "a new behavior change", which needs a new exemption decision or a fresh verdict.
- "independent" was dropped from step 3, but "under verify" and step 2's "verify's independent passing verdict" still bind it. Not a finding.

## Paper checks (one reader, single sample, no hosted merge seen)
1. Ordinary valid exempt PR, base unchanged: lands under step 2. Required checks must pass.
2. Exempt PR, base changed: step 3 reruns the checks and re-records the exemption on the combined revision. If the base touched what the patch depends on, the change's own checks run too. No model pass. If a rerun check fails, that is a finding and needs a fresh verdict. If a conflict resolution changed the patch, it needs a new exemption decision or a verdict.
3. Next exempt layer after its parent lands: same as case 2 for the new base. Step 3 still forbids merging a child into an unlanded parent, and step 4 reinspects after each landing.
4. Authorization change: review-scope excludes security and authorization, so no exemption is valid and step 2 needs a fresh passing verdict. On a base change, the verdict carries forward only under the same-patch rule, with checks rerun.
5. Missing required check: blocks. Step 2 says "Required checks ... must pass", step 3 says "fresh checks", and review-scope says "never required checks" and "no ... missing required evidence".
6. Unresolved finding: blocks. Step 2 says "unresolved blockers ... stop landing" and every finding needs a fix or a written reason. On the exemption path, carry-forward needs earlier findings "resolved by current deterministic evidence".
Rechecks, evidence and stricter project gates all stay mandatory. Both-provider exhaustion still blocks (round 2, homelab unchanged).

## Trail corrections: factual accuracy
- rethink row (07:11:46Z): accurate. Both ship gates now defer to verify.
- correction row: accurate. design.md is unchanged since 7257622 and has neither the examples nor the rethink question. Verify keeps the check-first rule (step 1) and "rethink the approach or scope" (step 6).
- provenance row: accurate. The steering, design, consistency and correction rows (07:02:03-04Z) were logged together in d41c92e.
- gate row: the homelab gate rewrite and the two-row Daniel's-words table are present at 25ab497 (agents/AGENTS.md:124-142). I did not check that the quotes match the user's original messages.
- checks.md addendum: accurate against the diff and the homelab identity.
- Unchanged and acceptable: row 1 stays "open" because the post-landing sync is not done yet. The round-1 "fixing" row has no closing row, but checks.md and review-round-2.md record what happened. Neither is a finding.
- PR #24 body: it now has "Ran 282 tests" and the ship paper-check note. I did not rescan the rest of the body.

## Post-merge conditions (no further model pass needed)
A pin-only update needs no further model pass if all of these hold:
- After the rebase merge, fetch, and take the actual origin/main commit, whatever its SHA.
- Require `git rev-parse <that commit>:skills` == b358f1920ea97329a5486b834c0f4c3637949f0a. Compare the whole tree. Any mismatch voids this.
- The homelab pin commit diff is exactly skill-sources.json's endstack "revision" string, with the skill list and the archify entry unchanged.
- It sits on homelab code identical to 25ab497. If homelab origin/main moved, rebase and rerun the 282-test suite.
- On both machines (pull homelab first on omarchy): `homelab install`, then `homelab sync` and a clean `homelab sync --check`. The installed route.py and routing.json, the global rules (0ba450e9…) and verify/review-scope.md (dc9773e8…) must match. If omarchy cannot be reached, record that.

Not checked: a hosted merge, a live run of the ship skill, the installed state on either machine, and the exact wording of the user quotes.
