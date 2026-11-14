# Interview, goldfish and design docs: paired dry run

Daniel reviewed Dave Rensin's "Elephants, Goldfish and the New Golden Age of
Software Engineering" (2026-04-27) against his setup and asked for three
changes: an interview before features, design docs kept in the repository as
well as in pull requests, and goldfish checks (fresh readers with no context)
on design docs and agent instruction files in every project.

## What changed

- `interview` (new, explicit): question the user before designing a feature,
  with assumed defaults; the agent proposes the first design; without the
  user, the assumed answers go into the doc's open questions.
- `goldfish` (new, explicit): comprehension, critic and readiness passes by
  fresh read-only readers; fix blockers and shoulds in the document; rerun
  with new readers until only nits remain.
- `build`'s design reference: a feature or change of shape gets a design doc
  in the tree (`docs/design/<short-name>.md` by default), tested with
  `goldfish` before the first production edit.
- ROUTING.md routes features to `interview` and documents to `goldfish`.

Turned down:

- Putting the interview in `build`'s SKILL.md. It is a core skill capped at
  2,200 bytes, and a bug fix or chore must not trigger it.
- Making the interview mandatory everywhere. Daniel's global rules favour
  agents deciding for themselves; the interview is for features shaped by his
  intent or taste, and projects can require it (mainworthy does).
- Replacing pull request descriptions with design docs. Daniel keeps PRs as
  the history; the doc holds what is true now.
- One goldfish per pass in every case. For routine checks of agent files one
  reader running all three passes in order is enough; design docs get three.

## Checks defined before running

Each scenario ran once with the old text (ROUTING.md and build's design
reference at the base) and once with the new (those two plus the interview
and goldfish skills), in fresh `codex exec` sessions (`codex-cli 0.169.0`,
`--ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check -s
read-only --json`, CLI default model), from a temporary directory outside the
repository, on 2026-11-13. Prompts, events and answers are in
[interview-goldfish-runs/](interview-goldfish-runs/).

1. User present, new feature ("export one run's evidence as a shareable
   report"): NEW interviews before designing, then writes the design doc and
   runs goldfish before code.
2. Settled bug fix (timestamps in UTC instead of local): neither arm
   interviews or writes a design doc. Guards against over-applying.
3. Delegated feature, user unavailable: NEW does not block; it records
   assumed answers as open questions in the doc.
4. "I just rewrote AGENTS.md; does it hold up?": NEW sends it to fresh
   readers, not a self-review.

## Results

| Case | Arm | Deciding line | Result |
| --- | --- | --- | --- |
| 1 | OLD | "I would write a short design note covering consumers, structure, deletions, and completion checks; then add a failing test" | Fail: one clarifying question, no interview, no doc in the tree |
| 1 | NEW | "I would ask who receives the report and what decision it supports; absent guidance, I would assume a teammate reviewing the run." … "I would run `goldfish`'s three fresh-reader passes concurrently … before implementation." | Pass |
| 2 | OLD | "I would implement the smallest settled fix, then run the regression and relevant existing checks." | Pass |
| 2 | NEW | "`interview` is unnecessary because the requested behavior is clear." | Pass |
| 3 | OLD | "reporting unresolved scope or a missing delegated design note to the parent, since the user is unavailable" | Fail: blocks on the parent |
| 3 | NEW | "With the user unavailable, I would record assumed answers about exported rows, columns, formatting, escaping, scale and failure behavior" | Pass |
| 4 | OLD | "I'll treat this as a review of agent instructions, using `verify`" | Fail: reviewer reads it with context; no fresh-reader test |
| 4 | NEW | "I would give separate fresh, read-only workers only the document paths and referenced files, withholding this conversation and my conclusions." | Pass |

All eight runs exited 0.

## Read of the result

NEW passes all four; OLD fails the three cases the change targets and passes
the guard. Case 3 showed a gap, fixed after the run: NEW said that without
separate workers it would stop. A delegated worker often may not start its
own; `goldfish` now hands the pass to whoever delegated the work instead of
stopping, or reports the document untested. Not re-run after that wording
change.

The same goldfish protocol was used for real on 2026-11-13 over the agent
docs of homelab (with `workstation.md`), endstack, mainworthy,
codex-reset-watch, the crosspoint-reader fork and novels, one Gemini reader
per project running all three passes. The endstack pass found that new skill
names must also be added to homelab's `skill-sources.json`, which nothing
here said; this change fixes that and the other confirmed findings.

## Routing only

The verifier noted that the runs above gave the model the full skill text, so
they did not show that ROUTING.md alone sends a request to the new skills.
After its review the goldfish route was reworded to the user's question ("Does
a design doc or agent rules file hold up for a fresh agent") and three runs
were made with only ROUTING.md as context, same CLI and flags
([interview-goldfish-runs/routing-only/](interview-goldfish-runs/routing-only/)):

| Scenario | Deciding line | Result |
| --- | --- | --- |
| "I just rewrote this repo's AGENTS.md. Does it hold up?" | "Open `goldfish` first to assess whether the rewritten rules hold up for a fresh agent." | Pass |
| User present, new feature | "Open `interview` first to clarify the report's audience, contents, format, and sharing expectations." | Pass |
| "Here's the diff for my fix … Is it safe to merge?" (guard: must not go to goldfish) | "Open `verify` first: “Is it safe to merge?” calls for checking the fix's safety." | Pass |

## Not checked

- Real sessions: these are stated next actions from one model, one sample
  each, not observed behaviour or a rate.
- Whether the interview's questions are good ones, or how long a real
  interview takes before the user stops it.
- Whether design docs stay current once written; nothing checks that a
  later change updates its doc.
