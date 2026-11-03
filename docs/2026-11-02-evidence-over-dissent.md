# Review findings need evidence; interrogate drops its dissenter (2026-11-02)

## Why

Lauren Tan, pstack's author, posted that she now finds adversarial review
mostly a waste of tokens: reviewers who only read code get lost in nitpicks
and "you aren't gonna need it" objections. She would rather spend those tokens
on empirical checks (run it) and formal verification (prove it), and has cut
back pstack's use of `interrogate`, maybe to remove it later. An agent proposed
two endstack changes in response, and Daniel agreed to both: drop the step
that briefs one more reviewer to argue the opposite when everyone agrees, and
rank as a nit any review finding that no failing check or code trace backs.
The agent then kept arena's dissenter, for the reason below.

## What changed

- `interrogate`: the unanimous-verdict dissenter (added 2026-10-23) is gone.
  Step 5 now puts a finding in Act on or Consider only with evidence a reader
  can check, from a reviewer or the lead. For a defect: a reproducer, or a
  step-by-step trace from a caller, input or setting to the failure, through
  the real code (for a design, through the sketch and the code it would run
  on). For a structural finding from the code-quality lens: the lines, sites
  or existing helper it names, and the simpler version it proposes. Reviewer
  agreement draws attention but is not evidence. Without evidence a finding
  is Noted (whose definition now says so); one the code rules out is
  Dismissed; a data-loss, security or trust-boundary finding that can be
  neither shown nor ruled out goes in Consider, marked unproven, with the
  check that would settle it. The reviewer prompt asks for the same evidence;
  without it a finding is a nit, except a safety one, which keeps its
  severity marked unproven.
- `verify`: the verifier "shows" what reaches each issue, and "nothing shown
  reaches it" is the first kind of nit. The rubric defines "shown" (a check
  that fails on this revision, or a step-by-step code trace) and sends an
  unshown data-loss, security or trust-boundary finding to not checked, not
  to nit. `SKILL.md` stays under its 2,200-byte limit (2,196) by tightening
  four phrases with no change of meaning.
- Homelab's global rule (`agents/AGENTS.md`, "Decide for yourself") keeps a
  dissenter when opinions on which option to take agree, and says a review,
  of a change or of a single design, gets none: its findings need evidence
  instead. Committed in homelab, not here.

## Kept, and why

- **arena's dissenter.** Arena's dissenter builds a competing design and scores it on the
  rubric. That is a design compared on its merits, not an abstract
  critique of finished code. It is also the one dissent step with a
  recorded case: in [the 2026-10-23 dry runs](2026-10-23-learnings-dry-runs.md)
  (S3), arena's runners and judge converged on the demo-reseed design behind
  a 17-minute outage, and the dissent rule was what made the agent plan a
  dissenter aimed at the lock's scope and the startup trigger (planned, not
  run). Removing it from arena too is one
  paragraph in Phase E.
- **The global dissenter for choices**, for the same reason. Kept by the
  agent; dropping it is one sentence in homelab's `agents/AGENTS.md`.

Turned down: raising `verify`'s byte limit to fit a longer rule (the limit is
a project rule, and the rubric is where definitions go); removing
`interrogate` altogether (it stays opt-in, reached only for a contested
design or "tear this apart").

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes.
   ROUTING.md is unchanged, so homelab's copy still matches.
2. `interrogate` no longer mentions arguing the opposite of a unanimous
   verdict; `arena` is unchanged.
3. Dry run, with and without, on the same fixture (below). Pass for "with":
   interrogate briefs no dissenter, an untraced finding raised by two
   reviewers stays out of Act on and Consider, and an unsettled security
   finding is marked unproven with its settling check. The verify arm is
   reported as it comes out.

## Dry run

Fixture: a small Python repository, `splitbill`, with one commit that adds
`split(total_cents, people)` and prints each share; its docstring says the
shares add up to the total. It has one real bug (the remainder is dropped)
and three concerns raised without evidence: a race on a module-level dict
(no concurrent caller exists), path traversal through `config["codes_path"]`
(the fixture never shows who builds `config`) and an unused import. Each arm
was a fresh Claude Opus 5.5 agent that saw only its own copy of the skills
(`origin/main` `c56ff8f` or this branch) and was not told which. Outputs
were kept outside the repository; the deciding lines are quoted.

| Arm | Before (`c56ff8f`) | After (this branch) |
| --- | --- | --- |
| interrogate, lead with three reviewers that all say "fix the remainder" | Drafted a brief for a fourth reviewer and said it would wait for it (this dry run could not launch one): "all three verdicts agreed ... the skill calls for one more reviewer to argue the opposite", and called the verdict unchallenged until it returns. Race: Dismissed. Path traversal: Dismissed, because "the party choosing the path already controls the process", which the fixture does not show. | "I did not convene any extra reviewer." Race: Noted, "Two reviewers agreeing drew my attention, but neither traced a concurrent caller." Path traversal: Consider, "can be neither shown nor ruled out", with the settling check "find the program that builds `config`". |
| verify, verifier given the same three concerns | Remainder: blocker with a reproducer. Race and path: "no finding", base code with no current path. | Same ranks for the three given concerns. One it found itself (`main` now returns a list, not the total) went from "no finding" before to "nit ... nothing shown reaches it". |

Read: in `interrogate` the change does what it says. It saves a reviewer
round on a verdict that already had a reproducer, and replaces an unbacked
dismissal with an honest "unproven". In `verify` it moved one self-found
finding from "no finding" to an explicit nit and nothing else: the rubric
already said to "trace a current path to an observable failure ... before
reporting it", and both arms did. There the change makes the consequence
explicit for the author, who re-ranks findings from `SKILL.md`, and says
where an unsettled safety finding goes.

## Review

A fresh Claude Opus 5.5 verifier judged `ce62399` with the homelab diff:
no blockers, six shoulds. Fixed: the evidence rule had no form for the
code-quality lens's structural findings, which have no failure to trace;
the reviewer prompt made an unproven security finding a nit; Noted still
read "technically valid" while also holding unbacked findings (the race
landed there in the first run although the lead wrote "there is none");
the homelab sentence kept a dissenter for designs, which interrogate is
routed for; homelab had no CHANGELOG entry; and this record overstated
three results. Declined nits: "unrun is not checked" drops its noun (the
byte limit), and verify and interrogate treat an unproven safety finding in
untouched base code differently (verify keeps its base-defect rule;
interrogate reports what the panel raised).

Recheck: a fresh lead on the fixed `interrogate`, same panel plus two
structural findings, one backed ("`return after` became `return shares`")
and one not ("bill.py should be decomposed ... it mixes concerns"). The
backed one went to Consider; the other was Dismissed: "It names no lines
and offers no simpler version ... The file is 19 lines". The race went to
Noted ("Neither named a concurrent caller"), path traversal to Consider as
unproven, and no extra reviewer was briefed.

Not exercised: a design review through `interrogate` (the sketch-trace
wording), a real multi-family panel, reviewers running the new prompt, and
arena (unchanged).
