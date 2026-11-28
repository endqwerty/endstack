# Review flow: one reviewer per provider, depth by blast radius (2026-11-27)

## Why

Daniel asked whether reviews earn their cost. Every non-exempt change got one
verifier from each of the other two providers, in parallel. Reviews of
Claude's work by GPT 6.2 Sol had become less useful than 6.1's: more
objections that did not hold. He wanted blast-radius back, combined with a
one-way or two-way door call, a light judge for loops, and fewer parallel
reviewers.

## What the record shows

A read of 194 merged PRs across endstack, bento-app, agent-factory,
mainworthy, ebook-manager and homelab (PR bodies, commit headlines, bot
comments; classified by agents, so judgment, not audit):

| | Count |
| --- | --- |
| PRs with a recorded finding | 151 of 194 (43 record none: unknown, not zero) |
| PRs with at least one real defect found | 132 (68%) |
| Real-defect rows | 304; wording 84, nit or declined 64, rebutted 1 |
| Real defects outside the diff | 81 of 304 (27%); endstack 29 of 53, mainworthy 17 of 41, agent-factory 12 of 84, ebook-manager 3 of 56 |
| Real defects a test, lint or script could have caught | 120 (39%); 88 could not, 93 unknown |
| PRs needing more than three rounds | 22 of 151 |

Code PRs yield real defects (228 rows); docs PRs mostly wording (42 of 52).
Escaped defects were few: endstack #48 (a pointer #43 cut), #14 (#13's design
step unread), agent-factory #141, mainworthy #1311, bento-app #45 (four bugs
found by property tests).

So review is worth keeping, and three things were true at once: a large share
of defects needed only a deterministic check, the defects outside the diff
cluster in agent instructions and stored data, and long round chains were
common.

## What outside guidance says

- Anthropic, 2026-11-16 ("How the Claude Code team thinks about
  verification"): "We don't try to improve reviews by stacking on more
  reviewers. Adding a second, more expensive, reviewer on top of the primary
  one is often a worse approach than tuning the primary." Rounds build on each
  other and re-review only the diff.
- Anthropic, 2026-10-15 ("Solving code review at Anthropic"): a three-round
  cap cut five-plus-round reviews from 8.9% to 1.5%; "Blast radius sets the
  bar"; the change sets the tier, not the author.
- arXiv 2610.01471: a top-tier cross-model reviewer was not significantly
  better than a same-model reviewer in a fresh session. arXiv 2607.21656: one
  direction of cross-model review lowered accuracy (91.4% to 82.8%).
- OpenAI: "We optimize for signal-to-noise first", and repository access with
  code execution "results in a stronger reviewer" ("A Practical Approach to
  Verifying Code at Scale"). Codex Code Review is tuned with review rules in
  the AGENTS.md nearest the code (developers.openai.com, Codex GitHub code
  reviews and "Custom Code Review rules for Codex"); a third-party guide says
  pull requests show only P0 and P1 findings, not confirmed here.
- Google's EGM: every Goldfish is a fresh subagent of the same harness, each
  on its own lens, with one re-audit per stage.

None of these sources describes reviewing one provider's work with another's
model. Anthropic's managed Code Review does run several agents on the diff in
parallel and then filters their findings, so "one reviewer" is the advice for
stacking whole reviewers, not a ban on parallel finders. Each vendor tunes its
review through its own repository rules file.

## What changed

- `verify`: one fresh verifier on the author's own provider; tune it rather
  than add a second. Homelab's global rules and router follow: another
  provider is never switched in, and a provider that cannot verify reports the
  work unverified. Panels, second opinions and `hard` seats stay on the
  thread's provider; Daniel picks the family by the thread he starts.
- `blast-radius` is back, routed, with a door call (what outlives a revert)
  and a rigor call that combines radius and door. The record says where it
  pays: instruction changes and stored data.
- `loop-judge`: from the third round of a loop on one goal, a light judge on
  the provider's gathering tier reads the goal, budget and attempt log and says
  continue, pivot or stop.
- Guards over reviewers, without a test deluge: `test-design` guards a class
  of mistakes (a type, then one check over the repository) before testing
  instances, and every added test is accounted for; `verify` makes an
  unaccounted test a should and asking for more tests a nit.

## Turned down

- A second verifier for one-way doors: the guidance says tune the primary;
  `blast-radius` instead requires the safety fact proven by running code.
- Watching suite size or time: a lagging signal that names no test to drop.
- Making routed skills visible to Claude in this change: the eval harness
  reads skills by path, so it cannot measure native loading (0 skill-tool calls
  in either arm, 0.95 vs 0.96); that needs real-session data.

## Not checked

The PR classification is agent judgment over PR bodies, not a defect audit,
and cost per review is not measured. Whether one same-provider verifier
misses defects two cross-provider ones caught will show in escaped defects
over the next weeks.
