# New skills from de8ee15

## Purpose and checks defined before editing

Daniel requested ketchup-video and a standing orchestrator thread. Port the
video catch-up role and the program coordinator, preserving upstream judgment
while removing product-specific execution machinery. Work is restricted to the
two new skill directories, W8 notes and this evidence document and run directory.
The coordinator owns shared indexes, independent review, commits and publishing.

Before editing either skill, the acceptance checks are:

- Both entrypoints remain under 6,000 bytes, descriptions under 201 characters,
  portable links resolve, and explicit-only policy exists in both formats.
- Video preserves ketchup's catch-up window and user-only action items, slide
  continuity, no fabricated captures, subtitle strip, measured word-based holds,
  frame inspection, render failure fallback and the requested reply shape.
- Orchestrate preserves coordinator-only work, one branch owner, independent
  verifiers, pilot before fan-out, depth and concurrency guidance, retry limits,
  durable state, live-state reporting and real-decision-only escalation.
  Invoking orchestrate on a program grants its owners merge authority,
  limited to that program and ship/verify gates; the coordinator never merges.
  Explicit no-merge instructions stop owners at merge-ready.
- One tool-free with/without dry-run pair per skill, same fixture per pair,
  recording complete prompts, responses and deciding lines. No claims of real
  rendering or real delegated delivery from a planning test.
- Run `python3 scripts/check-skills.py` and
  `python3 -m unittest discover -s scripts`. Test proposed routing in a scratch
  root with the actual skills directory linked, never by editing ROUTING.md.
  Run the real routing checker too and record expected missing-index failures.

## Findings and limits

Upstream c742dd6 replaces orchestration scripts with coordinator judgment.
The port follows that revision, not its removed state database or script API.
No subagents, commits, pushes or PRs are part of this author handoff.

## Coordinator decision before dry runs

The coordinator relayed Daniel's confirmed decision: invoking orchestrate on a
program is the go-ahead for that program's PR owners to merge, like ship.
The coordinator never edits code or merges. Owners need a passing independent
verdict on the current head and ship's landing gates. The pilot reaches merge
before fan-out. Explicit "don't merge" or "build it, I'll land it" instructions
reserve landing for the user and stop owners at merge-ready. Model and effort
choice defer to the user's routing rules. This supersedes the initial brief's
requirement for separate program-level merge words. It follows upstream's
build-to-merge role and Daniel's confirmed preference. To reverse the default,
change orchestrate's authority paragraph and catalog/cookbook descriptions to
require separate explicit merge words, then rerun both authority fixtures.
The user can reserve landing for any individual program without changing the
skill. Authority excludes deployment, destruction and unrelated work.

## Final authority and early feedback decision

Daniel clarified: "Make orchestrate have landing authority. It should be even
more autopilot. It fully orchestrates the flow. It should prioritize asking
questions early to get feedback if it anticipates questions that may make it
want to not merge." This supersedes the preceding decision's escalation timing.
The coordinator fully drives build, verify, babysit and landing for every PR;
there is no later merge-approval question. Failing gates go back to owners for
resolution. Before the pilot, batch anticipated product/preference, irreversible-
step, scope and risk questions in one message with defaults. Unanswered questions
use stated defaults within existing authority; defaults cannot add excluded
permissions or override holds. Ask mid-program only about genuinely new decisions.
An explicit no-merge instruction still reserves landing. To reverse this policy,
change the authority and early-feedback paragraphs plus cookbook/route wording,
then rerun both the ordinary program pair and early-feedback fixture. An
individual program can override defaults or reserve landing without a skill edit.

## Proposed index edits

These are proposals only. The coordinator applies shared files and mirrors
routing into homelab's `agents/AGENTS.md`. Counts assume the 29-skill base;
combine with other concurrent imports before publishing.

### ROUTING.md

Current file: 2,552 bytes. Replace its introductory paragraph, between the
heading and first bullet, with:

```text
Before each task, match this index, open the matching skill and follow it.
If absent from the catalog, read it from your skills directory. Say which
skill shaped a decision. Several can apply. Casual chat, a one-fact lookup,
or the user opting out skips routing. Explanations and reviews are tasks.
```

Keep the current "Only when named" line, appending the following two lines
immediately after it without a blank line. This keeps both skills explicit-only.
Invoking orchestrate then carries the authority stated in that skill.

```text
`ketchup-video` for a video catch-up;
`orchestrate` for a multi-day program.
```

The complete proposed file is 2,537 bytes. The checker passes against a
scratch root pointing to the real skill directories. No real routing file
was edited by this author.

