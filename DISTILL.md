# Distilling pstack into endstack

Goal: a small set of portable skills for Codex and Claude Code, each phrased as
outcomes and roles with no exact commands or harness features, that a
repository names in its `AGENTS.md`. Background and the merge-policy design:
`delivery-policy.md` in Daniel's homelab repository.

## Target shape

| endstack skill | Distilled from | Outcome |
| --- | --- | --- |
| `hand-off` | babysit, opening-a-pr, show-me-your-work (verdict only) | Build, check, verify, open a ready PR with a standing-alone description and the verifier's verdict posted; release the worktree, keep the branch; watch the PR for Daniel; never merge. |
| `land` | shipping, autopilot-full (owner loop only), opening-a-pr | `hand-off`, then merge with the project's mechanism, confirm the commit landed, clean up. |
| `verify` | principle-prove-it-works, interrogate (single reviewer), blast-radius | A verifier from a different provider than the author, read-only, answers each check pass / issues / not checked and tries to break the change; tied to the head it judged. |
| `pr-brief` (maybe folded into the two above) | opening-a-pr, technical-writing, unslop | About 40 lines: why, what, why this approach, verification with the deciding lines quoted, who verified. |
| `repro-first` (later, on a second failure) | bug-fix, tdd, fix-root-causes | Reproduce before fixing; a failing check first. |

Daniel's existing homelab skills (`use-gpt-budget`, `trmnl-screens`) stay
where they are.

## Done

- `verify` (2026-10-10): `skills/verify/`. One skill for both roles (author
  asks, verifier answers). Mandatory for features, bug fixes and anything
  touching auth, data, money, credentials or deployment; skipped for docs,
  comments, mechanical edits. "A different provider than yours" is stated without naming any;
  homelab routing decides who that is. Upstream `principle-prove-it-works`,
  `interrogate` and `blast-radius` stay until step 5, since other upstream
  skills still link to them. The global AGENTS.md paragraph shrinks to a pointer
  once the dry runs pass.

### `verify` dry run (2026-10-10)

Task: a planted off-by-one in a money calculation (`>` vs `>=` at exactly
$100.00), fix and deliver in a scratch repo. The global AGENTS.md verifier rule
was loaded in every run, so the baseline is "global rule only".

| Run | Result |
| --- | --- |
| Claude, without skill | Failing test first, fix, committed. Skipped the independent verifier ("one operator", scratch repo) but said so. |
| Claude, with skill (auto-triggered, no mention in the prompt) | Failing tests first, fix, then a Codex verifier reviewed the revision range read-only and ran a differential check over 140014 inputs; found only the intended change. Verdict tied to the range. |
| Codex, without skill | Failing tests first, fix, Claude reviewed independently before commit, then committed. |
| Codex, with skill (second try, after sign-in was fixed, current skill text) | Read the skill unprompted ("using the verification skill because this changes money calculations"), failing check first, fix, asked a Claude reviewer for an independent verdict, got none, and reported the independent review as **not checked** instead of passing it. Commit was blocked by the scratch run's read-only sandbox, so no commit. An earlier try died on an expired login. |

Read: with the global rule loaded, Codex's baseline already obtained a
review, and the skill turned Claude's skipped review into a done one. The
Codex trigger fired once (one run). The real test is after the global
paragraph shrinks to a pointer.

Upstream `principle-prove-it-works`, `interrogate` and `blast-radius` are
still linked from about 30 upstream files (poteto-mode, its playbooks, guide
chapters), so they stay until those are deleted (step 5).

## Triage of upstream (first pass, to be argued with)

- **Keep the idea, distill:** poteto-mode's merge gates and autonomy section,
  babysit, shipping, opening-a-pr, prove-it-works, interrogate, blast-radius,
  benchmark-checklist, unslop, technical-writing, correct (as a habit, not a
  skill), the principles as a reading list in docs, not as skills.
- **Drop:** poteto-mode as an always-on mode, the 23-playbook router, swarm,
  arena, orchestrate, autopilot-stack, hillclimb, visual-parity, eval,
  show-me-your-work's TSV trail, recall, ketchup, bro, make-bot-ui,
  automate-me, setup-pstack (models live in homelab's `routing.json`),
  poteto-help, the `benny` automations, the Cursor-specific agent definitions.
- **Vendored for reference only:** `vendor/cursor-team-kit/` (`deslop`,
  `control-cli`, `control-ui`); their ideas go into `verify` and `pr-brief`.

## Open questions

1. Distribution: sync endstack skills through `homelab sync` from this repo,
   or vendor the distilled skills into homelab's `skills/`? One source of
   truth either way; leaning towards homelab pulling from this repo.
2. Does `pr-brief` earn its own skill, or is it a section inside `hand-off`
   and `land`?
3. How is a skill's trigger tested across Codex and Claude Code without
   pstack's eval machinery? Proposed: a throwaway PR per harness, described in
   the skill's own PR.
4. Public or private repository. Private now; MIT allows either.

## Order

1. `verify` (smallest, already prose in the global AGENTS.md).
2. `hand-off`, then `land` (shares most of `hand-off`).
3. Casebook names `hand-off`; homelab and the other repos name `land`; the
   global AGENTS.md shrinks to point at them.
4. Dry runs from a Codex thread and a Claude thread on each machine; record
   what differed.
5. Delete the upstream files each distilled skill replaces.
