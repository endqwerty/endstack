# EGM import notes

> **Retired 2026-11-22.** endstack no longer ships this port: `goldfish`,
> `interview` and `drift` are deleted, and design work uses Google's EGM plugin
> itself, pinned by commit in [plugins.json](../../plugins.json). Why:
> [egm-plugin-trial.md](../egm-plugin-trial.md).

Source: `google/elephant-goldfish-model` at `72d06f5` (2026-11-15), Apache-2.0.
EGM is a plugin of seven skills and eight reviewer prompts built on Dave
Rensin's "Elephants, Goldfish" essay, the same source as `interview` and
`goldfish`. These notes record what the port kept, changed and dropped.
Evidence and dry run: [../egm-port.md](../egm-port.md).

## goldfish (from egm-review, egm-review-loop, egm-resolve, agents/, resources/)

Kept: the five review stages and their order (zoom out with the design-pattern
reviewer, comprehension, critic loop, zoom out again, readiness loop); the
split into a feature part and a detail part; the eight reviewer roles with
their review and concept modes; the merging worker, its retry-once and
`not run` rule, its report layout and its status-and-counts return; the
optional second instance of each reviewer; comprehension started directly so
the author reads its paraphrase; the loop rules (clean round, settled and
reopened findings, two clean rounds, five-round cap, churn); the resolve
categories (fix, contest, escalate, decline) and rules (checkable contests,
no contesting comprehension gaps, no changing a rank, the author's wish to
contest is not evidence); the design-pattern catalog with each pattern's cost
and the "No false compromise detected" exit; the feature-spec,
implementation-readiness and zoom-out standards.

Changed:

- Ranks keep endstack's `blocker`, `should`, `nit`, shared with `verify`,
  for EGM's Blocker, Major, Nit. Same meaning, one vocabulary.
- No human checkpoint between stages and no "auto accept" gate: the author
  runs the stages in order and fixes between them, because agents decide
  engineering questions themselves. The user is asked only for escalated
  findings and at the round cap or churn, one question at a time; without
  the user, both go to the doc's open questions or the report.
- Escalate always ends with the answer in the document. EGM's rule "do not
  add context only to satisfy a zero-context reader" is dropped: in endstack
  a fresh agent resuming from the doc is a real reader.
- Kept from goldfish and not in EGM: agent instruction files as targets
  (one goldfish, three passes, realistic tasks); readiness by realistic tasks,
  folded into the implementation-readiness role; a different model family if
  available; findings quote file and line; prefer cutting; a rule that keeps
  being missed becomes a check.
- The stage-3-only critic additions from endstack's design-doc specs (what a
  domain expert would add, scenarios missing or with weak checks) moved into
  the design-critic role.
- Reports go to a file outside the tree, not into chat or the repository.

Dropped: harness dispatch text and plugin paths; the repeated read-only
preamble per role (stated once); the tone charter and banned-adjective lists
(`unslop` and the brief's "agreeing is not help" cover them); presets and
gate option strings; the uninterrupted-flow traceability matrix; the
Heilmeier and re-implementation standards (EGM's own review stopped using the
latter for design docs; the former serves no stage); the structure role's
template rules beyond the project's design-doc layout.

## interview (from egm-brainstorm and egm-draft)

Kept: one question at a time; the concept review by seven reviewers through
a merging worker; the brief as a file with Overview, Goals and Non-goals,
Analysis, Alternatives weighed and Key decisions; rejections credited only
with a link; the draft reconciled against the brief, contradictions decided
by the user one at a time, and additions reported only when they change
architecture, an interface or a dependency; "do not make the doc match the
brief on your own".

Changed: the agent still proposes the first design (EGM has the author pick
among up to three unranked options); this keeps endstack's evidence that
proposing first exposes misunderstanding. Without the user, questions and
contradictions get assumed answers recorded as open questions. The brief
lives beside the design doc and is deleted once the doc is reconciled,
because two files describing one feature drift.

Dropped: per-section approval gates and the hand-off menu (publish as RFC,
draft, refine, stop); the draft's working file; the author-identity fallback
chain; the "Drafted with EGM" footer and sitemap registration.

## build design reference (from egm-draft's template)

Added *Goals* and *Non-goals*. EGM's Critical User Journeys are endstack's
*Behaviour* scenarios; its Verification Plan is the scenarios' named checks;
its non-functional requirements stay inside *Plan* and the risk questions of
the feature-spec standard.

## drift (from egm-drift-report)

Kept: one doc at a time from current files; only differences reported; the
categories missing behaviour, incomplete shape, shortcut and divergent design;
behaviour in the code that no doc covers counts as drift; note the missing
link so the next pass is cheaper.

Changed: expected behaviour is the doc's *Behaviour* scenarios and their
named checks, which the skill runs when local, read-only and cheap; added
changed behaviour, broken check and not-checkable categories; each difference
says which side should change (doc when history shows intent, code when a
check fails or a user decision is contradicted, else the user), where EGM
leaves it to the human.

Dropped: harness paths and the strict report heading format. Not ported:
`egm-bootstrap` (directory README contracts for large unfamiliar code bases;
no recurring need).