### README.md

Replace the state opening with:

```text
**State: five core delivery skills plus 26 imported role skills.** Build, babysit, ship,
```

Replace these two table rows, placing ketchup-video after ketchup and
orchestrate after swarm:

```text
| Explain and think | architect, how, why, teach, recall, figure-it-out, correct, ketchup, ketchup-video, sharpen |
| Review and process | reflect, interrogate, arena, swarm, orchestrate, show-me-your-work, benchmark-checklist, bro |
```

Replace the install count sentence with:

```text
Only `skills/` is installable (31 skills). Add `-s build -s verify ...` to take a subset.
```

### docs/cookbook.md

Add invocation-table rows:

```text
| ketchup-video | `$ketchup-video` | `/ketchup-video` |
| orchestrate | `$orchestrate` | `/orchestrate` |
```

Add deliverable-table rows:

```text
| [ketchup-video](../skills/ketchup-video/SKILL.md) | Named video catch-up since your last message | Silent subtitled video, followed by all user decisions in text |
| [orchestrate](../skills/orchestrate/SKILL.md) | Named multi-day program under one coordinator thread | Owners build, verify, handle readiness and land each PR; explicit no-merge stops at merge-ready |
```

Add copyable examples:

```text
**Video catch-up:**
> $ketchup-video Catch me up since my last message.

**Standing coordinator:**
> $orchestrate Own [program] through [checkable completion goal].
> Ask anticipated product and risk questions together before the first unit,
> with defaults. Do not deploy or expand the program.

Invoking orchestrate grants landing authority for the program. Its coordinator
never edits code or merges; each PR owner lands after independent verification
on the current head and required checks. The coordinator handles failed gates
through owners, without asking whether to merge. To reserve landing, add
"don't merge, I'll land it". Unanswered early questions use stated defaults
within the program's authority. Deployment and destructive actions remain excluded.
```

### CHANGELOG.md

Add under the current change group:

```text
- Add explicit-only ketchup-video: a checked silent subtitled catch-up video,
  with user decisions retained as text. Renderer choice stays with the agent.
- Add explicit-only orchestrate: one standing thread coordinates a multi-day
  program through delegated owners and independent verifiers. Invocation grants
  program landing authority; owners merge through ship/verify gates. Batch
  anticipated decisions early with defaults; explicit no-merge reserves landing.
  Ports, paired planning dry runs and limits: docs/new-skills-de8ee15.md.
```

### DISTILL.md

Append:

```text
### Video catch-up and standing coordinator (2026-11-10)

Daniel requested ketchup-video and orchestrate from pstack at de8ee15.
The former keeps the slide, subtitle and rendered-file checks with decisions
in text. The latter ports c742dd6's agentic program coordinator as a standalone
explicit-only role. Invoking it grants program landing authority, with
independent current-head verification and ship gates; explicit no-merge
reserves landing. The coordinator asks anticipated decisions early with
stated defaults and delegates code and landing to owners. See
[W8 notes](docs/import-notes/W8.md) and
[checks, dry runs and limits](docs/new-skills-de8ee15.md).
```

## Deterministic check evidence

Working base: `4897ee1a3c72ccc742aa5e50452bfd9b155a278b`. These new files
are uncommitted author artifacts. Exact skill byte sizes and hashes are in
[new-skills-de8ee15-runs/skill-manifest.json](new-skills-de8ee15-runs/skill-manifest.json).

- `python3 scripts/check-skills.py`: `0 problem(s)`, exit 0.
- `python3 -m unittest discover -s scripts`: `Ran 17 tests`, `OK`, exit 0.
  Existing unclosed-file ResourceWarnings appeared; none caused failures.
- `python3 scripts/check-routing.py /tmp/tmp.6miKR9vCuZ/routing-root`:
  `0 problem(s)`, exit 0. Scratch ROUTING.md is 2,537 bytes and links to the
  checkout's actual skills directory. The original is 2,552 bytes.
- `python3 scripts/check-routing.py`: `skill ketchup-video is not routed`,
  `skill orchestrate is not routed`, `2 problem(s)`, exit 1. Expected until
  the coordinator applies the proposed edit. No other routing errors.
- ketchup-video entrypoint: 3,925 bytes; orchestrate: 5,976 bytes. Each
  explicit-only policy file is 43 bytes. Descriptions and sibling links pass.

Check logs are in [the run directory](new-skills-de8ee15-runs/). This author
has not obtained independent review and does not call the behavior verified.

## Dry-run method and limits

