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
  Step 5 now puts a finding in Act on or Consider only when it shows what
  reaches it: a reproducer, or a step-by-step trace from a caller, input or
  setting to the failure, through the real code (for a design, through the
  sketch and the code it would run on). Reviewer agreement draws attention
  but is not that evidence. Without it a finding is Noted; one the code rules
  out is Dismissed; a data-loss, security or trust-boundary finding that can
  be neither shown nor ruled out goes in Consider, marked unproven, with the
  check that would settle it. The reviewer prompt asks for that evidence and
  says a finding without it is a nit.
- `verify`: the verifier "shows" what reaches each issue, and "nothing shown
  reaches it" is the first kind of nit. The rubric defines "shown" (a check
  that fails on this revision, or a step-by-step code trace) and sends an
  unshown data-loss, security or trust-boundary finding to not checked, not
  to nit. `SKILL.md` stays under its 2,200-byte limit (2,196) by tightening
  three phrases with no change of meaning.
- Homelab's global rule (`agents/AGENTS.md`, "Decide for yourself") keeps a
  dissenter when opinions on a *choice* agree, and says a review of finished
  work gets none: its findings need evidence instead.

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
| interrogate, lead with three reviewers that all say "fix the remainder" | Briefed a fourth reviewer: "all three verdicts agreed ... the skill calls for one more reviewer to argue the opposite", and called the verdict unchallenged until it returns. Race: Dismissed. Path traversal: Dismissed, because "the party choosing the path already controls the process", which the fixture does not show. | "I did not convene any extra reviewer." Race: Noted, "Two reviewers agreeing drew my attention, but neither traced a concurrent caller." Path traversal: Consider, "can be neither shown nor ruled out", with the settling check "find the program that builds `config`". |
| verify, verifier given the same three concerns | Remainder: blocker with a reproducer. Race and path: "no finding", base code with no current path. | Same ranks. A return-type change it found itself: "nit ... nothing shown reaches it". |

Read: in `interrogate` the change does what it says. It saves a reviewer
round on a verdict that already had a reproducer, and replaces an unbacked
dismissal with an honest "unproven". In `verify` it changed nothing on this
fixture: the rubric already said to "trace a current path to an observable
failure ... before reporting it", and both arms did. There the change makes
the consequence explicit for the author, who re-ranks findings from
`SKILL.md`, and says where an unsettled safety finding goes.

Not exercised: a design review through `interrogate` (the sketch-trace
wording), a real multi-family panel, and arena (unchanged).
