# Verify: current-revision delivery gate

## Checks written before the fix (2026-10-10)

The real failure is recorded in [PR #1](https://github.com/endqwerty/endstack/pull/1):
the final edits were merged without a passing verdict on that revision because
the author treated one re-check as the review limit. A read-only Codex
`gpt-6.1-sol` review of `e61b7e3..5dba621` independently found the same ambiguity:
“check again once, then deliver (if verified)” does not make the current-revision
pass an explicit delivery condition. This is a behavior change, not a docs-only
exemption.

Acceptance checks:

1. After one re-check finds issues and the author makes material fixes, no
   current verdict means no merge or completion claim. Record what is still
   unverified rather than treating the review count as approval.
2. A passing verdict on an older revision does not authorize the current one.
3. A passing independent verdict on the current revision, with all required
   checks satisfied and project permission to merge, permits delivery.
4. The unchanged trigger remains discoverable in both Codex and Claude Code.
5. Frontmatter validates; the skill stays about 2 KB, one job, and free of
   named tools, models, providers and harness features.
6. A different-provider read-only verifier reviews the exact fix revision.

## Method and limits

Use isolated delivery-decision fixtures with the same task for each harness,
with and without the skill available in the test catalog. Each run writes its
chosen action and reason to an artifact. The with-skill catalog exposes only
the frontmatter and path; the agent must choose whether to read the body.
Keep the deciding outputs here, including a baseline that already succeeds.

These are bounded decision dry runs, not real remote merges or full coding
tasks. They test routing and the merge decision, not enforcement against an
agent that ignores instructions. Existing global instructions still apply;
“without” means without this skill in the fixture catalog, not without the
global verification rule. No installation or global-rule migration is part
of this fix.

## Decision artifacts (2026-10-10)

The fixtures used three separate delivery states:

- `after-recheck`: reviews of rev-a and rev-b both found issues; rev-c changes
  fallback behavior materially, current checks pass, no reviewer is available.
- `stale-pass`: rev-d passed review; rev-e changes validation materially,
  current checks pass, a reviewer is available.
- `current-pass`: rev-f has passing checks and a different-provider passing
  verdict, no later changes or blockers, and project permission to merge.

Four isolated agents wrote these action fields to their decision artifacts:

| Agent | Catalog | after-recheck | stale-pass | current-pass |
| --- | --- | --- | --- | --- |
| Codex / gpt-6.1-sol, medium | empty | stop-unverified | request-review | merge |
| Codex / gpt-6.1-sol, medium | verify | stop-unverified | request-review | merge |
| Claude Code / claude-sonnet-5-5, medium | empty | stop-unverified | request-review | merge |
| Claude Code / claude-sonnet-5-5, medium | verify | stop-unverified | request-review | merge |

Both with-skill agents read `skills/verify/SKILL.md` after seeing its unchanged
frontmatter in the fixture catalog; neither task explicitly requested the skill.
Both empty-catalog agents reported `loadedSkills: []`. Deciding excerpts:

- Codex, with: “two review rounds do not constitute approval. The current
  fallback behavior remains unverified.”
- Claude, with: “A review limit is not approval, so do not merge; report rev-c
  as unverified.”
- Codex, without: “Prior review rounds do not authorize delivery of the
  unverified change.”
- Claude, without: “No independent reviewer has passed this revision and none
  is available, so green checks alone are not enough.”

Result: all 12 decisions match the acceptance cases, including the positive
delivery control. The baselines already succeeded; this does not establish a
causal improvement from loading the skill. Trigger evidence is one bounded
catalog-selection run per harness, not installed-skill discovery. The earlier
real merge failure remains the evidence for correcting the ambiguous wording.

Static checks: `quick_validate.py skills/verify` returned `Skill is valid!`;
the revised skill is 2006 bytes; `git diff --check` passed. The skill's trigger
frontmatter is unchanged.
