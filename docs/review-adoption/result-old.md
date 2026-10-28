# Policy dry run: old bundle

Inputs (SHA-256):

- `/tmp/endstack-adopt.LsPF6j/old.md`: `4ceb20e6d036c33bd41886c570e931af8ea805a2acac31f22145b136a3fb97f5`
- `docs/review-adoption/scenarios.md`: `0d88aeffab8bb680c0642e101fc2b393ce410c63f1953a58c1f8bb36d52050e5`

The bundle has five files: verify `SKILL.md`, verify `references/carry-forward.md`,
and the principles references boundary-discipline, minimize-reader-load and
type-system-discipline. Quotes below come from it. "Review" means the
independent verifier in verify Author step 3.

## 1. Only a fresh same-provider session is available

- **Action:** Do not deliver it as verified. Report it as unverified.
- **Review needed:** Yes. Step 3 asks for "a read-only verifier from another
  provider. Without one, report unverified." A new session on the author's
  provider is not from another provider, whatever context it has seen.
- **Evidence:** The author's checks on the real artifact with their deciding
  lines (steps 1–2), plus an explicit unverified status.
- **Why:** This is a behaviour change, so the skill's description puts it in
  scope. The bundle allows no same-provider substitute. Settled.

## 2. Pure boolean transform, three-value input space exhaustively checked

- **Action:** Keep the exhaustive checks and their deciding lines, then send it
  to an independent verifier anyway.
- **Review needed:** Yes. The change alters behaviour (how one enum variant is
  handled), and the description covers "a behaviour ... change". The bundle has
  no exemption for small, pure or exhaustively checked changes.
- **Evidence:** All three inputs checked against the contract, with deciding
  lines. The verifier reruns them itself, names the safety fact (for example
  "the input type has exactly three variants and the match is exhaustive"),
  proves it on the real code and tries callers.
- **Why:** The bundle has no low-risk tier. Settled: review is required. Whether
  such a case *ought* to be exempt is a question the bundle does not address.

## 3. Two-line authorization bypass change with green unit tests

- **Action:** Refuse the exemption. Add checks on the real surface (the API or
  endpoint the authorization guards), with a failing check first if this fixes
  a bug. Then send it to an independent verifier.
- **Review needed:** Yes. The description names "auth" explicitly. Step 2 says
  "Green tests alone prove no behaviour." The bundle has no size exemption.
- **Evidence:** Deciding lines from real-surface checks covering allowed and
  denied paths. The verifier names the safety fact (who may now pass, and why
  that is intended), proves it or marks it unproven, and tries other inputs and
  callers.
- **Why:** "Data loss, security or a trust boundary is never a nit", so any
  issue found ranks at least should. Settled.

## 4. Otherwise eligible mechanical edit with an unrun required check

- **Action:** Run the required check before delivering.
- **Review needed:** The bundle does not settle this. It has no notion of an
  "eligible" mechanical edit. The description excludes "edits that change none
  of these" from verify altogether. In carry-forward, a prose-only edit "keeps
  the verdict" but must still "rerun the required checks". If the edit changes
  no behaviour, verify does not apply. If it does, a verifier is needed as in
  case 2.
- **Evidence:** Deciding lines from the required check, run on this revision.
- **Why:** Step 5 says "Deliver only on an independent pass of every required
  check", and the verifier rules say "an unrun check is not checked". Every
  branch of the bundle needs the run, so that part is settled. What "eligible"
  exempts is not.

## 5. Reviewer found nothing; author wants three more reviewers

- **Action:** The bundle requires one passing independent verdict. Before
  counting "found nothing" as a pass, confirm the report answers each required
  check with pass, issues or not checked, with deciding lines, names the safety
  fact and names the revision judged. If it does, deliver.
- **Review needed:** No further review is required. The bundle asks for "a
  read-only verifier" (singular). Extra reviewers are neither required nor
  forbidden.
- **Evidence:** The existing verdict's per-check answers and safety fact on the
  current revision.
- **Why:** Whether three more reviewers are wasteful, or are allowed in order
  to make the result "convincing", is not settled. No rule caps or discourages
  them.

## 6. Downstream pure consumer repeats checks the boundary schema already guarantees

- **Action:** Remove the repeated typeof-object and property-existence checks.
- **Review needed:** Not settled. If the checks are truly unreachable, removing
  them may change no behaviour, which would put the edit outside verify. The
  bundle does not say whether removing dead defensive checks counts as a
  behaviour change. If it is treated as one, a verifier is needed, and the
  safety fact is "every path into the consumer carries the parsed domain object".
- **Evidence:** That every caller passes the schema's output (types, or a
  traced call graph), so no raw data reaches the consumer.
- **Why:** Boundary-discipline: "Inside the system: typed data, error
  propagation, no re-validation. Trust the types." It also says: "No redundant
  nil checks deep in call chains if the boundary already validated", and its
  test is "Is this data crossing a system boundary right now? If not,
  validation is redundant." Type-system adds "Validate once at creation, trust
  the type downstream."

## 7. JSON import uses a cast; another function needs fresh authorization and current inventory

- **Action:**
  - Replace the cast with a parse function at the import boundary. Type-system:
    "External data is untyped until parsed"; "Trace each `any`, `as` ... to the
    boundary and validate there."
  - Keep the authorization decision and the inventory read in the function that
    needs them, at the time they are needed.
