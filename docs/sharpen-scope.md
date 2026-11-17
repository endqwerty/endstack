# Keeping sharpen inside the user's scope

## Problem

`sharpen` says "deeper, not bigger", but in practice its rewrites grew. The
2026-10-20 import dry run already noted that "it adds many deliverables, so
this sample does not establish the 'not bigger' constraint"
([upstream-190d287-new-skills.md](upstream-190d287-new-skills.md)).

## Evidence from use

Fifteen Claude Code and Codex session transcripts from 2026-10-25 to
2026-11-14, delegated runs included, invoked `sharpen`. Four kinds of overreach show up, and each was followed by the user
pulling the scope back or correcting the rewrite:

- **Added deliverables and frameworks.** A request for a competitor review,
  SWOT and "what we'd do differently" came back asking for hands-on fixtures in
  every free tier, mined review-site complaints, a jobs-to-be-done grid,
  positioning, a Wardley-style map, a TOWS matrix, a pre-mortem and dated
  predictions. A CI cost request came back with DORA metrics, value-stream
  mapping, mutation testing, a seeded-defect benchmark with Fleiss' kappa, and
  cost "in four currencies" with "exchange rates". The user asked: "remove the
  currencies. why would I care about that?"
- **Research turned into delivery.** After "do it" on the review, the agent
  opened a pull request and ran the repository's checks and audit. The user
  asked: "why do you need to run tests, why are tests modified for a research
  question?"
- **Half-formed ideas hardened.** "Might be worth adding a flag to all
  entities noting if it's claimed and in use or unclaimed... idk" became a
  full ownership model ("Define ownership and demand alongside placement"),
  and "or leave it there for now and somehow mark it as available" became an
  open product question about visible abandoned experiments. The user then
  said they were optional, "only if feasible and able to be done without
  making the project overly complex".
- **Too many open choices.** Rewrites carried five or six bracketed choices
  with no recommendation. The UI-rubric session took four more turns of
  answers before "give me the full prompt now", and the CI session ended with
  "pick reasonable things based on what you know of the repo and my past
  conversations for the inputs that need me". In the backlog session the user
  answered "Do 1, 2, and 3", choosing a subset of the four answers.

## Change

The skill now defines deeper (rawer sources, better methods, an outside check)
against bigger (more deliverables, phases, frameworks, review rounds or
process). The rewrite keeps the user's deliverables. Anything new goes in a
"Left out" list of at most three lines that approving the rewrite does not
approve. Tentative ideas stay optional. A question stays a question. Inputs get
defaults from the repository and conversation, and at most three choices stay
open, each with a recommendation. Methods are named only when they change the
result, in plain words. Before returning, the agent lists the user's
deliverables beside the rewrite's and cuts what does not trace.

The upstream line "leave choices that are mine to make open instead of
deciding them" is replaced: users asked for defaults, not an open form.

## Dry run

Fresh read-only agents ran three past prompts with the old text and the new,
grounded in the current repositories (mainworthy and agent-factory). Each got
only the skill file and the prompt, and read the repository itself.

| Prompt | Old text | New text |
| --- | --- | --- |
| Competitor review, SWOT, "from day 1" | Kept the asks, added a TOWS matrix and a cross-provider claim check in the prompt; four "ask me before" items. | Six numbered items, each mapping to an ask; "Read-only: no code, tests or commits. Give the answer in chat"; three choices with recommendations; "Left out" holds the PR, the second-model check and interviews. |
| Factory placement idea ending "idk", "sharpen the ideas first" | "Then design ownership of standing entities as a set of users per entity"; "Lay out both options... without picking one"; three choices, no recommendations. | "You may add an owner record per placed entity... Skip it if removal works without it"; "Optionally, keep them and mark them unclaimed"; defaults filled ("default up to five"); two choices with recommendations; reuse matching left out. |
| "Review the todos" | Added a pilot dependency chain; one bracketed choice, "[Report only / also apply...: pick one]". | "Read them only; change nothing"; defaults stated (39 issues, `origin/main`, two weeks of CI); one choice with a recommendation; Linear changes, fixes and other states left out. |

Limits: one sample per arm. The old text also ran against repositories where
earlier work already existed, so its outputs were milder than the historical
ones. The comparison shows the new constraints being followed, not a measured
rate. No run used the CI cost prompt. After review, the "Left out" rule was
narrowed so answer 4's outside check stays in the prompt when it judges a
requested deliverable cheaply; the competitor-review run predates that and
left its second-model check out.