Ran tool-free planning fixtures in `/tmp/tmp.6miKR9vCuZ`, outside the repo,
with `codex exec --ignore-user-config --ephemeral --skip-git-repo-check`,
model `gpt-6.1-sol`, medium effort, JSON events and final-message capture.
The dry-run calls were explicitly requested tests, not implementation delegates.
No agent in these tests could use tools under the fixture instruction. Logs
provide an event audit, not enforcement of that instruction.
Each pair uses the same common fixture and shared context; only the skill
under test is added in the with arm. Video shares ketchup. Orchestrate shares
ship, verify and autopilot-full. Prompts, complete responses, event logs,
stderr and return codes are saved handoff artifacts in the run directory.
The ordinary orchestrate-with and early-feedback scenarios were rerun after the
final authority clarification and size trim; the without arm is unchanged.

Ambient global instructions still appeared in the responses, including routing
model names and extra work-planning policy. Ignoring user configuration did not
remove those instructions. This is a within-environment comparison, not a clean
model-only experiment. All PR links and screenshots are fictional fixture data.
A placeholder in a planning reply is not an actual video artifact. No real
video, phone playback, rendering, live watcher, worker recovery, PR merge,
rebase, or multi-day resume has been exercised. These checks show planning
behavior on one sample per arm, not end-to-end delivery or broad reliability.

## Dry-run results and deciding lines

All five final runs exited 0. Every event log contains only `thread.started`,
`turn.started`, one `agent_message` and `turn.completed`; there are no tool,
command or delegation events. Output paths below contain the full responses.

### ketchup-video pair

Without: [response](new-skills-de8ee15-runs/ketchup-video-without.response.md).
The reply includes "The checkout boundary fix is ready" and separate capture
placement text, then action items. Its plan lists opening, checkout, receipt,
merge-decision and closing sections rather than a connected slide sequence.

With: [response](new-skills-de8ee15-runs/ketchup-video-with.response.md).
Deciding lines: "Use two slides on a persistent checkout-and-receipt canvas"
and "The subtitle strip would stay below the pictures at a consistent height."
It says "These are proposed holds, not measured playback" and requires
"checking frames, readability, subtitle placement, and added-word counts before
embedding." The reply starts "You have two decisions", then a clearly labeled
video placeholder, remaining assistant work and both user decisions as text.

Result: observed uplift in video planning and requested reply structure.
No uplift claimed for catching both decisions or choosing the correct window:
both arms do that with shared ketchup context. The test forbids rendering,
so no real timing, image quality or subtitle-readability claim is supported.

### orchestrate ordinary program pair

Without: [response](new-skills-de8ee15-runs/orchestrate-without.response.md).
Deciding lines: "merging awaiting explicit authority" and "Do you authorize me
to merge A–F into `main` ...?" It initially assigns A and E plus design and
coverage work, without a completed-pilot-before-fan-out rule.

With: [response](new-skills-de8ee15-runs/orchestrate-with.response.md).
Deciding lines: "The `orchestrate` invocation authorizes landing these six PRs"
and "Pilot A through owner, independent verifier and landing before fan-out.
E waits for that pilot despite being independent." The asks are "Nothing
initially" because that fixture has no unresolved product choices. It honors
"don't merge" by stopping every owner at verified merge-ready.

Result: observed uplift on authority, coordinator/owner roles and pilot sequencing.
Both arms preserve dependencies, independent current-head review, durable state
and no deployment. No uplift claimed on those shared delivery requirements.

### orchestrate early-feedback scenario

[Response](new-skills-de8ee15-runs/orchestrate-early-feedback.response.md).
The fixture adds reversible malformed-input and diagnostic-wording choices,
plus an optional irreversible purge outside the program. One up-front batch
asks "Should malformed legacy input be rejected or normalized?" and
"Should diagnostics preserve old wording or explain the new contract?" with
concrete defaults. It states "I'll proceed with these defaults if unanswered.
The old-data purge is outside this program and will not be performed."
At the later passing-A checkpoint: "Both defaults stand. A's owner checks live
mergeability, dependency readiness, holds and verdict/head alignment, then merges
A to `main`" and "No later question is needed unless a genuinely new decision
arises; failed gates, retries and rebases remain owner work."

Result: the requested early batch occurs before kickoff, unanswered defaults
proceed, the excluded irreversible action stays excluded, and no later merge-
approval question appears. One planning sample, not live merge evidence.

## Handoff status

Author work is complete within the allowed paths. No subagents, commits, pushes
or PRs were made. The coordinator still owns independent verification, shared
index application, final integrated checks and publication. These working-tree
artifacts are not an independent passing verdict.
