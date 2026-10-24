---
name: reflect
description: Review this transcript for learnings and route each to an edit of an existing skill.
disable-model-invocation: true
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Find the active conversation's transcript using the workspace-scoped location supplied by the harness. Match its opening user prompt. Never search unrelated workspaces or private conversations. If no matching transcript is available, pass a tight digest of this session instead.

## 2. Give each reviewer its lens

Use separate workers in parallel if the harness has them; otherwise apply the three lenses yourself in sequence and disclose that they were not independent. Use a different model family for the tooling lens if available, preserving its distinct technical perspective. Reviewers may read connected sources for tickets, threads and traces cited in the transcript, but change nothing.

| Lens | Prompt template |
|---|---|
| Judgment: durable principles and synthesis | [Judgment reviewer](references/judgment-reviewer.md) |
| Tooling: technical conventions and agent self-sufficiency | [Tooling reviewer](references/tooling-reviewer.md) |
| Divergent: blind spots and second-order effects | [Divergent reviewer](references/divergent-reviewer.md) |

Pass each template verbatim, substituting the transcript path or digest where marked. Keep each reviewer's full findings for synthesis.

## 3. Synthesize

Give the [synthesizer](references/synthesizer.md) to a separate worker, if available; otherwise synthesize yourself and say so. Pass each reviewer's full output into the template. The synthesizer may spot-check cited context through connected read-only sources and returns Accepted / Rejected / Backlog lists.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog, but only a recurring defect; a preference or an experiment stays a revisable note (the [correct](../correct/SKILL.md) skill says which is which). See the [encode-lessons-in-structure](../principles/references/encode-lessons-in-structure.md) principle.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File each Backlog item to your team's devex or backlog tracker without waiting, where that writing is authorized. If it is not, report it as unfiled. Only the Accepted list waits for approval.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): use an available skill-authoring workflow and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): use an available skill-authoring workflow and run its description-optimization loop.
- `new skill via skill-authoring workflow: <kebab-name>`: use an available skill-authoring workflow. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
