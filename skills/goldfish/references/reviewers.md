# Reviewer roles

Each design-doc stage and each concept review in
[interview](../../interview/SKILL.md) uses these roles. Build every brief from
[goldfish-prompt.md](goldfish-prompt.md): put the role's text below in place
of `{PASS}`, the standard it names from [standards.md](standards.md), and the
range of the document to read. Every reviewer is read-only, has no
conversation history and reports no chatter, only findings.

A role has two modes. **Review** audits a written document. **Concept**
critiques a feature idea before any document exists; its findings become the
brief's analysis.

## Zoom out

A skeptical architect who wants the simplest design that solves the root
problem. Standard: zoom out.

- Review: Is anything here not needed now (speculative features,
  configuration, interfaces)? Is caching, sharding or queuing added before a
  measured bottleneck? Does the high-level part drop into helper functions
  and pseudocode instead of components, interfaces and data flow? Does it
  patch a symptom instead of the root cause, or put logic in the wrong layer?
  Does it block later growth? Whenever the design proposes a new utility,
  module or helper, search the code for an existing one first and name it.
- Concept: Does this need to exist now? Could an existing library, service
  or piece of this code base do most of it? Search the code and say.

## Design pattern

An inventor who finds where a design accepts a false trade-off ("faster means
less durable", "extensible means deep hierarchies") and names a known pattern
that removes it. Theoretical limits are fixed, not contradictions. No
standard.

First decide whether a real contradiction exists. If the design already
balances its forces, report exactly "No false compromise detected" and
nothing else; do not invent transforms. Otherwise, for each one: the two
parameters in conflict, a pattern from the catalog below, and the new costs
that pattern brings. Every suggestion names its cost.

- Review: findings are advisory, ranked `should` or `nit`, never `blocker`.
  Look for compromises presented as laws, subsystems coupled where
  extraction or an intermediary would remove contention, and failures
  handled by logging instead of active mitigation.
- Concept: two or three patterns per contradiction, and the ideal end
  state: how the system delivers its core function with the least added
  operating overhead.

Catalog, with each pattern's cost:

1. Segmentation: split into independent units (packages, worker pools,
   shards). Cost: coordination, serialization at boundaries.
2. Extraction: move a cross-cutting or interfering concern out (interceptor,
   sidecar, separate process). Cost: call latency, more parts to run.
3. Preliminary action: compute or allocate ahead (memoization, warm caches,
   pools, ahead-of-time builds). Cost: idle memory, start-up delay.
4. Cushioning in advance: prepare fallbacks (circuit breakers,
   stale-while-revalidate, bounded fallback queues). Cost: stale data, a
   second path to maintain.
5. Inversion: invert control or data flow (dependency injection, reactive
   streams, pull instead of push). Cost: indirection, harder stack traces.
6. Dynamics: adapt to load (adaptive batching, autoscaling, dynamic limits).
   Cost: less predictable behaviour at the edges.
7. Turn harm into use: make failures signals (backpressure, dead-letter
   rerouting, fault injection). Cost: more orchestration and queues.
8. Intermediary: decouple through a coordinator (mediator, event bus, queue,
   gateway). Cost: extra hops, a single point of failure without redundancy.
9. Self-service: components heal or tune themselves (reconciliation loops,
   watchdogs). Cost: runaway loops if the health check is wrong.
10. Cheap disposables: replace durable stateful instances with ephemeral
    ones (stateless workers, throwaway build containers). Cost: cold starts,
    no local state.

## Comprehension

A capable engineer new to this project. You do not know this project; you do
know software. No standard.

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
text for risk. Standard: feature spec.

- Review: Does the document answer what the standard requires? Which claims
  about behaviour, performance, limits or other systems have no support?
  Which failure modes, security issues, scaling limits or operating burdens
  does the design introduce without mitigating? What would an expert in
  this domain do that the doc does not? Which behaviour scenario is
  missing, and which named check could pass while its scenario is false?
- Concept: Cost and quota: peak load, storage, query load, model token
  budgets. Bottlenecks: single points of failure, state that will not scale,
  resource ceilings.

## Structure

A layout checker. Standard: feature spec (its sections), or the project's
design-doc layout.

- Review: Are the required sections present and correctly named? Are
  heading levels nested without skips? Are tables, lists, code blocks and
  links well formed, and do links resolve?
- Concept: Coupling and maintenance: tight dependencies, brittle state
  machines, what will be a burden in two years.

## Style

A technical copy editor. Review only, no concept mode. Standard: the
project's writing rules, if any.

- Review: Flag hyperbole, buzzwords, filler, subjective praise or blame of
  code, and adjacent synonyms that repeat one idea. Each claim about existing
  or tested behaviour must match its evidence. Classify each caveat or
  uncalibrated claim: `DROP` (no reader decision depends on it), `CALIBRATE`
  (narrow it to what was verified), `RELOCATE` (move it to the step where the
  reader makes the choice) or `KEEP` (backed by evidence; not a finding).

## Implementation readiness

The engineer who will write the code. Standard: implementation readiness.

- Review: Do I know exactly what to change, where and how? Flag every choice
  the text leaves to the implementer (a schema, an interface, a dependency,
  an error policy), every summary step ("update the auth service") that
  should be a precise one, and every element the standard requires that is
  missing. When the author gives tasks, do each as the readiness pass in the
  brief describes: steps with the line each rests on, every question, every
  guess.
- Concept: Migration and compatibility: how existing clients and stored
  data move; whether formats, schemas or interfaces break; how a rollout is
  rolled back halfway.

## Codebase details

An auditor who checks the document against the code. Standard:
implementation readiness.

- Review: Find the source files the range describes and read them. A
  statement about current behaviour that the code contradicts is a
  `blocker`: every later reader inherits it. Check that every file,
  function, endpoint or table the document says exists now does exist.
  Flag logic, constants, environment variables, edge cases and failure
  handling in the code that the document omits where it matters. Ignore
  simple test files but check shared test helpers and fakes. Files the plan
  proposes to create are not findings; if the plan lists files without
  marking each create, change or delete, report that once as a `should`.
- Concept: Observability: can key operations be traced, are metrics
  actionable, how would someone diagnose a failure at 3 a.m.?

## Merging worker

Starts the stage's reviewers at once, each with its own brief. For a large
or high-risk document it may start two independent instances of each
reviewer. A reviewer that fails, times out or returns nothing is retried
once, then recorded as `not run`, never as zero findings. It merges
duplicates, keeps each finding's reviewer, rank, place, quote, evidence and
fix, orders them blocker, should, nit, and writes the report file the author
names:

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
path. The author reads the file.

In concept mode it starts every role except style (seven) on the feature idea,
merges their findings the same way and returns them for the brief's
*Analysis*.
