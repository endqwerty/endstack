# Change log

## 2026-10-27 — A finding names what reaches it

Daniel asked twice in Mainworthy for fewer guards against states the design
rules out; agents kept adding them. Of 32 guards sampled there (30 asked for
by a verifier or the audit), 4 guarded nothing reachable; each rested on a bad
outcome with no present path to it ("a future parser could…"), three in a
finding and one in the author's own reasoning.

- `verify`: the verifier reports an issue only with what reaches it in this
  revision (input, a caller, stored or imported data, a race, a setting it
  accepts); what only later code makes is a note. The author fixes reachable findings. Wording
  trimmed to stay under the core size limit, with no change in meaning.
  Evidence and dry run: [docs/verify-reachable-findings.md](docs/verify-reachable-findings.md).

## 2026-10-23 — Fewer skills; corrections are classified; panels get a dissenter

From a review of how agents built Mainworthy: tentative remarks became fixed
rules, a first measurement became a ceiling, a Principles line became a parsed
CI gate, and unanimous panels went unchallenged.

- Dropped `autopilot-stack`, `automate-me`, `in-your-own-words`,
  `create-verification-skill` and `maintain-verification-skill`: unused in
  Daniel's transcripts (no project ever got a verification skill). Five core
  delivery skills remain. `autopilot-full` without landing authority builds
  each item and leaves landing to the user.
- ROUTING: every task first decides whether to `swarm`; `benchmark-checklist`
  covers any timing number reported, compared or turned into a limit.
- `correct` and `encode-lessons-in-structure`: classify a correction as a
  defect, preference or experiment; only a defect gets a guard, and a guard
  must cost less than the mistake. Preferences keep the user's words and stay
  open; a first measurement is a baseline. Before 1.0 any product or technical rule may go; safety, credential, money,
  publishing and merge rules stay.
- `build-the-lever`: build a tool when it saves work or makes the result
  checkable, not to show the principle was applied.
- `build` design step: a settled fix answers three steps; the Principles line
  is for a reader, not for a check to parse.
- `arena` and `interrogate`: when every candidate or reviewer agrees, one more
  argues the opposite before the verdict. Arena runs one dissenter per
  comparison, scores it on the rubric, and reframes at most once. `architect`: a past rationale is
  evidence, not a constraint. `reflect`: only a recurring defect goes to lint.
- `build` opens every pull request with each choice made for the user and how
  to reverse it; a correction goes through `correct` (a recurring defect gets a
  guard, a preference a note). `autopilot-full` also keeps a
  `show-me-your-work` decision log.

## 2026-10-21 — four new skills from upstream

- `sharpen` (asks what a top professional would add, their raw material,
  methods and an outside check, then hands back the rewritten prompt without
  doing the task) and `in-your-own-words` (restates the user's goal and
  problem): only when named, as in pstack.
- `create-formal-verification-skill` (verify one high-harm property tests
  rarely reach, show it fail on a broken variant, state bounds, and leave a
  project skill that records the covered code and its sync commit) and
  `maintain-formal-verification-skill` (bring that check back in line after
  the code changed, and tell drift from a bug). Explicit-invocation; ROUTING
  sends a request to prove or model-check a property (a race, an invariant, a
  case tests rarely reach), not an ordinary bug fix, to the first, and an
  existing formal check whose covered code changed since its sync commit to
  the second. create-verification-skill and create-formal-verification-skill link
  to each other.
- Port notes [W6](docs/import-notes/W6.md); dry run and limits:
  [docs/upstream-190d287-new-skills.md](docs/upstream-190d287-new-skills.md).

## 2026-10-21 — a verdict covers the patch, not the revision

- `verify`: step 5 points at a new reference, `references/carry-forward.md`,
  taken from pstack's shipping and autopilot playbooks. The same patch on a
  new base keeps its verdict; if the base changed something the patch uses,
  the change's checks run on the combined result and a pass keeps it. A patch
  changed only in tests, docs or lint configuration keeps each built check's
  result when the build matches apart from noise, and the changed part gets a
  scoped independent review. The patch identity keeps whitespace, so an
  indentation change is never the same patch. One verifier is enough after a conflict
  resolution or small fix. The verifier names the patch it judged, and a
  defect the base already has is not charged to the change unless the change
  copies it or newly reaches it.
