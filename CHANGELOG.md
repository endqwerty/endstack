# Change log

## 2026-10-10 — current-revision verification gate

- Clarified `verify`: material fixes need fresh checks and an independent
  passing verdict on the current revision. A review limit never permits
  unverified delivery. This corrects the ambiguity exposed by PR #1's merge.
- Recorded paired Codex and Claude decision dry runs in
  `docs/verify-gate-checks.md`, including successful no-skill baselines and
  limits. Updated the README's stale day-zero status and kept installation
  and global-rule migration explicitly pending.
- Required passing safety evidence, a fresh verdict after any revision change,
  and reporting of unverified work and non-blocking limits. Extended controls
  against the old text also passed; no causal improvement is claimed.
- Recorded `hand-off` source analysis and planned checks without adding a new
  skill: the twice-recurring-failure condition is not yet established.

## 2026-10-10 — verify

- Added `skills/verify/` (distilled from principle-prove-it-works,
  interrogate, blast-radius). Upstream files kept until DISTILL.md step 5. Dry run recorded in DISTILL.md.

## 2026-10-10 — repository created

- pstack copied from `cursor/plugins@978ca6e` with the history of its folder
  (`git subtree split`), plus the three `cursor-team-kit` skills it links to
  under `vendor/`. Upstream README moved to `docs/pstack-readme.md`.
- Added README.md, AGENTS.md, DISTILL.md. Nothing distilled yet.
