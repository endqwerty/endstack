# Upstream role-skill updates at 190d287

## Why

Review on 2026-10-21 of selected upstream changes after endstack's
`978ca6e` snapshot, through `190d287` dated 2026-10-20. This is a bounded
port, not renewed upstream tracking. The author owns four skill directories
and this report plus [W5 import notes](import-notes/W5.md). The coordinator
integrates, publishes, and obtains independent verification.

## Checks planned before edits

- Run `python3 scripts/check-skills.py` and
  `python3 scripts/check-routing.py`. Both must report `0 problem(s)`.
- Run `python3 -m unittest discover -s scripts`. All tests must pass.
- Compare old and new skill decisions in isolated, tool-free sessions:
  usable launch from empty data, missing journey prerequisites and substitute
  setup, factual visuals, complete grouped calls, validated brands, existing
  opaque constructors, and a review with seven real findings.
- Inspect the full diff for assigned-file scope, retained invocation policies,
  entrypoints below 6000 bytes, and no tool or model coupling in skills.

## Progress

- Read repository rules, README, DISTILL, and W1-W4 import notes. Confirmed
  the assigned worktree is clean on `t3/port-role-skill-updates`.
- Read the upstream range diff and the nine named commits. Confirmed that
  interrogate also deletes useful context upstream, which this port will keep.
- Prepared paired scenarios and ran old-text sessions before the skill
  edits, with the baseline frozen at `b03c038`.
- Discarded an initial baseline batch because global Claude instructions
  appeared in an answer. Reruns use `--safe-mode` to disable instruction
  discovery and an explicit neutral system prompt, retaining the requested
  model, effort, empty tools, and no-session-persistence flags.

Baseline observation before skill edits: the brand scenario retains the cast,
"Decision: keep the parser as is." This reproduces the requested example
problem. The other baseline scenarios already reject premature readiness,
report the journey as unverified, preserve factual visuals, enumerate the
batch, keep the existing constructor, and retain all seven real findings.
Those decisions cannot count as measured uplift merely because the rules
become more explicit.

The first mechanical check caught a 6407-byte verification-skill entrypoint.
Moved its unchanged repo interview into a linked reference rather than cut
substance. The final-text launch and journey dry runs include that reference.

## What changed

- `create-verification-skill` requires usable launch from empty data,
  completed migrations and seeds, failed journeys for missing prerequisites,
  and disclosure of setup supplied by substitute environments. The unchanged
  repo interview moved to a linked reference to meet the entrypoint limit.
- `ketchup` reuses existing captures or factual diagrams while staying
  read-only. It discloses missing screenshots and never fabricates screens or
  starts an app for a capture. Grouped calls retain every item's link, user
  impact, evidence, risk, and recommendation. No word or diagram-box quota.
- `typescript-best-practices` narrows through a predicate backed by the real
  UUID validator. It explains that predicate bodies can lie and preserves
  established opaque constructors and schema validators.
- `interrogate` drops the five-item heuristic and its pressure to favor an
  incomplete verdict. Lead identity, context, filtering, and explained
  dismissals remain.

[W5](import-notes/W5.md) records each upstream commit and the portability
choices. The earlier author commits changed no routing, invocation metadata, shared
changelog, or other skill. The coordinator subsequently added the shared CHANGELOG entry
in `c67273c`.

## Checks

Final checks on the authored skill text:

| Command | Deciding output |
| --- | --- |
| `python3 scripts/check-skills.py` | `0 problem(s)` |
| `python3 scripts/check-routing.py` | `0 problem(s)` |
| `python3 -m unittest discover -s scripts` | `Ran 16 tests in 0.024s`, `OK` |
| `git diff --check` | No output, exit 0. |

The unit test command emitted existing unclosed-file `ResourceWarning`s in
checker and fixture code. They did not fail the suite. No tests were changed.
All four entrypoints are below 6000 bytes: verification 5129, ketchup 3968,
TypeScript 2888, interrogate 3598. The moved interview preserves its original text, apart from a trailing
blank line removed after the full-range whitespace check. Ketchup's explicit-only frontmatter and invocation
metadata remain unchanged. Diff inspection confirms edits are confined to
the four assigned skill directories and the two assigned reports.

## Dry run