- `autopilot-stack`: stack topology has one writer; builders never rebase or
  retarget.
- Why, dry run and limits: [docs/verify-carry-forward.md](docs/verify-carry-forward.md).

## 2026-10-21 — role skills follow upstream's later fixes

- `create-verification-skill`: ready means usable. Launch reaches a usable
  state from empty data, with migrations and seeds done; a journey whose
  prerequisite is missing fails instead of being weakened; a proof on a
  substitute environment lists the setup the real target still lacks. The
  repo interview moved to a reference (pstack `c49b37a`). The follow-up keeps
  its five-question interview and broken-checkout gates explicit at entry.
- `ketchup`: visuals only from what the work already produced, never a drawn
  or fabricated screen; every item of a grouped call keeps its own link,
  impact, evidence and risk, and no count or link replaces an item
  (`ea32d95`, `d00ba6e`, `c86f349`, `afd51cf`, `16541c6`, `bc14437`). Never
  invent a call. An unnecessary, unrequested irreversible step already waiting
  on the user gets one line and no visual.
- `typescript-best-practices`: a brand comes from a validating type guard, not
  a cast; a project's existing opaque-type constructor wins (`0317eb8`).
- `interrogate`: the lead no longer treats more than five findings as a sign
  of weak filtering (`99743e9`).
- Port notes [W5](docs/import-notes/W5.md); dry run and limits:
  [docs/upstream-190d287-role-skills.md](docs/upstream-190d287-role-skills.md).

## 2026-10-21 — four principles restated as reasoning; a readable design note

- `principles`: Attack the Premise, Fix Root Causes, Make Operations
  Idempotent and Test Behavior, Not Implementation take upstream's rewrites
  (pstack `e5136d8`, `36cecbf`): test the premise directly instead of a census;
  a guard is a fix only when the state it handles is legitimate, and a deep dig
  ends with a proposed always-on signal; derive each step from the state that
  exists; judge a test by breaking the behaviour and by changing the internals.
  `correct` step 3 and design steps 7 and 8 follow.
- `build`'s design note ends with one `Principles:` line (names and the choice
  each changed, or `n/a: <reason>`) that a project's checks can read.
  Mainworthy's description check now requires it: 3 of 169 of its pull
  requests since the design step named a principle, though agents read the
  index in nearly every code thread.
- Why, dry run and limits: [docs/upstream-190d287-principles.md](docs/upstream-190d287-principles.md).

## 2026-10-16 — lessons go into code, not into rules files

- `verify`: each real finding is fixed with a check that catches it again.
  To stay under the cap, the verifier's "do not accept the author's output"
  goes (running every check yourself already says it), and two phrases are
  shortened.
- `build`: a correction, or a mistake made before, gets the strongest guard
  `correct` names; an instruction-file rule is only for judgment.
- `ROUTING.md`: `correct` also routes when an agent is about to add a rule to
  AGENTS.md or another agent instruction file. `correct` gains a "One rule"
  section for that case: no repository sweep, one mistake taken down the
  levels, and a rule only if the user asked for it (one row naming its
  guard) or it still needs judgment.
- Why, dry run and limits: [docs/lessons-in-code.md](docs/lessons-in-code.md).

## 2026-10-16 — tdd: a bug fix finds every consumer itself

- `tdd` step 1 now carries the design checks a bug fix needs inline: find
  every consumer with the same fault by what the code does, not its name, and
  list them; name the shape if a type or state changes; delete what the fix
  makes redundant. It points at `build`'s design step only for a fix that
  crosses a function boundary or adds a module. Each independently faulty
  place gets a failing test and the fix (consumers of one faulty
  implementation share one check), and the reply lists the consumers checked.
- Dry run: Claude fixed all three consumers of a race in 7 of 7 runs with the
  change against 3 of 7 without. [docs/tdd-design-checks.md](docs/tdd-design-checks.md).

## 2026-10-16 — a design step before code

- `build` has a design step (`skills/build/references/design.md`), read and
  done before the first edit to production code: read the whole principles
  index, list every consumer, name the data shape and make impossible states
  unrepresentable, subtract, change every consumer with the same fault, think
  through retries, tests and the split of work. Its short note goes into the
  pull request and every brief; a delegated builder reads the index and the
  design step before coding. This is pstack's Feature playbook and
  `poteto-agent`, without the mode.