- **Review needed:** Yes, for both changes. The parse turns some inputs into
  errors, which is a behaviour change. The authorization part is auth, which
  the description names.
- **Evidence:** Checks that malformed JSON is rejected at import. Checks that
  authorization is decided at use, for example that a revoked permission is
  denied even though the stored object passed shape validation earlier. The
  verifier names the safety fact for each.
- **Why:** The bundle's "no re-validation" rule covers shape and type
  guarantees only. Nothing in it addresses how fresh an authorization decision
  or an inventory read must be. Read literally, "Trust the types" could be
  misapplied to skip the authorization check. The separation into shape at the
  boundary and authorization at use follows from the problem, not from the
  bundle. Not settled by the bundle beyond the parse. One partial pointer:
  boundary-discipline lists "database rows" as external data, so reading the
  stored object is itself a boundary.

## 8. One-caller `parseConfig` versus a proposed `processValue` for two arithmetic statements

- **Action:** Keep `parseConfig`. Do not extract `processValue`.
- **Review needed:** No. Extracting or inlining code changes no behaviour, so
  verify's description excludes it.
- **Evidence:** None beyond a no-behaviour-change refactor.
- **Why:**
  - `parseConfig` hides meaningful decisions (external parsing and detailed
    errors). Minimize-reader-load says "Prefer boundaries that hide meaningful
    decisions", and boundary-discipline wants "Parse functions: pure transforms
    from raw bytes to typed state" at each boundary.
  - `processValue` adds a layer and a vague name with nothing hidden, so it fails
    the test "does it reduce reader load elsewhere by at least as much?"
  - Tension: "wrappers with one caller ... Inline them", read literally, also
    hits `parseConfig`. The qualifier "layers that cost more than they save"
    resolves it, but the bundle leaves that to judgment.

## 9. JSON parse failure at an HTTP handler, a swallowing internal catch, file cleanup

- **Action:**
  - **Catching:** Parse at the HTTP boundary and turn a parse failure into a
    meaningful client error there ("At boundaries ... validate, return errors,
    handle defensively").
  - **Propagation:** Remove the internal catch that logs and returns an empty
    success, and let errors propagate ("Inside the system: typed data, error
    propagation").
  - **Cleanup:** The bundle does not settle how to close files after failure.
    It has no rule on resource cleanup.
- **Review needed:** Yes. Error responses and the end of silent empty successes
  are behaviour changes.
- **Evidence:**
  - Checks on the real HTTP surface: invalid JSON returns the client error.
  - An internal failure now surfaces instead of returning empty success.
  - The verifier exercises failure paths ("Try to break it: ... failure
    paths").
- **Why:** The swallowed error is reached in ordinary use, so it ranks at least
  should. It may be data loss, which is "never a nit". Any cleanup rule beyond
  that would be filling a gap.

## 10. Wrong author credited in a source report; rename of a private local variable

- **Action:**
  - Rename: a nit (wording, no observable consequence). "Fix a nit only if
    small; declining one starts no round."
  - Attribution error: the bundle does not settle how to rank a factual error in
    a report. Its ranking scale is about code reached by use. "Wording" is the
    nearest category, which would make it a nit, but a wrong credit is a factual
    error, not style. "Blocker: the intended case is wrong" could also apply if
    the report's purpose is attribution.
- **Review needed:** No, for either, provided the report is not something an
  agent or tool reads as instructions. Neither changes behaviour, data, auth,
  money or deployment.
- **Evidence:** For the attribution, the source showing the correct author.
- **Why:** The rename is settled as a nit. The attribution is not settled. Under
  a literal reading it is an optional nit; I would fix it because it is small
  and factual, but that is judgment, not the bundle.

## 11. Change to agent delivery instructions with passing Markdown checks

- **Action:** No exemption. Run real checks of the instructions' effect, then
  get an independent verdict from another provider.
- **Review needed:** Yes. Carry-forward: "An agent's rules or skills, and
  anything else a tool or agent reads as instructions, are behaviour here, not
  docs." Step 2: "Green tests alone prove no behaviour."
- **Evidence:** Checks on the real surface, meaning what an agent does under the
  changed instructions, with deciding lines. The Markdown lint pass is
  necessary but not enough.
- **Why:** Settled. If this is a re-review after an earlier verdict, the
  "Patch changed only in tests, docs or lint configuration" section does not
  apply, because the instructions count as behaviour. "Anything else" applies.

## 12. Earlier passing verdict, then a behaviour change in response to a later finding

- **Action:**
  1. The earlier verdict does not carry forward. The patch changed beyond tests,
     docs or prose, so carry-forward's "Anything else" applies: "A fresh verdict
     on the current revision."
  2. Fix the finding with "the cheapest check catching them again" and rerun
     the affected checks (step 5).
  3. Brief the verifier with "the change since the last verdict, what it
     affects and open findings" (step 4).
  4. Record the revision, base and patch identity at the new verdict.
- **Review needed:** Yes. "One verifier is enough after ... a small fix; a full
  review again is for new behaviour, a redesign or a large new diff."
- **Evidence:** A fresh independent pass on this revision covering every
  required check and the safety fact, with no blocker or should open (step 5).
- **Why:** "Never stand in for the comparison with ... a passing check from an
  older revision." If findings are still open after two rounds, step 6 applies:
  rethink, then at most two more rounds, then stop and report both sides.
  Settled.
