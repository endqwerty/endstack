# Four upstream skill ports

## Why

Daniel requested these four skills on 2026-10-21, from `cursor/plugins`
revision `190d287` (2026-10-20). This author owns only this worktree and local
commits. The coordinator handles integration, publication and independent
verification. This document records author checks, not an independent verdict.

## Checks defined before editing

- Both mechanical checkers must report `0 problem(s)` and all script unit tests
  must pass. Each new entrypoint must be below 6,000 bytes, each description at
  most 200 characters, and ROUTING.md at most 2,600 bytes.
- All four skills retain explicit-invocation frontmatter and the policy file.
- Compare each port with upstream for retained role, steps and judgment.
- Run old/new routing against six prompts with no tools. The formal routes
  should appear for a proof request and covered-code drift, but not a plain bug
  or casual question. The prompt helpers should require their names.
- Run one with/without pair per skill. Check prompt-only rewriting, goals-only
  restatement, code-grounded property selection, mutation sensitivity, scope
  limits, and honest labeling of generated-input testing.
- Keep quoted deciding output and disclose no-uplift rows and untested behavior.

## Progress

- Read repository rules, routing evidence, catalog rules and W1-W2 port notes.
  Read all four upstream entrypoints and their help/setup/guide connections.
  Working branch: `t3/add-formal-verification-skills`; checkout started clean.
- Preserve the upstream formal workflows. Replace the named model-checking
  default with selection by question. Keep prompt helpers user-invoked only.
  Keep this work separate from the coordinator's shared catalog updates.
- First mechanical run found two size overruns (6,020 and 6,017 bytes).
  Shortened only the new sibling sentence and moved the formal report to a
  reference; both checkers now report zero problems. Script tests passed.
- Initial dry-run results: the new index selected the intended formal pair and
  both named helpers. Neither index routed the ordinary bug or casual question
  to formal verification. The restatement arm preserved the open format choice
  but added discovery questions; the baseline emitted unavailable tool calls.

## Follow-up round 2

The coordinator found that sharpen's added "Return only the rewritten prompt"
contradicted its four answer steps. Before editing, the author confirmed that
line was present. The correction must return all four answers and the rewrite,
preserve the user's choices, and leave the migration guide unwritten. Compare
the skill with upstream to confirm every existing byte remains unchanged.
Remove only the blank line before the formal-routing bullet, preserve the
blank line before "Only when named", and rerun both checkers and script tests.

The corrected skill adds only "Return the four answers and the rewritten
prompt. Do not carry out the task." to the upstream text. A byte comparison
passed. The routing edit removes one blank line without changing wording.
The two mistakes require judgment about prompt meaning and list continuity;
this round adds no generalized wording test or new agent rule. The coordinator
owns the independent review, shared changelog and integration steps.

## What each skill does

| Skill | Output and boundary |
| --- | --- |
| `sharpen` | Rewrites a deeper prompt using four questions about professional practice, raw material, methods and an outside check. Returns the four answers and the rewrite, preserves the user's choices, and does not carry out the task. |
| `in-your-own-words` | Restates goals and the underlying problem. Does not provide a playbook or change code. |
| `create-formal-verification-skill` | Selects a high-harm property tests rarely reach, verifies within explicit scope, and generates a rerunnable project-local skill with coverage and a sync commit. |
| `maintain-formal-verification-skill` | Reconciles formal checks with covered-code changes, separates drift from product bugs, and rechecks mutation sensitivity before advancing sync records. |

## How they are linked

ROUTING.md lists the two prompt helpers only under “Only when named.” A new
situation-first line beside the existing behaviour-verification pair routes
races, invariants and cases tests rarely reach to the formal generator, and
covered-code changes since the recorded sync commit to formal maintenance.
The two generators link to each other in one sentence each: a behaviour
journey through the app versus a property within stated assumptions. Formal
creation also links to formal maintenance; maintenance links back to creation.
The on-demand maintenance report is linked from its entrypoint.

Upstream evidence: `poteto-help/SKILL.md` state guidance and skill table,
`setup-pstack/SKILL.md` section 8, and `docs/guide/06-verify-and-ship.md` section
“Prove a property with a formal verification skill.” The setup offer is not
ported as an always-on prompt: endstack's index is the equivalent entrypoint.
All four remain hidden from implicit catalog invocation in both adapters.

