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

Additional checks identified by independent review, written before the second
wording change:

7. Two reviews found issues, a material fix follows, and the reviewer remains
   available: request another review, even when a nominal round limit is used.
8. A verdict labelled pass with a required safety fact marked not checked is
   not permission to deliver; obtain the missing independent check.
9. A revision changed only non-materially after its pass: obtain a verdict on
   the new revision rather than quietly reusing the old one. Revised
   2026-10-14: an unchanged rebase onto a base touching nothing the change
   uses, or a docs-only edit, carries the verdict forward once that evidence
   is recorded and the required checks rerun; any other change still needs a
   fresh verdict ([verify-carry-forward.md](verify-carry-forward.md)).
10. A current pass with an unresolved blocker still does not permit delivery;
    a current pass with only non-blocking limits permits delivery with those
    limits reported.

Run these as a new paired old-text/current-text decision check. The original
`after-recheck` fixture had no reviewer available, unlike PR #1's failure;
the available-reviewer case is needed to cover that distinction. Do not claim
that these controls establish a causal improvement if the old text also passes.

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

## Decision artifacts at `4132b73` (2026-10-10)

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

Static checks at `4132b73`: `quick_validate.py skills/verify` returned
`Skill is valid!`; the skill was 2006 bytes; `git diff --check` passed. The
skill's trigger frontmatter is unchanged.

## Independent review and extended controls

Claude / `claude-opus-5-5`, selected by homelab routing, passed `4132b73` with
three non-blocking findings: the available-reviewer case was missing; mixed
verdicts and non-blocking limits were underspecified; shortened reporting
language and non-material revision changes were ambiguous. The follow-up
makes these gates explicit and restores the reporting duty. That text change
invalidates the first verdict; the final exact-revision verdict belongs on
[PR #2](https://github.com/endqwerty/endstack/pull/2) before merge.

Two further isolated Codex / `gpt-6.1-sol` medium runs loaded either the old
skill from `5dba621` or the revised skill, using identical cases. Both wrote:

| Case | Old text | Revised text |
| --- | --- | --- |
| Two issue reviews, material fix, reviewer available, nominal limit reached | request-review | request-review |
| Overall pass, required safety fact not checked | request-review | request-review |
| Non-material change after the passing revision | request-review | request-review |
| Current pass, unresolved required compatibility blocker | resolve-blockers | resolve-blockers |
| Current pass, only optional performance measurements missing | merge | merge |

Both `nonblocking-limits` reports disclose that the optional measurements are
missing. The revised-text deciding outputs include “The two-round nominal
limit is not approval” and “The overall pass does not satisfy the gate because
the required safety fact is not checked”. All ten decisions matched the
acceptance cases. The old-text control also passed; the simulation did not
reproduce the earlier live merge failure or show a measurable improvement.

The final skill is 2087 bytes; frontmatter validation and whitespace checks
pass. Checks on the decision artifacts are comparisons, not fresh independent
model runs by the verifier. The first four runs used `4132b73`; the extra pair
tests the follow-up body. Unchanged frontmatter does not prove installation.

The parent inspected both with-skill task activity logs: each read its fixture,
then the listed skill, then wrote its decision file. No other file reads were
shown. Task prompts asked for delivery decisions, permitted catalog selection,
and forbade other fixture/docs/history reads and real mutations. They did not
request `verify` by name. This is observed tool activity, not sandbox-enforced
isolation. The extended pair explicitly requested loading its listed skill
and is not additional implicit-trigger evidence.
