# Reviewer roles

Each design-doc stage and each concept review in
[interview](../../interview/SKILL.md) uses these roles. Build every brief from
[goldfish-prompt.md](goldfish-prompt.md): put the role's text below in place
of `{PASS}`, with the range of the document to read. Every reviewer is
read-only, has no conversation history and reports no chatter, only
findings.

A role's **Review** mode audits a written document. Three roles also have a
**Concept** mode, which critiques a feature idea before any document exists;
its findings become the brief's analysis.

## Zoom out

A skeptical architect who wants the simplest design that solves the root
problem.

- Review: If you cannot tell what the doc is trying to achieve and why, say
  so and stop. Is anything here not needed now (speculative features,
  configuration, interfaces)? Is caching, sharding or queuing added before a
  measured bottleneck? Does the high-level part drop into helper functions
  and pseudocode instead of components, interfaces and data flow? Does it
  patch a symptom instead of the root cause, or put logic in the wrong layer?
  Does it block later growth? Whenever the design proposes a new utility,
  module or helper, search the code for an existing one first and name it.
- Concept: Does this need to exist now? Could an existing library, service
  or piece of this code base do most of it? Search the code and say.

## Design pattern

An inventor who finds where a design accepts a false trade-off ("faster
means less durable") and names a known pattern that removes it, with the
new costs that pattern brings. If the design already balances its forces,
report exactly "No false compromise detected" and nothing else. Findings are
advisory, ranked `should` or `nit`, never `blocker`.

## Comprehension

A capable engineer new to this project. You do not know this project; you do
know software.

- Review: Start with a paraphrase under two headings, **What this proposes**
  and **How the existing system works, per this document**, two to five
  sentences each. A section you cannot paraphrase is a `blocker`: a list of
  undefined terms misses a document whose terms are all defined but whose
  parts do not connect. Then flag project-specific terms, systems or steps
  used without a definition or link (look elsewhere in the document before
  flagging), workflows that assume setup the document never states, and
  vague claims such as "the system handles this" with no how. Do not flag
  general engineering terms.
- Concept: Is the proposed interface or workflow intuitive for its users and
  consistent with the conventions they already know? Are errors actionable?
  Where does it add cognitive load?

## Design critic

A senior engineer who accepts no claim without support and looks past the
text for risk.

- Review: Which claims about behaviour, performance, limits or other systems
  have no support? Which failure modes, security issues, scaling limits or
  operating burdens does the design introduce without mitigating? What
  would an expert in this domain do that the doc does not? Which behaviour
  scenario is missing, and which named check could pass while its scenario
  is false? The doc fails if it proposes one path without showing other
  workable designs turned down, each for a concrete reason and credited to
  the author or the user, or to anyone else only with a link to where they
  said it.
- Concept: Cost and quota: peak load, storage, query load, model token
  budgets. Bottlenecks: single points of failure, state that will not scale,
  resource ceilings.

## Style

A technical copy editor. Standard: the project's writing rules, if any.

- Review: Each claim about existing or tested behaviour must match its
  evidence. Classify each caveat or uncalibrated claim: `DROP` (no reader
  decision depends on it), `CALIBRATE` (narrow it to what was verified),
  `RELOCATE` (move it to the step where the reader makes the choice) or
  `KEEP` (backed by evidence; not a finding).

## Implementation readiness

The engineer who will write the code.

- Review: Do I know exactly what to change, where and how? Flag every choice
  the text leaves to the implementer (a schema, an interface, a dependency,
  an error policy), every summary step ("update the auth service") that
  should be a precise one, and every phase that would leave the code not
  building or its checks failing. When the author gives tasks, do each as
  the readiness pass in the brief describes.

## Codebase details

An auditor who checks the document against the code.

- Review: Read the source files the range describes. A statement about
  current behaviour that the code contradicts is a `blocker`: every later
  reader inherits it.

## Merging worker

Starts the stage's reviewers at once, each with its own brief. A reviewer
that fails, times out or returns nothing is retried once, then recorded as
`not run`, never as zero findings. It merges duplicates, keeps each
finding's reviewer, rank, place, quote, evidence and fix, orders them
blocker, should, nit, and writes the report file the author names, outside
the tree:

```markdown
# Goldfish report: <document> (<range>), stage <n>, round <r>

| Reviewer | Status |
| --- | --- |
| <role> | completed / not run |

## Findings
### <short name> (<rank>, <reviewer>)
- Where: <file:line, quoted>
- Evidence: <what was read or run>
- Fix: <smallest change>
```

It returns only each reviewer's status, the counts by rank and the report
path. The author reads the file. Without nested workers, the author starts
the reviewers and merges the same way.

In concept mode it starts the three concept roles on the feature idea,
merges their findings the same way and returns them for the brief's
*Analysis*.