## Dry-run method

Headless Claude Sonnet 5.5, medium effort, one sample per arm, run on 2026-10-21
from a `mktemp -d` directory outside the repository, with no tools or persistent
session. Exact invocation shape:

```sh
claude -p "<prompt>" --model claude-sonnet-5-5 --effort medium --tools '' --no-session-persistence < /dev/null
```

At most two processes ran concurrently. Nine runs exited 0; the sharpen baseline timed out after 240 seconds and its process was terminated. No completed baseline response was retained, so that comparison is incomplete. The routing prompt asked, “Using only
this index, say which skills you would open for each numbered prompt and
briefly why. Respect explicit-only helpers.” It supplied either ROUTING.md
from the starting revision or the new text, followed by the six prompts below.
No skill bodies were supplied for routing. The skill arms supplied the new
entrypoint (and the linked maintenance report); baseline arms supplied only
the same user request. These are response dry runs, not code execution or
independent review. Text that looks like a tool call is not an executed tool.

### Round-2 sharpen rerun

Only sharpen was rerun, with the same migration-guide request above and the
same command shape, model, effort, no tools, and no persistent session. Both
arms ran from one new temporary directory outside the repository, with a
600-second subprocess limit. The without-skill prompt was exactly the user
request. The with-skill prompt was `Follow this skill:` plus a newline, the
complete corrected entrypoint, then `User request:` on a new line and that
same request. A first with-skill CLI launch began directly with the entrypoint's
YAML delimiter and exited 1 with `error: unknown option '---`. It produced no
model response. The introductory line fixed argument parsing; the corrected
launch is the response reported below. The without-skill arm was launched only
once in this round. It timed out at 600.0 seconds with zero response bytes, so
there is no reply to assess for task execution. No other scenarios were rerun.
Both processes have ended. The temporary directory was removed after these
deciding lines were recorded.

### Routing results

| Prompt | Old index: deciding line | New index: deciding line | Assessment |
| --- | --- | --- | --- |
| Prove our job lease never lets two workers run the same job. | “no narrower playbook covers proving an invariant” (`figure-it-out`) | “Open `create-formal-verification-skill`.” | New formal route selected. |
| The retry module that our model checker covers was refactored last week after its recorded in-sync commit; check the formal verification still matches. | “no skill is specific to spec drift” | “Open `maintain-formal-verification-skill`.” | New maintenance route selected. |
| /sharpen write a migration guide | “`/sharpen` isn't in this index” | “Open `sharpen`.” | Explicit command discoverable; old arm would still try a catalog lookup. |
| /in-your-own-words I need customers to export invoices without waiting on support. | “`build`: this is a change request.” | “I would not open `build` yet” | Named restatement boundary improved in this sample. |
| Fix the off-by-one in a date formatter with a cheap regression test. | “`tdd`: a bug fix with a cheap local test” | “Open `tdd`” | Both select build/test/verify, neither selects formal verification. No uplift. |
| What time zone is Los Angeles in? | “No skill: this is a one-fact lookup.” | “No skill.” | Correct skip in both arms. No uplift. |

### Skill scenarios

The exact user requests were:

- **sharpen:** “Write a migration guide from our legacy billing API to the new
  API. We have old and new endpoint specs and anonymized failure logs. Pricing
  and rollout dates are my choices.”
- **in-your-own-words:** “I need customers to export invoices without waiting
  on support. Finance keeps requesting CSV exports, and support currently runs
  SQL for each request. We have not chosen CSV versus XLSX yet.”
- **create-formal-verification-skill:** “Create a project-local verification
  skill for this scenario. Given only this scenario, describe what you can
  establish and what execution remains. A job lease implementation in
  lease.src has acquire(job,worker,now): read expiry; if expired then write
  owner and expiry in separate database operations; run(job,worker): perform
  external payment. renew(job,worker) extends expiry. Harm is duplicate
  payments when workers overlap; normal tests cover a single worker. Runtime
  and verifier availability are unknown. A sibling slug formatter has a
  trivial length invariant. Choose the target and outline the deliverable,
  evidence and fallback if no verifier supports this language.”
