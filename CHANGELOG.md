# Change log

## 2026-10-11 — verify: re-review inputs; stale pending notes

- `verify`: a re-review gets the new revision range and the earlier findings,
  never the author's reasons for dismissing them. Found in the autopilot-full
  dry run, where the author re-asked with its own conclusion. Dropped the
  "Never verify your own work and call it independent" bullet, which step 3
  already says, to keep the size near 2 KB (2142 bytes).
- README and DISTILL.md no longer say the global rule is pending: homelab's
  short rule plus gate has landed. Still open: verifier launch command in
  `homelab route plan`, and `autopilot-full` direct pushes.

## 2026-10-10 — distribution docs

- Cookbook, README and DISTILL.md now describe installation through
  `homelab sync` from a pinned reviewed revision, with `$name` (Codex) and
  `/name` (Claude Code) entry points. Added docs/distribution-checks.md
  (installer evidence, installed-state checks, what is not checked) and
  docs/upstream-token-review.md (pstack PR #538 is already in our snapshot).

## 2026-10-10 — user-agnostic agent instructions

- Removed the owner's name and account from AGENTS.md. Describe the collection
  generically and reserve default review and merging for the user; delivery
  gates and the approved core skill set are unchanged.

## 2026-10-10 — separate delivery stages

- Added build, babysit, ship, autopilot-stack and autopilot-full alongside
  verify, following Daniel's explicit request after he merged PR #2. Building
  does not start watching; readiness is not merge permission; full autopilot
  requires a bounded queue and explicit landing authority.
- Added the command cookbook with prompts, outputs, stopping points and pstack
  source links. Replaced the combined hand-off/land roadmap; retained upstream
  sources and the superseded design as clearly labeled reference material.
- Changed this repository to review-first delivery. Other repositories, global
  rules and installation are unchanged. Recorded pre-implementation acceptance
  checks in `docs/delivery-checks.md`.
- Recorded paired 16-case Codex/Claude catalog and baseline decisions. Codex's
  baseline would reuse an older verdict if it remained applicable; both catalog
  runs required a fresh verdict, applying unchanged verify policy. These are
  bounded simulations, not installed discovery or causal improvement; Claude's
  baseline already respected that gate.
- Tightened babysit readiness even when no edit was made, kept dependency fixes
  inside the authorized scope, made build's stop explicit, and clarified the
  cookbook's immediate-merge example following independent and hosted review.
- Added an original SVG endstack icon and PNG export, with separate stacked
  bars and a terminal endpoint. The inherited pstack logo is unchanged.

## 2026-10-10 — model roles instead of setup-pstack

- Added `docs/model-roles.md`: pstack's per-role model setup mapped to five role
  classes and three effort profiles, kept in homelab's `routing.json` (landed
  there as `10c6450`, with `homelab route models`). Balanced runs Sonnet 5.5 and
  Sol 6.1 at medium or high; Opus only for the hardest tasks.

## 2026-10-10 — import of the pstack role skills

- Ported 23 role skills and 23 principles (as one `principles` skill) from
  `candidates/` to `skills/` with tool, model and harness names removed; skills
  now total 30. Not imported: make-bot-ui, setup-pstack, poteto-help,
  poteto-mode. Added `scripts/check-skills.py` (with tests) and the rules for
  imported role skills in AGENTS.md. Port notes: `docs/import-notes/`.
- Installing them through homelab still needs its allowlist and pin updated.

## 2026-10-10 — break from upstream pstack

- Daniel decided to stop tracking pstack. Deleted the Cursor-only material
  (`.cursor-plugin/`, `agents/`, `automations/`, `vendor/cursor-team-kit/`, the
  pstack README, `docs/guide/`, the inherited logo). The 52 pstack skills not yet
  imported moved to `candidates/` (indexed, not installed). The pre-cleanup tree
  is the git tag `pstack-snapshot`.
- `skills/` now holds exactly the six distilled skills, so
  `npx skills add <path-or-repo>` lists and installs only those.
- Renamed `assets/endstack-icon.{svg,png}` to `assets/icon.{svg,png}`; T3 Code
  looks for `assets/icon.png` (and `.svg`) as a project icon, and previously
  picked up the inherited `assets/logo.png`.

## 2026-10-10 — pointer-only check and delivery dry runs

- Recorded the pointer-only global rule check (`docs/pointer-only-checks.md`,
  33 run records): a bare pointer fails; a short rule with a skill-independent
  gate passed, reviewed by Codex. Homelab's change is prepared, not landed.
- Recorded real-pull-request dry runs of build, babysit, ship, autopilot-stack
  and autopilot-full (`docs/delivery-dry-runs.md`). No skill text changed.
  Open findings: verifier reachability, autopilot-full direct pushes, a
  verifier re-asked with the author's conclusion.

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