Seven paired scenarios, one answer per arm, Claude Sonnet 5.5 at medium
effort, on 2026-10-21. The old arm reads endstack `b03c038`, not upstream's
snapshot. The new arm reads the authored text. All accepted commands exited
0. These are decision simulations, not independent verification.

Each process runs in a disposable directory created by `tempfile.mkdtemp`
(the Python equivalent of `mktemp -d`) and receives only one version of its skill text plus the scenario.
The baseline was frozen before edits, and its cast-retaining answer was
observed before implementing. TypeScript arms include `references/patterns.md`;
interrogate arms include `references/lead-judgment.md`. The final verification
arm also includes the moved `references/repo-interview.md`. Its old arm
already has that same text inline. Other linked references are not loaded.

The requested command is retained, with two isolation additions after an
initial batch exposed global-instruction contamination:

```sh
claude -p "$prompt" --model claude-sonnet-5-5 --effort medium --tools '' \
  --no-session-persistence --safe-mode \
  --system-prompt 'You decide scenarios using only the supplied guidance and facts. Do not use tools.' < /dev/null
```

Safe mode disables automatic instruction discovery while preserving normal
authentication. The discarded batch is not counted. The verification arms
were rerun after moving the interview. Ketchup and the moved interview changed only by blank-line cleanup
after their accepted runs. Every other accepted new arm uses the final
skill text. Scratch prompts and responses were removed after extracting the
following evidence.

| Scenario | Old-text decision and deciding line | New-text decision and deciding line | Observed difference |
| --- | --- | --- | --- |
| Empty-data launch answers its port before migrations and seeds finish. | Rejects readiness. "the launch section is not acceptable." | Rejects readiness. "A bare port check or DB health check may stay as an early progress step, but it must not count as ready." | No uplift. Baseline already requires complete initialization. |
| Missing seeded editor prevents sign-in/create/invite journey; admin-token demonstration ran in a container that installed, migrated, and seeded for an unprepared VM. | "The mapped journey is **not proven**." Reports missing editor and container setup as unverified. | "The mapped journey **failed**." Records the missing editor in `Gotchas`; "dependency install, migrations, and seeding as **unverified** on the VM." | More precise failure status and recording location. No uplift in rejecting the substitute proof or disclosing setup. |
| Settings shows saved timezone, no capture exists, app stopped, factual browser/API/database notes available. | "no app start, no capture, and no visual beyond a small text flow". | "Don't start the app, and don't generate a screen image." Says "No screenshot yet"; factual flow diagram optional. | No uplift in the decision. New answer uses the explicit missing-capture marker. |
| Four linked PRs share merge approval; each has user impact, tests, independent pass, and low or moderate risk. | Lists all four. "One action item: a single merge decision covering four PRs." Gives their impacts, evidence, and risks with a shared recommendation. | Lists all four, riskiest first. "Shared recommendation: merge all four." Each item has link, impact, evidence, and risk. | No uplift in completeness for this small batch. |
| UUID parser returns `input as AgentId`; alternative predicate always returns true. | "Decision: keep the parser as is." Rejects lying predicate. | "Decision: revise the parser, but only to remove the `as` cast." Uses `return isUUID(input)` in the guard and `return input` in the parser. "The compiler establishes **nothing** about validation." | Observed uplift for cast-free construction. Both reject the lying predicate. |
| Existing private-symbol AgentId and validated `AgentId.parse`; reviewer asks for the example's brand spelling and hand-written predicate. | "Decline the request." Keeps existing constructor by interpreting the rule's intent. | "Decline the request." Cites "Respect existing validated opaque-type constructors and schema validators". | No uplift. New guidance makes the existing good decision explicit. |
| Seven distinct, reachable, reproduced defects plus one variable-renaming preference; no follow-up patch. | "Act On: all seven confirmed issues. Dismissed: the variable-rename preference." Treats five-item rule as a heuristic. | "Act On (all seven)" and dismisses the preference with its reason. | No uplift. Both preserve the seven real findings and explain dismissal. |

The evidence supports one changed parser decision and a more precise journey
failure report. It does not establish improved reliability across agents,
large batches, or real applications.

## Reproduce the prompts

Each prompt uses this wrapper, followed by the named skill files and one
scenario below. No prompt identifies the intended change or supplies an
expected decision.

