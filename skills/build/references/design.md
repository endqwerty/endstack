# Design before code

Do this before the first edit to production code for a feature or a change of
shape, and again at each phase boundary of a larger change, one line per step
that applies. A fix whose shape is already settled answers steps 2, 6 and 8 in
a sentence each and skips the rest.

1. **Principles.** Open the [principles index](../../principles/SKILL.md) now
   and read all of it: one page, one rule per line. For each principle whose
   situation matches this change, read its reference before the step it
   governs.
2. **Ground.** Trace where the behaviour lives and everything that uses the
   code you will change, with the [how](../../how/SKILL.md) skill when the
   subsystem is unfamiliar. List every consumer that does the same job: other
   clients (web, mobile, command line), other call sites, sibling functions
   with the same pattern.
3. **Shape.** Name the data shape before writing logic: the states, the data
   each one carries, and the structure that holds them (one tagged value over
   independent flags and nullable fields, a table over branching, a parse at
   the boundary into a named type). List the combinations the shape allows
   that the domain does not, and make them unrepresentable. When the change
   adds a state to an existing shape, redesign the shape as if that state had
   been there from the start.
4. **Alternatives.** Non-trivial code that crosses a function boundary or adds
   a module: run [architect](../../architect/SKILL.md)'s ground and sketch
   phases, take its synthesized sketch as this step's shape, and return here.
   Its implement phase waits until the remaining steps are done and, under a
   test-first workflow, until the failing test exists. A change whose shape is
   already settled (a signature update across its callers, a bug with a clear
   fix) is `n/a`. Several valid shapes with no clear winner go to
   [arena](../../arena/SKILL.md); a contested one to
   [interrogate](../../interrogate/SKILL.md).
5. **Subtract.** Name what this change makes redundant (a check, a wrapper,
   an old path, a guard) and delete it in the same change.
6. **Every consumer.** A fix or improvement to behaviour several consumers
   share goes into each of them, each verified, or the note says why one is
   exempt. Fixing one client and leaving its sibling broken is an unfinished
   change.
7. **Failure.** For anything that can be retried, interrupted or run by two
   actors at once: what is the end state, and how does the next run
   recognise and reconcile what an interrupted one left behind? Split shared
   state before serializing it.
8. **Tests.** Each test calls the code the way its users do and asserts what
   the contract promises: it fails when that behaviour breaks and keeps
   passing when only the internals change. A test that avoids a failing state,
   instead of fixing it, is a finding, not a pass.
   A test written only to prove this change, where the cause cannot recur (a
   one-time script retired after its run, a removed path, a restated value),
   leaves the suite in its own last commit; keep one that a plausible later
   change could break unnoticed, including a migration new databases still run.
9. **Throughput.** Name the blocking first steps, the workstreams with
   disjoint files, and the smallest safe split. If one worker is best, say why.
   Order the work as small units that each end in a check.

## The design note

Write the outcome in a few lines: the shape and its structure, the consumers
and which ones change, and what is deleted. Name each principle that changed a choice, with the choice, and leave the
line out when none did. It is for a reader, not for a check to parse. The note goes into the pull request's "why this approach" and
into every brief.

## The design doc

A new feature or a change of shape also gets a design doc in the repository,
so a fresh agent can resume or extend the work from the tree instead of from
the conversation. A fix whose shape was already settled needs only the note.

- **Before.** When the feature's result depends on the user's intent or
  taste, run the [interview](../../interview/SKILL.md) skill before step 1
  and build the doc from its brief.
- **Where.** The place the project's rules name; otherwise
  `docs/design/<short-name>.md`, one per feature. Extending a feature updates
  its doc in the same change.
- **Sections**, written one at a time: *Problem* (a few plain sentences a
  casual reader understands); *Goals* and *Non-goals* (what it will and will
  not deliver); *Plan* (the parts and how they fit, a block
  diagram if it helps, light on jargon); *Behaviour* (numbered scenarios,
  each "when … then …" about what a user or caller observes, each naming the
  test or command that proves it; edge and failure cases get their own);
  *Alternatives* (each option turned down and why, so no later agent reopens
  it unknowingly); *Implementation* (every file created or changed, and why);
  *Tasks* (step 9's units in order, each marked done or open, so a new
  session resumes from the doc); *Open questions* (with the answer assumed
  meanwhile).
- **Test it.** Before the first edit to production code, run the
  [goldfish](../../goldfish/SKILL.md) skill on the doc and fix it until its
  review converges. Implementation follows the doc; a builder that has to depart
  from it updates the doc in the same change and says why. Mark tasks done as
  they land.
- **Finish it.** When the build is done and before the final
  [verify](../../verify/SKILL.md) pass, in a commit of its own, delete
  *Implementation* and *Tasks*, make *Plan* describe the shape as built, and
  drop answered open questions. A scenario whose test
  [test-design](../../test-design/SKILL.md) dropped names the kept check that
  covers it instead, or, when none is kept, why the test was dropped and the
  pull request holding its proof. This rewrite needs no goldfish pass unless the
  build departed from the plan. What remains is the feature's spec record;
  fixes after it that change behaviour update its scenarios.
- **Later changes.** A change to the feature's behaviour adds, edits or
  removes its scenarios in the same change, and re-adds *Implementation* and
  *Tasks* while it is in progress if it needs a plan. An older doc with
  *Checks* instead of *Behaviour* is converted when its feature next changes.
  Where a scenario and its test disagree, the test and code are the truth and
  the doc is fixed.
- The pull request links the doc and still carries the note: the pull request
  records what happened, the doc what is true now.

## Delegated builders

A builder gets the design note, the files it owns, the checks that prove it
done (the doc's scenarios, where there is a doc), and an instruction to read the principles index and this file before
writing code. A builder that finds the shape does not fit reports back instead
of redesigning alone. Review the returned diff against the note, not only
against the checks.
