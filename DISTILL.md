# Distilling pstack into endstack

Goal: a small set of portable skills for Codex and Claude Code, each phrased as
outcomes and roles with no exact commands or harness features, that a
repository names in its `AGENTS.md`. Background and the merge-policy design:
`delivery-policy.md` in Daniel's homelab repository.

## Target shape

| endstack skill | Distilled from | Outcome |
| --- | --- | --- |
| `build` | feature, bug-fix, opening-a-pr | Implement, check and verify a non-draft PR; neither watch nor merge automatically. |
| `babysit` | babysit | Handle existing PR feedback and checks; stop at merge-ready. Status-only is one read-only pass. |
| `ship` | shipping | Explicitly authorized landing of identified, currently verified work; confirm destination. |
| `autopilot-stack` | autopilot-stack | Build a bounded, verified dependent PR chain; the operator lands it. |
| `autopilot-full` | autopilot-full | Compose build, babysit and ship for a bounded queue with explicit merge authority. |
| `verify` | principle-prove-it-works, interrogate (single reviewer), blast-radius | A verifier from a different provider than the author, read-only, answers each check pass / issues / not checked and tries to break the change; tied to the head it judged. |
| PR brief (inside `build`, not another skill) | opening-a-pr, technical-writing, unslop | Short, standalone why, what, approach, checks, deciding evidence and reviewer. |
| `repro-first` (later, on a second failure) | bug-fix, tdd, fix-root-causes | Reproduce before fixing; a failing check first. |

Daniel's existing homelab skills (`use-gpt-budget`, `trmnl-screens`) stay
where they are.

## Done

- `verify` (2026-10-10): `skills/verify/`. One skill for both roles (author
  asks, verifier answers). Mandatory for features, bug fixes and anything
  touching auth, data, money, credentials or deployment; skipped for docs,
  comments, and mechanical edits that change no behaviour, data or contract. "A different provider than yours" is stated without naming any;
  homelab routing decides who that is. Upstream `principle-prove-it-works`,
  `interrogate` and `blast-radius` stay until step 5, since other upstream
  skills still link to them. Do not shrink the global AGENTS.md paragraph until
  distribution exists and a pointer-only dry run passes. The original runs
  below predate installation; distribution evidence is recorded separately.

### Current-revision gate follow-up (2026-10-10)

PR #1 landed as `5dba621` without a passing verdict on its final revision.
The author treated “check again once” as permission to stop checking after
further material fixes. A fresh read-only Codex review of that merged revision
confirmed the ambiguity. `verify` now requires a passing independent verdict
on the current revision with no unresolved blockers; a review limit leaves
the change unverified, not mergeable.

[Checks and paired dry runs](docs/verify-gate-checks.md) keep the evidence and
limits. Both harnesses selected the skill from the fixture catalog and made
the safe decisions. Both no-skill baselines also succeeded, so this is not
evidence of an improvement over the existing global rule. Real installation,
pointer-only discovery and live remote delivery remain untested.

The follow-up also states that all required checks and the safety fact must
pass, any revision change needs a fresh verdict, and non-blocking limits must
be reported. Old-text/current-text controls cover available reviewers after
the nominal review limit, mixed verdicts, non-material revisions and blockers.
Both variants passed; this clarifies policy without claiming measured uplift.

### Core delivery separation (2026-10-10)

