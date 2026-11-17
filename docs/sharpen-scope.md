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

## Root cause

Thirteen of the past outputs that contained a rewrite had three to eight
bullets under every question, and none said "nothing to add here". The old
text caused that in four ways:

- Every question had to be answered, and nothing tested whether an answer
  mattered, so each answer became a list.
- Nothing was judged against what the user wanted to get out of the task.
  "What a top professional would do" has no edge.
- "Rewrite my prompt to ask for exactly that" carried every answer into the
  prompt.
- "Leave choices that are mine to make open" handed every uncertainty back as
  a blank instead of deciding what evidence could settle.

A first fix capped counts (three open choices, a three-line "Left out" list).
That treats the symptom and can push an important item off the list, so it was
dropped.

## Change

The skill first states the goal: the decision, answer or change the task
serves. Everything is judged by one test: would it change that result, or how
far the user can trust it? What passes is kept, most important first. The rest
is dropped without being listed, and "nothing here would change the result" is
an allowed answer. The rewrite asks for the user's deliverables made deeper.
New deliverables, phases or artifacts that pass the test become proposals,
returned first with what they would change, and they stay out of the prompt
until taken. What the user asked for stays required, tentative ideas stay
optional, and a question stays a question.
The agent decides what evidence and the user's known preferences can settle,
says what it assumed, and asks only what changes the outcome and only the user
can answer, with a recommendation. Output order: goal, proposals and
questions, the four answers, the rewrite.

## Dry run

Fresh read-only agents ran past prompts against the current repositories
(mainworthy and agent-factory). Each got only the skill file and the prompt,
and read the repository itself. The old text ran on three prompts. The final
text ran on the competitor review, the factory idea and the CI cost prompt;
the historical output stands in for the old text on the CI cost prompt.

| Prompt | Old text | Final text |
| --- | --- | --- |
| Competitor review, SWOT, "from day 1" | Kept the asks, added a TOWS matrix and a cross-provider claim check in the prompt; four "ask me before" items. | Goal first. Top item: whether trial accounts may be used to load the repo's own CI output, "the biggest gap". Rewrite: "research only: no code, tests or commits", all five asks kept; committing the result is a proposal. |
| Factory placement idea ending "idk" | "Then design ownership of standing entities as a set of users per entity"; three open choices without recommendations. | Found the planner already plans before placing ghosts and entities already record owners. First question: "what prompted this, lines being skipped or fed by robots, or wanting a less regular layout?" Keep-for-reuse stays an option "you may take or drop". |
| CI cost and agent validation (historical old output) | Four "currencies" with "exchange rates", DORA, value-stream mapping, Fleiss' kappa, nine open brackets. | Top item: "Continue the 2026-11-07 delivery review instead of starting a new one", since it already measures this. Assumptions stated instead of asked. Replaying past bugs against a slimmer test plan is a proposal. |

Limits: one sample per prompt. The final text still lists several methods
under question 3 (the CI run named six, each with what it does here). The CI
run marked "workflows that could become features" optional, though the user
had listed it among the goals. After review the skill says "What I asked for
stays required". A rerun of the CI prompt with that line listed "Goals, all
required", features included, and again led with continuing the 2026-11-07
review. The comparison shows the test being applied, not a
measured rate.
