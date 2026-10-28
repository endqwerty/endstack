# Paper dry run: new policy bundle against scenarios

Inputs (SHA256):

- `/tmp/endstack-adopt.LsPF6j/new.md`: `8fea489369e66b9c001d99207a09bf1e74fa8035da3f57561cdcd7a70efe9751`
- `docs/review-adoption/scenarios.md`: `0d88aeffab8bb680c0642e101fc2b393ce410c63f1953a58c1f8bb36d52050e5`

Policy applied literally: verify `SKILL.md`, `review-scope.md`, `review-rubric.md`,
`carry-forward.md`, and the principles references `boundary-discipline.md` and
`minimize-reader-load.md`. These are paper judgments, not runtime measurements.

## 1. Only a fresh session on the author's provider

- **Action:** Use that session as the one fresh, read-only verifier. Give it the
  task, the checks and the revision range, not the author's conclusions.
- **Review needed:** Yes. One fresh initial reviewer is the default, and an
  ordinary implementation change matches none of the exemption categories.
- **Evidence:** The verifier reruns every required check itself and reports the
  deciding lines, the safety fact it named (proven or unproven), ranked
  findings, and the revision and patch it judged.
- **Why:** review-scope: "The same provider or model family qualifies. A
  different family is optional ... it is not a gate." The session never saw the
  conversation and did not write the change, so it counts as independent.
- **Gap:** "Fully checked" does not establish that deterministic evidence covers
  the full affected contract, so this case has no basis for an exemption. The
  default applies.

## 2. A pure boolean transform with three exhaustively checked inputs