```text
Use only the supplied skill guidance and scenario. Do not use tools or read other files. Give your decision and its reason, quoting a short deciding line from the guidance where applicable. Keep the answer focused.

<guidance>
### SKILL.md
[full skill text from this arm]
[each included reference under its filename, with its full text]
</guidance>

<scenario>
[one scenario below]
</scenario>
```

### launch

Skill: `create-verification-skill`.

```text
A generated verification skill launches a service against an empty data directory. The port answers and database health is green, but migrations are still running and the seed account does not exist. Its launch instructions mark the app ready at the first answered port. Decide whether the launch section is acceptable and what readiness must require.
```

### journey

Skill: `create-verification-skill`.

```text
The mapped journey is: sign in as the seeded editor, create a workspace, then invite a teammate. The seed has no editor. An author instead uses an admin token to prove that creating a workspace works. The demonstration ran in a container whose entrypoint installs dependencies, migrates, and seeds; the intended fresh VM has none of those steps documented. Decide the status of the mapped journey and what the proof handoff must say.
```

### visuals

Skill: `ketchup`.

```text
The user requests a catch-up. A settings screen now shows the saved timezone, and the worker says it tested saving successfully. No screenshot or video exists. The app is stopped. You have factual notes showing save flows from browser to API to database. Choose what visuals, if any, to include, whether to start the app for a capture, and how to report the visible change. Do not perform actions.
```

### batch

Skill: `ketchup`.

```text
The user requests a catch-up on four PRs awaiting their merge approval. Each has passing tests and an independent pass. Links: https://example.com/pull/11 timezone display (cosmetic, low risk); https://example.com/pull/12 retry billing (prevents duplicate charges, concurrency test passed, moderate payment risk); https://example.com/pull/13 CSV download (unblocks exports, file check passed, low risk); https://example.com/pull/14 session expiry (signs out idle users, expiry test passed, moderate auth risk). They share one merge decision. A linked report contains details. Write the catch-up reply.
```

### brand

Skill: `typescript-best-practices`.

```text
A parser is `type AgentId = string & { readonly __brand: "AgentId" }; function parseAgentId(input: string): AgentId { if (!isUUID(input)) throw new Error("invalid"); return input as AgentId; }`. isUUID is the established runtime UUID validator. Decide whether to keep this parser or revise it, and show the result. Also assess the alternative predicate `function isAgentId(input: string): input is AgentId { return true; }`. What does the compiler establish about its validation?
```

### constructor

Skill: `typescript-best-practices`.

```text
A project consistently uses an opaque AgentId with a private unique-symbol brand. Its established AgentId.parse constructor validates UUIDs at runtime and returns that opaque type. Callers already use it and no unsafe conversion is proposed. A reviewer requests replacing this convention with `readonly __brand: "AgentId"` and a hand-written isAgentId predicate for consistency with your guidance. Decide whether to accept the request and explain why.
```

### findings

Skill: `interrogate`.

```text
You lead a review. Reviewers independently confirmed seven separate reproducible issues introduced by this change: cross-account invoice read, duplicate charge on retry, expired sessions accepted, timezone shift loses appointments, CSV formula injection, migration deletes existing labels, and export truncates the last row. Each has a reachable user path, a minimal reproduction, and a distinct fix. They also reported one preference for renaming a local variable, consistent with the repository. The release has no follow-up patch planned. Decide the Act On and Dismissed buckets and explain any filtering.
```

## Author commits

Original branch: `t3/port-role-skill-updates`, based on `b03c038`. The
coordinator rebased the port onto `t3/1b3c946a-role-skills`; the SHAs below
name those rebased commits.

- `d10053d`: usable launch, complete journeys, and moved repo interview.
- `21c0afa`: factual visuals and complete catch-up calls.
- `01b5a15`: branded narrowing and existing-constructor guidance.
- `97a14ef`: review findings without numeric pressure.

The documentation commit `0187b02` adds this report and W5 import notes, and removes
a trailing blank line from the moved interview. These commits
are local for the coordinator to integrate. No push, pull request, merge, or
write to another checkout was performed.

## Not checked

No live application launch, captured screen, real generated verification skill,
production migration, large approval batch, compiler execution of the example,
or multi-family review panel was exercised. Independent verification and
publication belong to the coordinator. No claim
of an independent passing verdict is made by this implementation handoff.