- `autopilot-full` and `autopilot-stack` do the design step before any code or
  brief for an item. `tdd` reads it, and its fix step now fixes the cause in
  every consumer with the same fault.
- `principles`: each entry states its rule, not only when it applies, so
  reading the index alone gives every rule.
- Dry run and limits: [docs/design-step.md](docs/design-step.md).

## 2026-10-15 — model roles: Gemini column removed

- `docs/model-roles.md` drops the Gemini column and the three-provider panel:
  homelab's `routing.json` routes only Codex and Claude now, since Gemini was
  unreliable in T3 Code. No skill changes: the skills never named a provider.

## 2026-10-14 — smaller catalog, verdicts carry forward, unslop checked

- The 24 explicit-invocation skills have `agents/openai.yaml` with
  `allow_implicit_invocation: false`, so Codex no longer lists them in every
  request; every description is at most 200 characters. Codex's endstack
  catalog falls from about 2,285 to 350 tokens a request, Claude Code's from
  415 to 291. `check-skills.py` enforces both. Evidence in
  [docs/catalog-size.md](docs/catalog-size.md).
- `verify`: a re-review covers what changed since the last verdict and what it
  can affect; a verdict carries forward over an unchanged rebase onto a base
  touching nothing the change uses, or prose no tool or agent reads as
  instructions, once the required
  checks are rerun. `ship` and `autopilot-stack` point at it. Dry run in
  [docs/verify-carry-forward.md](docs/verify-carry-forward.md).
- `unslop` checked: applied while writing it removed every counted pattern
  (0 against 50 hits in 80 runs); in real threads the effect is smaller. It
  stays. [docs/unslop-check.md](docs/unslop-check.md).

## 2026-10-14 — model roles: Gemini column

- `docs/model-roles.md` lists Gemini (Antigravity) beside Codex and Claude:
  homelab's `routing.json` now routes every Gemini role to Gemini 4 Argon
  (low, medium or high by class and profile) and no longer to Flash.

## 2026-10-12 — principle groups and step citations

- `principles`: the index is grouped again under upstream's Core, Architecture,
  Verification, Delegation and Meta (the port had flattened it to alphabetical
  order), and carries upstream's rule to name each principle that shaped a
  decision and the choice it changed, citing only references read this session.
- `build` and `tdd` cite a principle at the step it governs, as upstream's
  feature and bug-fix playbooks did. `build` names `fix-root-causes`,
  `model-the-domain` and `sequence-verifiable-units` (2131 bytes). `tdd` names
  `fix-root-causes`, `test-behavior-not-implementation` and
  `sequence-verifiable-units`, and commits the failing test before the fix.
- Dry run in `docs/principle-citations.md`: replies now name the principle and
  the choice (4 of 4 runs against 0 of 4 without the change), and the bug task reads
  `fix-root-causes` and commits the failing test first. The code the agent
  wrote did not change on either task. A linked principle was not opened until
  the skill said to read it.

## 2026-10-12 — routing index (replaces the dropped always-on router)

- Added `ROUTING.md`: one line per situation naming the skill to open, covering
  all 30 skills (1.9 KB; the pstack router was 19 KB). Homelab copies it into
  the global rules, since only those load every turn, so hidden skills are
  routed without growing the catalog. Prose now routes to `unslop` and docs to
  `technical-writing` inside any delivery skill, without editing the core
  skills' size caps. Added `scripts/check-routing.py` with tests. Merge skills route only on an
  explicit request, and `no-comments`, `tdd` and `architect` keep their own
  trigger limits (independent review found the first draft wider; casual skip no longer covers explaining or reviewing). Dry run and
  limits in `docs/routing.md`.

## 2026-10-11 — verify: re-review inputs; stale pending notes

- `verify`: a re-review covers the whole change through the new head, with the
  earlier findings, never the author's reasons for dismissing them (a hosted
  review noted that "the new range" could mean only the incremental diff). Found in the autopilot-full
  dry run, where the author re-asked with its own conclusion. Dropped the
  "Never verify your own work and call it independent" bullet, which step 3
  already says, to keep the size near 2 KB (2170 bytes).
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
