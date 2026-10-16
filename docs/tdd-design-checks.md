# tdd: the design checks a bug fix needs, inline

Why: in the [design-step dry run](design-step.md), 0 of 5 Claude runs that
went through `tdd` opened `build`'s design step, even when `tdd` said "read it
and do it". The agents judged the fix small and skipped the pointer. All five
still fixed both clients, because `tdd`'s own fix step stated the
every-consumer rule and the second client was in plain view in a 150-line
fixture. A rule inside the skill being read is followed; a pointer to another
file is not. The Mainworthy miss this targets was a fix made in the iPhone
client and not in the web client, which reaches the same data through a
different call.

## Checks (written before the edits)

1. `python3 scripts/check-skills.py` and `python3 scripts/check-routing.py`
   print `0 problem(s)`; `python3 -m unittest discover -s scripts` passes;
   `tdd`'s SKILL.md stays under 6000 bytes.
2. `ROUTING.md` is unchanged, so homelab's copy still matches.
3. Dry run, with and without the change, on a fixture where the second
   consumer is not in view: the bug is reported against the command line;
   the web page and a chat digest pair the same two reads through a different
   call spelling, in other directories, among unrelated modules. The prompt
   names no skill or principle. Pass for "with": the change fixes all three
   consumers, or the reply names each one not fixed and why; and the reply
   lists the consumers checked. The "without" arm is reported as it comes out.

## What changed

`skills/tdd/SKILL.md` (4794 bytes):

- Step 1, after tracing the cause and before the test, lists four checks:
  find every consumer with the same fault, searching by what the code does
  rather than by its name or call spelling, and list each place; name the
  shape when the fix changes a type or a state; name and delete what the fix
  makes redundant; read `build`'s design step only when the fix crosses a
  function boundary or adds a module. The unconditional pointer to the design
  step is gone.
- Step 3 writes a failing test for each independently faulty place found;
  consumers that share one faulty implementation share one regression check on
  it (added after the independent review: 60 callers of one faulty parser need
  one test, not 60). Step 5 fixes each one or says why one is exempt.
- The subtract check keeps interfaces callers outside the repository may use,
  and the conditional pointer says `build`'s own design step still applies to
  every fix made under `build` (both from the review).
- The final response lists the consumers checked, which changed, and why any
  was left.

Turned down: routing every bug fix through `build` first. It changes the
routing line, and with it homelab's copy and the global rules, and costs a
one-line fix the full design pass, when the evidence says an inline rule is
what agents follow.

## Dry run (2026-10-16)

Fixture: [tdd-design-runs/fixture/](tdd-design-runs/fixture/), a 29-file,
408-line TypeScript CI gate. The command-line `show` reads the gate and then
the latest results through the typed `Api`
(`api.gate(change)`, `api.results(change)`); the web change page
(`src/web/pages/change.ts`) and the chat digest
(`src/integrations/chat/digest.ts`) pair the same two reads through
`call("gate", …)` and `call("results", …)`, among command, page and
integration modules that read only one of them. Prompt, the same as the
[design-step](design-step.md) port task: "Users report that `gatekeep show
feat` sometimes prints a passing verdict above results that contain
failures. It happens when CI pushes a new head while the command is running.
Fix it." Without: `main` at `a4e8b49`, whose `tdd` already says to read the
design step and to fix every consumer with the same fault. With: this branch.
Claude Code ran Sonnet 5.5 at medium effort with shell and file tools only;
Codex ran GPT 6.1 Sol at medium. Scoring:
[score.py](tdd-design-runs/score.py) (a file counts as read when its text is
in a tool result; "fixed" means the run's commits changed that file; every
final commit passes `bun test`).

| Arm, agent | Read `tdd` | Read design step | All three consumers fixed | Reply names the other two |
| --- | --- | --- | --- | --- |
| without, Claude ×7 | 7 of 7 | 5 of 7 | 3 of 7 (one fixed two, three fixed only `show`) | 3 of 7 (one named one) |
| with, Claude ×7 | 7 of 7 (new checks 7 of 7) | 0 of 7 | 7 of 7 | 7 of 7 |
| without, Codex ×2 | 2 of 2 | 2 of 2 | 2 of 2 | 2 of 2 |
| with, Codex ×2 | 2 of 2 | 2 of 2 | 2 of 2 | 2 of 2 |

Checks: 1 passes (`0 problem(s)` from both linters, 16 unit tests OK, 4576
bytes at the dry run, 4794 after the review) and 2 passes (`ROUTING.md` has no diff). Check 3 passes for "with": 9
of 9 runs fixed all three consumers and named them in the reply, against 5 of
9 without.

Read:

- The inline rule changed the code on the path that missed: Claude fixed
  every consumer in 7 of 7 runs with it, against 3 of 7 without.
- Reading the design step did not: five "without" Claude runs opened it, and
  three of those five still missed a consumer. One reply said it had "checked
  the other callers"; it had searched by the method name and found `list`,
  which reads only the gate, and not the two `call("results", …)` callers.
  "Search by what the faulty code does, not by its name or call spelling" is
  the line written for that.
- Codex found all three consumers on both arms; this fixture does not separate
  them for Codex.
- Two "with" runs went further and deleted the `results` operation, so the
  pairing can no longer be written; one of them committed once with two tests
  failing on the way and said so, its final commit passes.

## Not checked

- A repository the size of Mainworthy. This fixture is about 165 times
  smaller; there the search is harder and a consumer may be in another
  language (the iPhone client is Swift).
- Whether the shape and subtract checks fire on a fix that needs them; this
  bug has no shape change, though two runs subtracted unprompted.
- The review-driven wording (shared regression check, outside interfaces kept,
  the note about `build`) was added after the runs and not rerun. The fixture's
  three consumers each had their own faulty pairing, so it could not exercise
  the shared-implementation case.
- Seven samples per Claude cell and two per Codex cell are a sample, not a
  rate.