- **maintain-formal-verification-skill:** “Maintain the formal verification for
  this scenario. Given only this scenario, describe what you can establish and
  what execution remains. The lease check records lease.src acquire and renew
  at sync commit a111. Current commit b222 splits acquire's formerly atomic
  owner-and-expiry update into two separately committed operations; no
  documented promise change. The old two-worker model treats that update as
  atomic and passes. The property is no overlapping payment workers for one
  job. A verifier rerun and real code are unavailable here. Explain what to
  update, how to judge results and what evidence and sync record to leave.
  If only generated-input tests are possible, explain the claim.”

### Skill results

| Skill | Without: quoted deciding lines | With: quoted deciding lines | Assessment |
| --- | --- | --- | --- |
| `sharpen`, initial round | “timed out after 240 seconds” (process timeout; no completed response retained). | “Treat these as the primary sources.” / “Pricing, rollout dates, deprecation and sunset timelines, and any commitments about support windows are my decisions.” | Skill arm returns a rewrite with raw sources, methods and outside checks. Baseline comparison is incomplete; no uplift claimed. It adds many deliverables, so this sample does not establish the “not bigger” constraint. |
| `sharpen`, round 2 | `{"arm": "without", "timeout": 600, "seconds": 600.0}` (process result; zero response bytes). No reply to quote; whether it carried out the task is unknown. | “Build the guide from a field-level diff.” / “The two endpoint specs themselves” / “`oasdiff` or `openapi-diff` for OpenAPI specs” / “every example request and response in the guide passes schema validation” / “## Rewritten prompt” / “Leave pricing and rollout dates as clearly marked placeholders for me to fill in.” | Skill arm exited 0 in 16.4 seconds. It returns all four answers and a rewrite, leaves pricing and dates open, and does not write the migration guide. It still expands deliverables, so deeper rather than bigger is not established. Baseline timed out; the comparison remains incomplete and no uplift is claimed. |
| `in-your-own-words` | “I'll start by looking at what's in the working directory.” followed by unexecuted tool-call text. | “Customers should be able to get their invoice data out of the product themselves” / “Open: whether to offer CSV, XLSX, or both.” | Restates the goal, problem and open choice without code or an implementation plan. Adds “Gaps I'd want to close before building,” so the restatement-only boundary is imperfect. |
| `create-formal-verification-skill` | “I'd skip the slug formatter.” / “A mutation check: reintroduce the split write and confirm the harness fails.” | “A broken lease charges someone twice” / “each model action lists the `lease.src` function and line it represents.” / “Broken variants must fail.” / “I'd label this property-based testing, not proof.” | Both choose the harmful race and request a mutation check: no uplift on those criteria. The skill arm adds explicit action correspondence, bounds and a clearer testing label. Neither executes a broken variant. |
| `maintain-formal-verification-skill` | “The a111 pass is stale for b222.” / “It is not a proof” | “Outcome for the lease check: blocked.” / “Write the update from the code before rerunning.” / “The sync commit **stays at a111**.” | Both identify stale atomicity, preserve sync and distinguish testing from proof: no uplift on those criteria. The skill arm adds a mutation check and explicit blocked outcome. |

The formal-creation skill arm also said “TLA+/TLC is the default if Java is
available,” although the port removes that default. It suggested a file hash
until a repository exists rather than the required sync commit. Those are
response limitations, not requirements added to the port. The baseline drew
inferences from the scratch working directory despite having no tools; those
are not observed filesystem facts. Both arms disclosed no verification had
run. The baseline proposed applying a product fix; the skill arm said “I
wouldn't change product code unless asked.” This is one prompted sample, not a
measured reliability rate.

The formal-maintenance arm proposed breaking the new **model**, while the
skill requires a break in the new **code**. Thus it stated a mutation check but
did not fully preserve the real-code sensitivity requirement. Neither arm
executed a mutation, replayed a counterexample or confirmed a product bug.
The skill arm preserves the property and requires code-first updates; its
blocked outcome is appropriate for the unavailable code and verifier.

## Author checks