Daniel merged the verification follow-up (#2) as `b570bf1`, then explicitly
requested pstack's separate build, babysit, ship and two autopilot flows. This
supersedes the combined `hand-off`/`land` plan. The core split is directly
authorized, not justified by invented repeated failures. The twice-failure rule
still governs speculative additions. Crosspoint-reader #28 merged under its
project's rules; it is not evidence of an unauthorized merge.

The five new core skills join `verify`. Endstack's own delivery becomes
review-first; Daniel merges unless he explicitly delegates identified landing.
See the [cookbook](docs/cookbook.md) for prompts, boundaries and pstack sources,
and [acceptance checks](docs/delivery-checks.md) for evidence and limitations.
The [old preparation](docs/hand-off-preparation.md) is historical, not policy.

All upstream playbooks remain verbatim because the mode, help and guide still
link to them. Do not install them alongside the distilled catalog. Distribution
selects only the six core skills at a reviewed revision. Migration of other
repositories/global rules remains separate; installing the skills does not
perform that migration.

### Pointer-only and delivery dry runs (2026-10-10)

Step 3's pointer-only check and step 4's dry runs, Claude first and a small
Codex pass after its allowance recovered. A bare pointer at `verify` **failed**
(the skill is not always loaded; "before you deliver" came after the edit), so
the global section becomes a short rule plus a gate that stands without the
skill, prepared in homelab on branch `pointer-verify` and not landed until an
independent verdict on its final revision. See
[pointer-only-checks.md](docs/pointer-only-checks.md) (arms, 33 run records,
Codex review of the wording) and
[delivery-dry-runs.md](docs/delivery-dry-runs.md) (real pull requests in a
throwaway private repository: build, babysit, ship, both autopilots, with and
without the skills). Baselines without the skills merged behaviour changes with
no real independent verdict twice; with them, once held and once verified. Open
from that: verifier reachability (`homelab route plan` names who, not how),
`autopilot-full` direct pushes to `main`, and re-asking a verifier with the
author's conclusion.

### `verify` dry run (2026-10-10)

Task: a planted off-by-one in a money calculation (`>` vs `>=` at exactly
$100.00), fix and deliver in a scratch repo. The global AGENTS.md verifier rule
was loaded in every run, so the baseline is "global rule only".

| Run | Result |
| --- | --- |
| Claude, without skill | Failing test first, fix, committed. Skipped the independent verifier ("one operator", scratch repo) but said so. |
| Claude, with skill (auto-triggered, no mention in the prompt) | Failing tests first, fix, then a Codex verifier reviewed the revision range read-only and ran a differential check over 140014 inputs; found only the intended change. Verdict tied to the range. |
| Codex, without skill | Failing tests first, fix, Claude reviewed independently before commit, then committed. |
| Codex, with skill (second try, after sign-in was fixed, text at `2e2146b`) | Read the skill unprompted ("using the verification skill because this changes money calculations"), failing check first, fix, asked a Claude reviewer for an independent verdict, got none, and reported the independent review as **not checked** instead of passing it. Commit was blocked by the scratch run's read-only sandbox, so no commit. An earlier try died on an expired login. |

Read: with the global rule loaded, Codex's baseline already obtained a
review, and the skill turned Claude's skipped review into a done one. The
Codex trigger fired once (one run). The real test is after the global
paragraph shrinks to a pointer.

Upstream `principle-prove-it-works`, `interrogate` and `blast-radius` are
still linked from 23 upstream files (poteto-mode, its playbooks, guide
chapters), so they stay until those are deleted (step 5).

## Upstream (decided 2026-10-10: broken from)

Daniel decided pstack is no longer tracked: endstack differs too much, and
future changes are taken by reading upstream and importing what is valuable,
not by fetching. Done in one cleanup:

- **Kept as reference:** the 52 pstack skills not yet imported, in
  [candidates/](candidates/README.md) with an index and import steps. They sit
  outside `skills/` so neither `npx skills add` nor `homelab sync` installs them.
- **Deleted:** `.cursor-plugin/`, `agents/` (Cursor agent definitions),
  `automations/benny/`, `vendor/cursor-team-kit/` (reference only; its ideas
  already went into `verify` and build's PR brief), the pstack README and the
  `docs/guide/` chapters, and the inherited pstack logo.
- **Recoverable:** everything above, and the old layout, is the git tag
  `pstack-snapshot` (`cursor/plugins@978ca6e` plus the pstack history).
- The three upstream skills replaced by `verify` and poteto-mode's replaced
  playbooks stay inside `candidates/` because other candidates link to them.
  There is no longer a step "delete the files a distilled skill replaces".

## Open questions

The [upstream prompt-reduction review](docs/upstream-token-review.md) confirms
that PR #538 is already in our retained snapshot and records a controlled
compression follow-up. Its reported byte/word reductions are not runtime token
measurements; distribution and pointer-only checks still precede global cleanup.

1. Distribution is decided: homelab's source manifest pins a reviewed endstack
   revision and six names; content stays here. See
   [distribution checks](docs/distribution-checks.md) for installation evidence.
2. Live delivery and cross-machine discovery: Claude ran the delivery skills
   against real pull requests on this machine (delivery-dry-runs.md); watching a
   pull request, Codex on a pull-request host and another machine are still
   untested. Keep those limits separate from earlier simulations.
3. Which other repositories should adopt review-first versus explicitly
   authorized full delivery? Do not migrate them as a side effect of this work.
4. Public or private repository. Private now; MIT allows either.

## Order

1. `verify` (smallest, already prose in the global AGENTS.md).
2. The five separated delivery skills and a human-facing cookbook.
3. Choose distribution, then deliberately assign repository delivery policies;
   shrink global instructions only after installed pointer-only checks pass.
4. Dry runs from a Codex thread and a Claude thread on each machine; record
   what differed.
5. ~~Delete the upstream files each distilled skill replaces.~~ Superseded by
   the break from upstream above.
