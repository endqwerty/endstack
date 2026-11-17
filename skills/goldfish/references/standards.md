# Document standards

Reviewers judge a design doc against the standard their role names in
[reviewers.md](reviewers.md). Each passes when a capable engineer, or a
fresh agent, new to the code base could do what it describes.

## Feature spec

Applies to the feature part of a design doc: everything before
*Implementation*.

A reader new to the code base understands the feature, why it is needed and
its trade-offs, and can confirm the major risks and alternatives were dealt
with.

- **Alternatives.** The doc fails if it proposes one path without showing
  that other workable designs were considered and turned down, each for a
  concrete technical or scope reason. A rejection is credited to the author
  or the user, or to anyone else only with a link to where they said it.
- **Risks and limits.** It names its own failure modes, security
  implications and scaling limits, and how each is handled.
- **Where they apply:** the problem, goals and non-goals, the plan
  (components, data flow, how it fits the system), behaviour scenarios, the
  alternatives, risks and their mitigations.

## Implementation readiness

Applies to *Implementation* and *Tasks*.

A reader new to the code base could make the right change on the first
attempt without guessing, asking or deciding the design.

- **Zero decisions.** The plan fails if the implementer must still choose a
  schema, an interface, a dependency or how to handle a new edge case.
- **Phases.** Work is split into units that each leave the code building and
  its checks passing.
- **Where they apply:** each file to create, change or delete, by its path
  (a glob only for generated files); the precise change in each; the test
  cases, including edges and failures, tied to the behaviour scenarios.

## Zoom out

Applies to the whole doc.

A design passes when it solves the root problem in the simplest way, reuses
what exists, avoids speculative features and early optimization, and keeps
its high-level parts at the level of components and interfaces.

0. **Context.** If the reviewer cannot tell what the doc is trying to achieve
   and why, the review fails at once and asks for that context.
1. **Root problem.** It fixes the cause, not a symptom, and fits the goals
   and design the project's own docs state.
2. **Simplicity.** No abstraction, path or feature only for a guessed future
   need; no caching, sharding or queues before a measured bottleneck; data
   passes through as few components as it can; interfaces leave room to grow
   without building the growth now.
3. **Altitude.** High-level sections describe architecture, interfaces and
   data flow, not helpers and loop variables. A structural fix in the right
   component beats a local workaround; new logic sits in the layer that owns
   it.
4. **Reuse.** Search for and reuse existing utilities and patterns, as long as
   they are maintained and do not cross a dependency boundary; prefer the
   platform's standard tools to bespoke ones; flag known anti-patterns such
   as bypassing authentication or hard-coded deployment settings.