- **Action:** An exemption is allowed. Record the current revision, the changed
  contract, why the risk is low, the exact exhaustive check and its deciding
  output, why the check covers all affected behaviour (callers that consume
  this variant's result included), and any assumptions with proof that they
  hold.
- **Review needed:** No, if that record is complete. Required checks still run.
- **Evidence:** Output of the exhaustive three-value check against the explicit
  contract, on the current revision. There must be no unresolved safety fact.
- **Why:** review-scope lists "small bounded behavior changes whose full
  affected contract is established by deterministic evidence, such as an
  exhaustive finite input check". The case touches none of the excluded
  categories, and the project has no stricter rule.
- **Gap:** The wording is "may include", which permits the exemption without
  requiring it. The case does not say whether any caller's behaviour changes
  with this variant. The exemption depends on the record showing coverage of
  all affected behaviour.

## 3. A two-line authorization bypass with green unit tests

- **Action:** Refuse the exemption and get a fresh reviewer. If none can run,
  report the change as unverified and stop delivery. Do not lower the risk
  rating to get around the missing reviewer.
- **Review needed:** Yes.
- **Evidence:** Required checks run on the real artifact. The verifier names the
  authorization fact the change's safety rests on and proves it on the real
  code or marks it unproven, and it tries inputs, failure paths and callers.
- **Why:** review-scope: "Do not exempt changes to ... security or
  authorization" and "Size, a green test suite ... alone do not justify an
  exemption." SKILL.md: "security or a trust boundary is never a nit."

## 4. An eligible mechanical edit with an unrun required check

- **Action:** Run the check first. Until it passes on the current revision,
  there is no valid exemption and no delivery. If it cannot run, record the gap
  and report the change unverified, without delivering.
- **Review needed:** Not if the exemption becomes valid once the check passes.
  A review cannot stand in for the check.
- **Evidence:** The command, its deciding output and the revision.
- **Why:** review-scope: "An exemption skips model review, never required
  checks" and "An exemption has no ... missing required evidence." rubric: "A
  requested review can investigate the gap, but cannot turn it into a pass."
  SKILL.md: deliver "only with every required check ... proven on this
  revision".

## 5. A clean review, and the author wants three more reviewers

- **Action:** Decline the extra reviewers. Deliver on the first pass if every
  required check and safety fact is proven and nothing sits under "not
  checked".
- **Review needed:** No more review.
- **Evidence:** The first verdict: checks run with deciding lines, the safety
  fact proven, the revision and patch judged.
- **Why:** rubric: "No findings is a valid result" and "Do not add a reviewer
  just to seek more findings." A re-review happens only for fixes or new
  evidence that carry-forward requires.

## 6. A downstream consumer repeats checks the schema guarantees

- **Action:** Remove the downstream typeof-object and property-existence
  checks. Before removing them, name the guarantee: the schema parse at the
  owning boundary yields the domain object.
- **Review needed:** The question is about design. As a code change, it removes
  validation, so a reviewer would expect the guarantee named. The case does not
  say whether this change is exempt.
- **Evidence:** That the schema really parses the data (it is not a cast), and
  that no other path, such as a fresh import or external read, reaches the
  consumer without going through it.
- **Why:** boundary-discipline: "Do not defensively revalidate guarantees
  established by a schema ... Pass typed values inward instead of repeating
  object and property-existence checks." rubric: "Name the existing guarantee
  before removing validation."

## 7. A JSON import with a cast, plus an authorization and inventory decision

- **Action:** At the import, which is a new boundary, replace the cast with a
  parse into the domain type. In the other function, make a fresh authorization
  decision and read current inventory at the point of use. Earlier shape
  validation does not stand in for either.
- **Review needed:** As a code change, yes. It touches authorization, which is
  never exempt.
- **Evidence:** The reachable path through the unvalidated cast, which justifies
  the new parse. Proof that authorization is decided on current state.
- **Why:** boundary-discipline: "A cast or type annotation does not validate
  external data. Shape validation does not establish authorization or mutable
  business state." "A fresh import or external read is a new boundary.
  Checking ... a changing business condition is ordinary logic, not redundant
  validation."
- **Gap:** The policy calls these checks ordinary logic. It does not say which
  module or layer should hold the authorization decision.

## 8. Helpers: `parseConfig` and `processValue`

- **Action:** Keep `parseConfig`. It hides a complex boundary (external parsing
  with detailed errors) and has a clear, independent name. Do not extract
  `processValue`: the two statements are obvious arithmetic, the helper has a
  single use, and the name says nothing.
- **Review needed:** Not settled by the case. In a review, asking for
  `processValue` would need a concrete readability benefit, and none exists.
- **Evidence:** None beyond reading the code.
- **Why:** minimize-reader-load: "Do not extract single-use helpers
  preemptively ... unless the helper is reused, hides a complex boundary, or
  has a clear independent name" and "One caller alone is not a reason to remove
  a useful helper." rubric: name "the concrete readability ... benefit before
  requesting a helper".

## 9. Catching, propagation and cleanup around JSON parsing

- **Action:**
  - The HTTP handler catches the JSON parse failure in a narrow block around the
    parse only, translates it into a meaningful client error under the
    boundary's error contract, and keeps the original cause.
  - Remove the internal catch that logs and then returns an empty successful
    result. Let that error propagate.
  - Close files in `finally`, which runs on failure too and needs no catch.
- **Review needed:** Not settled by the case. It is design guidance, and the
  case gives no change classification.
- **Evidence:** A reachable invalid-JSON path that produces the client error,
  and proof that files close on the failure path.
- **Why:** boundary-discipline: "Catch errors where you can recover, translate
  them into the boundary's error contract, or add necessary context. Otherwise
  let them propagate. Keep the protected operation narrow, preserve the
  original cause, and do not turn unexpected failures into successful-looking
  defaults. Use finally for cleanup even when no catch is needed."
- **Gap:** The policy does not say whether a catch that logs and rethrows is
  allowed. It also does not set the client status code.

## 10. A wrong author credit, and a rename suggestion

- **Action:** Fix the wrong author credit, and use the cheapest check that would
  catch it again. Decline the rename without an edit or another round.
- **Review needed:** The credit is a finding to fix. The rename needs nothing.
- **Evidence:** The source showing the correct author.
- **Why:** rubric: "Factual errors in evidence or requirements are correctness
  defects, not wording nits" and "Skip style, naming". SKILL.md: "Decline nits
  without edits or another round."
- **Gap:** The policy does not settle whether the credit is a blocker or a
  should. That depends on whether the report's intended case is attribution.
  The policy also does not settle whether fixing it needs a fresh verdict:
  under carry-forward, a correction to plain prose keeps the verdict, but the
  case does not say what reads the report.

## 11. A change to agent delivery instructions with passing Markdown checks

- **Action:** The change cannot be exempted. Get a fresh reviewer. If none is
  available, report the change unverified and stop delivery.
- **Review needed:** Yes.
- **Evidence:** The Markdown checks are required, but they are not enough. The
  verifier runs them and reviews the instruction behaviour against the
  requirements.
- **Why:** review-scope: "Do not exempt changes to agent instructions." Under
  carry-forward, agent rules and skills "are behaviour here, not docs."

## 12. A behaviour change after an earlier passing verdict

- **Action:** The earlier verdict does not carry. Make a new exemption decision
  or get a fresh verdict on the current revision, covering what changed since
  the last verdict, what that can affect, and the earlier findings. Rerun the
  affected checks. Record the revision, the base and the patch identity. Count
  the round against the cap: after two rounds still open, rethink the approach;
  after at most two more, stop delivery and report both sides.
- **Review needed:** Yes, unless the new change itself qualifies for an
  exemption. One verifier is enough for a small fix. New behaviour, a redesign
  or a large diff gets a full review.
- **Evidence:** Checks proven on the new revision, and the re-review brief: the
  delta, what it affects, the open findings.
- **Why:** review-scope: "A new behavior change needs a new exemption decision
  or a fresh verdict." carry-forward, "Anything else", and SKILL.md steps 4 to
  6.
- **Gap:** The case does not describe the change, so whether an exemption
  applies, and whether one verifier or a full review is needed, stays open.