- `python3 scripts/check-skills.py`: `0 problem(s)`.
- `python3 scripts/check-routing.py`: `0 problem(s)`.
- `python3 -m unittest discover -s scripts`: `Ran 16 tests`, `OK`.
  The initial round emitted existing unclosed-file ResourceWarnings; its final
  run suppressed only that warning category. The round-2 rerun also passed all
  16 tests and emitted those ResourceWarnings without suppression.
- `git diff --check`: no whitespace errors.
- Checked all new frontmatter and policy files against the existing shape.
  Descriptions are below 200 characters; the two formal descriptions were
  shortened from upstream. All four are explicit-invocation only.
- Read the ports against upstream for retained questions, workflow phases,
  code correspondence, mutation requirements, bounds, findings and sync rules.

| File | Bytes |
| --- | ---: |
| `skills/sharpen/SKILL.md` | 739 |
| `skills/in-your-own-words/SKILL.md` | 391 |
| `skills/create-formal-verification-skill/SKILL.md` | 5266 |
| `skills/maintain-formal-verification-skill/SKILL.md` | 5999 |
| `ROUTING.md` | 2221 |

## Not checked and coordinator handoff

No real project verifier was generated or executed, no proof was run, and no
real-code mutation was demonstrated. The formal dry runs are proposed steps
from small scenarios, not proof evidence. No live adapter discovery or actual
hidden-skill loading was tested. The model already had ambient machine rules
in its headless session; these are not clean-room measurements. There is one
sample per arm in the initial round, plus the disclosed sharpen rerun, with no
statistical claim. No provider-independent verdict on
this revision is supplied by this implementation worker; the coordinator owns
that gate before delivery.

The coordinator must reconcile shared README and catalog counts, CHANGELOG.md,
DISTILL.md, and the homelab routing copy under their rules. This worker did not
edit those files, candidates, upstream, or another checkout. No push, pull
request, merge, installation or remote publication was performed. Local commits
are the implementation handoff only. No project-specific worktree release step
was found in AGENTS.md or README.md.

## Final progress

- Implementation and port notes committed as `2e599d2e7581b9fa3154e79be54be9037299662d`.
- Nine no-tool dry runs returned; the remaining sharpen baseline reached the
  240-second process limit. Recorded the incomplete comparison without claiming
  improvement. No retries or successful samples were substituted for it in the initial round.
  Round 2 retried only sharpen as recorded above; the baseline timed out again
  at 600 seconds, and the corrected with-skill response retained four answers.
- Final checkers each printed `0 problem(s)`; all 16 script tests passed.
  The temporary dry-run directory is removed after its deciding lines and
  scenarios are recorded here. No servers or databases were started.
- Proposed CHANGELOG entry for integration: Added four explicitly invoked
  pstack roles: sharpen, in-your-own-words, create-formal-verification-skill,
  and maintain-formal-verification-skill; linked formal creation and upkeep
  from the routing index and recorded scope and dry-run limits.
- Proposed DISTILL paragraph: On 2026-10-21 Daniel requested four additional
  roles from cursor/plugins at 190d287. W6 preserves prompt-only sharpening,
  goals-only restatement, code-grounded formal property selection and formal
  check upkeep. The formal pair retains broken-variant checks, bounds,
  coverage and sync commits; generated-input fallback is testing, not proof.
  See docs/import-notes/W6.md and this evidence document for author checks,
  paired dry runs and limits. Independent verification remains an integration
  gate, not a result of these response dry runs.

## Round-2 local handoff

- Branch: `t3/add-formal-verification-skills-r2`, based on the two earlier local
  commits `2e599d2` and `c39b109`. Only the sharpen boundary, W6 notes, this
  evidence document and one routing blank line changed.
- Both checkers report `0 problem(s)`; the script suite reports `Ran 16 tests`
  and `OK`. `git diff --check` reports no whitespace errors.
- Against main, routing adds the formal pair directly under the existing
  verification pair and adds sharpen and in-your-own-words under "Only when
  named". The index is 2,221 bytes, below 2,600.
- Independent verification, shared changelog and distribution updates remain
  with the coordinator. This is a local implementation handoff, unverified
  independently. No push, pull request or merge was performed.
