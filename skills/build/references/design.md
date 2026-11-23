# Design before code

Do this before the first edit to production code for a feature or a change of
shape, and again at each phase boundary of a larger change: one line per step
that applies, `n/a` otherwise. A fix whose shape is already settled still does
step 1, and answers ground and tests in a sentence each.

1. **Principles.** Open the [principles index](../../principles/SKILL.md) now
   and read all of it: one page, one rule per line. For each principle whose
   situation matches this change, read its reference before the step it
   governs.
2. **Ground.** Trace where the behaviour lives and everything that uses the
   code you will change. List every consumer that does the same job (other
   clients, call sites, sibling functions with the same pattern) and change
   each, verified, or say why one is exempt.
3. **Shape.** Name the data shape before writing logic: the states, the data
   each carries, and the structure that holds them. List the combinations the
   domain forbids and make them unrepresentable. When the change adds a state
   to an existing shape, redesign the shape as if that state had been there
   from the start.
4. **Alternatives.** Non-trivial code that crosses a function boundary or adds
   a module: run [architect](../../architect/SKILL.md) first and take the
   shape it picks. Code waits for the remaining steps and, under a test-first
   workflow, for the failing test.
5. **Subtract.** Name what this change makes redundant and delete it in the
   same change.
6. **Failure.** For anything that can be retried, interrupted or run by two
   actors at once: what is the end state, and how does the next run
   recognise and reconcile what an interrupted one left behind?
7. **Tests.** A test that avoids a failing state, instead of fixing it, is a
   finding, not a pass.
8. **Order.** Order the work as small units that each end in a check.

## The design note

Write the outcome in a few lines: the shape and its structure, the consumers
and which ones change, and what is deleted. Name each principle that changed a
choice, with the choice, and leave the line out when none did. The note goes
into the pull request's "why this approach" and into every brief.

## The design doc

A new feature or a change of shape also gets a design doc in the repository,
so a fresh agent can resume or extend the work from the tree instead of from
the conversation. A fix whose shape was already settled needs only the note.

- **Where.** The place the project's rules name; otherwise
  `docs/design/<short-name>.md`, one per feature. Extending a feature updates
  its doc in the same change.
- **Sections**, written one at a time: *Problem* (plain sentences);
  *Goals* and *Non-goals*; *Plan* (the parts and how they fit, with risks and
  limits: failure modes, security, scale, and how each is handled);
  *Behaviour* (numbered scenarios, each "when … then …" about what a user or
  caller observes, each naming the test or command that proves it; edge and
  failure cases get their own); *Alternatives* (each option turned down and
  why); *Implementation* (every file created or changed, and why); *Tasks*
  (step 8's units in order, each marked done or open); *Open questions* (with
  the answer assumed meanwhile).
- **Test it.** Before the first edit to production code, run the EGM plugin's
  egm-review skill on the doc and resolve its findings with egm-resolve until
  the review converges. Keep its gates for the user unless the project's rules
  say to run EGM unattended; then answer each halt and resolve findings
  yourself, in stage order with fresh reviewers. Implementation follows the doc; a
  builder that has to depart from it updates the doc in the same change and
  says why.
- **Finish it.** When the build is done and before the final
  [verify](../../verify/SKILL.md) pass, in a commit of its own, delete
  *Implementation* and *Tasks*, make *Plan* describe the shape as built, and
  drop answered open questions. A scenario whose test
  [test-design](../../test-design/SKILL.md) dropped names the kept check that
  covers it instead, or, when none is kept, why the test was dropped and the
  pull request holding its proof. This rewrite needs no egm-review pass unless
  the build departed from the plan. What remains is the feature's spec record.
- **Later changes.** A change to the feature's behaviour adds, edits or
  removes its scenarios in the same change, and re-adds *Implementation* and
  *Tasks* while it is in progress if it needs a plan.
- The pull request links the doc and carries the note.

## Delegated builders

A builder gets the design note, the doc's scenarios where there is a doc, and
an instruction to read the principles index and this file before writing
code. A builder that finds the shape does not fit reports back instead of
redesigning alone. Review the returned diff against the note, not only
against the checks.