## Follow-up round at c67273c

Branch: `t3/1b3c946a-role-skills-r2`, starting at `c67273c`. This round
addresses the independent verifier's notes on the earlier port. It restores
the interview gates in section 1 and ports ketchup's omitted no-invented-call
rule and its exception for unnecessary, unrequested irreversible steps already
waiting on the user. W5 and CHANGELOG record those changes. The author-commit
list above now uses the rebased SHAs, and the earlier no-changelog statement
is limited to the earlier author's commits. The optional cosmetic rewrite was
left out to keep the behavioral correction small.

Before editing, planned checks were the three repository checkers, a whitespace
check, byte limits, and paired decision simulations for a broken checkout,
no pending call, and an unrequested irreversible step. All old-text responses
completed before the first skill edit. Old means the skill at `c67273c`;
new means the final text in this round. These are old-text/without-fix and
new-text/with-fix controls, not no-skill controls.

### Retained runs

[Run files](upstream-190d287-role-skills-runs/) retain every exact prompt and
response. Filenames pair `r2-<scenario>-old` with `r2-<scenario>-new`.
`first-new` retains the initial revision's responses for all three scenarios;
`second-new` retains the irreversible-step response after the first wording
clarification. The final irreversible prompt uses the final ketchup text.
The no-call response uses an earlier ketchup revision differing only in the
irreversible-step exception, which that scenario does not exercise. The final
interview response uses the final verification-skill text. Empty stderr files
were omitted. Every command exited 0.

The runs used Claude Sonnet 5.5, medium effort, on 2026-10-21. Each process ran
from the same scratch directory created by `mktemp -d`, subsequently deleted.
Only the skill entrypoint was supplied, deliberately leaving its linked
interview unopened. No tools were enabled. The requested command was used
without the isolation additions of the earlier round:

```sh
claude -p "$prompt" --model claude-sonnet-5-5 --effort medium --tools '' \
  --no-session-persistence < /dev/null
```

Global instruction discovery was not disabled. The old interview response
mentions `unslop` and says "This working directory isn't a git repository,"
although neither fact is in the supplied scenario. This is contamination from
the execution context, so the runs do not isolate the skill as the only cause.
The raw responses retain those statements. These are simulations of proposed
next steps, not actual repository inspection, repairs, or independent review.

### Deciding lines and limits

- Interview, old: "Read the repo interview first" and "Diagnose the build
  failure before writing anything." It already defers generation and proposes
  code inspection. New: "Then I'll answer its five questions (surface, run,
  drive, observe, isolate) from the codebase" and "I won't generate a skill
  for an app that can't start." It makes the five-question inventory explicit.
  The new response checks the repository before asking about the missing
  module, but also proposes asking whether the user wants a fix. No general
  improvement in autonomy or reliable reference opening is established.
- No call, old: "Nothing is waiting on you." New: "Nothing waits on you,
  so there are no action items." Both avoid inventing a call. No measured
  uplift in this scenario.
- Irreversible step, old: "Delete the legacy export archive permanently?"
  followed by a nested options and recommendation brief. The first new arm
  also expands it into a nested brief, exposing the conflict with the later
  all-items summary rule. The second new arm uses one long bullet. After
  explicitly exempting this case from the brief and requiring one short
  sentence, final new keeps one bullet and no visual: "My recommendation is
  to leave the archive alone." It preserves the pending irreversible decision
  and drops the color cleanup, but still uses several sentences. **Partial
  adherence:** this run does not prove the short-sentence requirement works.
  No visuals appear in either arm.

### Follow-up checks and handoff

- `python3 scripts/check-skills.py`: `0 problem(s)`.
- `python3 scripts/check-routing.py`: `0 problem(s)`.
- `python3 -m unittest discover -s scripts`: `Ran 16 tests`, `OK`.
  Existing unclosed-file `ResourceWarning`s remain non-fatal.
- `git diff --check`: no output, exit 0.
- Final entrypoint sizes: create-verification-skill 5253 bytes; ketchup
  4315 bytes. Both are below 6000 bytes. Invocation metadata is unchanged.

Only the local follow-up branch is committed. No push, pull request, merge,
or write to another checkout was performed. Current-revision independent
verification belongs to the coordinator; this author handoff is unverified.
