# Skill evals

Standing cases that score endstack's skills on Claude Code and Codex. Each case
replaces a hand-run dry run under `docs/`: the same scenario, run by a fresh
agent that sees only the revision's `ROUTING.md` and `skills/`, graded by
checks a machine can decide.

## Run

From an endstack checkout:

```sh
homelab skill-eval main HEAD                  # every case, both agents, base and head
homelab skill-eval --case why-retry HEAD      # one case at one revision
homelab skill-eval --case 'bugfix-*' HEAD     # cases whose folder names match a glob
homelab skill-eval --runs 1 --jobs 8 --case 'bu*' main HEAD   # the usual PR check: tagged cases, once, in parallel
homelab skill-eval --agents claude --runs 1 main HEAD
homelab skill-eval --agents claude,codex,antigravity --runs 1 --case why-retry main HEAD   # Gemini through agy too
```

`--case` takes case folder names under `evals/` or a glob over them, not skill
names. To run the cases that exercise one skill, find them by their tags:

```sh
grep -l '^- verify$' evals/*/prompt.md       # cases tagged verify
```

The runner archives each revision into a temporary directory, adds the plugin
manifest, prepends "your skills directory is ..." and that revision's
`ROUTING.md` to the system prompt, and runs the cases from HEAD's `evals/` at
both revisions. It prints one row per case with the base, head and delta score
per agent, then totals and cost. Paste the table into the pull request as
evidence for a skill change; it is not a merge gate.

`python3 evals/check-evals.py` checks that every `prompt.md` and grader parses
and uses only known keys, and compiles each pattern in Python and, when `node`
is installed, JavaScript. Run it after editing a case.

## What the score means

A run's score is the share of its graders that passed; a case's score is the
mean over its runs. 1.0 means every check passed in every run. Compare the
base and head columns of the same agent; a delta inside one run's worth of a
grader (1 / graders / runs) is noise. LLM graders are judged by a small model
and are the least stable; read the trace before trusting a delta that rests on
one.

## Cost

A short Claude run (a reply, a few file reads) costs about $0.10. A code
change with tests (`build-design`, `bugfix-shared-fault`) costs about ten
times that, which is why those cases use two runs. The full suite at two
revisions on Claude is roughly 60 runs; pass `--max-cost-usd` to cap it, or
`--case` while iterating. Codex cost is not reported.

## Time

Up to `--jobs` units run at once (default 4). Each Claude case at one revision
is one unit, and each Codex run of a case at one revision is another, so a
check of N cases at two revisions with `--runs 1` on both agents is 4 x N
units. Set `--jobs` to that number and the wall time is about the slowest single
run: a few minutes for a reply case, eight to ten for a code change. One or two
cases take about ten minutes; when there are more units than `--jobs` slots,
the rest wait and run in waves.
Runs inside one Claude case go one after another, so `--runs 3` on a
code-change case takes about three run-times.

`--case` takes one folder name or one glob; repeating the flag keeps only the
last, and a comma-separated list matches nothing. When no single glob selects
exactly the cases you need, run one invocation per case or glob.

## Add a case

1. Pick a scenario that a skill change could break, ideally one already run
   by hand in `docs/`, and name the folder for it: `evals/<case>/`.
2. Write `prompt.md`: frontmatter with `name` (the folder name), `tags`
   (every skill the case exercises), `runs` (3; 2 for code changes),
   `max_turns`, `timeout_seconds` and `allowed_tools`, then the prompt as the
   body. The prompt is self-contained and names no skill, so routing has to
   pick it. A task that changes files ends with "Do not ask questions; finish
   and summarize." Never set `append_system_prompt`, `model` or `plugins`; the
   runner does.
3. Put files the agent works on in `fixture/`. The runner copies them into the
   working directory and commits them once as "fixture".
4. Write one grader per file in `graders/<name>.md`, frontmatter only:
   - `regex`: `pattern`, optional `flags` (`i`, `m`, `s`), `match`
     (`contains`, `not_contains`, `count:N`) and `target`.
   - `file_exists`: `path`, a glob relative to the working directory.
   - `tool_used`: `tool`, optional `input_match`, `min`, `max` (Claude only).
   - `llm`: `criteria`, one yes-or-no question a judge can answer from the
     final reply.
   Prefer `regex` and `file_exists`; use `llm` only for what a pattern cannot
   decide.
5. Run `python3 evals/check-evals.py`, then the case once on each agent, and
   read the traces of any grader that fails before trusting it.

### Regex targets

- `last_message`: the agent's final reply.
- `trace`: the run's event stream as JSON lines: Claude's stream-json events,
  or Codex's `item.completed` events (`command_execution` with `command` and
  `aggregated_output`, `file_change` with `changes[].path`, `agent_message`).
  Antigravity (`--agents antigravity`) runs are rewritten into these shapes: a
  file read as a Read call with `file_path`, a shell command as
  `command_execution`, an edit as `file_change`; its raw stream-json is kept
  beside it. A skill read is a Read call whose `file_path` ends in
  `skills/<skill>/SKILL.md`, or a `command` in which a reading command (`cat`,
  `sed`, `head`, `tail`, `nl`, `less`, `more`, `awk`, `bat`) stands at a
  command-word position and names that file, directly, in a brace list, through
  a `for` loop variable or after a `cd` into `skills/`. A listing (`ls`, `rg
  --files`), a path in command output, and the word `head` inside a directory
  name do not count.
- `{source: file, path: <relative path>}`: one file's content at the end of
  the run. Use it to check what an edit kept or removed.
- `files`: the list of files the run created, by path. It holds no content
  and does not list edited files.

To check order in the trace, such as a test written before the fix, use
`^(?:(?!SECOND)[\s\S])*(?:FIRST)`: it matches when FIRST occurs before any
SECOND. Tie each event to its kind: a file write is a Write or Edit call's
`file_path` or a Codex `file_change` path, never a bare path; a test result is
the output of that test command (the Claude tool_result with the same
`tool_use_id`, or the same Codex item's `aggregated_output`), never failure
text elsewhere. A test run is a test command (`node --test`, `npm test`, a
test runner through `npx`) at the start of the command, after an optional
shell `-c` wrapper, `cd` or `set` statements (ended by `&&`, `;` or a newline;
a trailing `#` comment only before a newline) and variable assignments; one
inside `echo`, `printf`, a comment or a heredoc is not. Known limits: any `#`
on the test command's line ends it, so `node --require=./a#b.cjs --test` is
not seen; blank lines between a prefix and the test, and quoted spaces in a
variable assignment, are not followed either.
Give every changed trace or file grader a negative control (the
unchanged fixture or a wrong trace fails) and a positive control (a correct
outcome passes) before relying on it.

### Limits of the Claude arm

Claude runs inside the eval sandbox. Its shell can read and run programs but
cannot write files, reach the network or run `git`; edits go through the edit
tools, and `npm test` fails, so prompts name `node --test`. A case therefore
cannot grade commits on Claude. Grade the order of edits and test runs in the
trace instead.

## Cases

| Case | Skills | Checks |
| --- | --- | --- |
| ship-explains | ship | "How would you ship PR #12?" runs no merge command and the reply explains the gates |
| build-design | build, principles, architect | archive tasks: design doc before production code, both list consumers changed, tests added, no merge or push |
| review-routing | verify | a pre-merge review reads verify, not how, why or swarm, and finds the extra retry attempt |
| bugfix-shared-fault | test-design | refunded lines: shared total and invoice fixed (receipt and mail share the total), test written and seen failing before the fix, green after the last edit, redundant cap removed |
| interrogate-pager | interrogate | three planted pager bugs, each with a command; no source edited |
| no-comments-nine | no-comments | nine comments: licence, API doc, platform note, issue link (ids come from a vendored API client) and formatter ignore kept; narration and "do not remove" gone |
| unslop-prose | unslop | three pieces of prose without dashes, curly quotes, bold-label colons, rule 7's words or chatbot phrases |
| principles-review | principles | guard hiding the bug, swallowed catch, cast on disk data |
| why-retry | why | cites PR #812, marks inference, says the record does not show the rotation, advises keeping 7 |
| pr-watch-wait | pr-watch | waiting for an upstream PR to merge runs the bundled watcher with `--until merged` and no `--timeout` or a whole number of hours or of minutes of at least 60, no sleep loop, no write to the PR (including `gh api` with fields or a non-GET method); the reply ties the next step to the merge. The PR is already merged, so the command line, not the exit, shows a sustained wait |
| architect-ratelimit | architect | two shapes compared, router middleware with a shared counter, jobs exempt by construction |
| orchestrate-medium | orchestrate, build | a one-PR multi-currency change in five parts reads orchestrate, writes the CSV export, and the reply reports units built by separate workers and makes no landing claim (judged from the reply: trace patterns for delegation and pushes kept failing review); bugfix-shared-fault checks a small fix does not read it |
| test-design-properties | test-design | three billing modules: reads test-design and its property reference, picks stateless property-based tests for the cent allocator, stateful model-based tests with a reference model for the TTL cache, example tests for HTTP route wiring, uses an independent oracle, pins shrunk regressions or checks broken variants, and pins seed and run bounds for the every-change suite |
| formal-verification-boundary | formal-verification, test-design | single-process LRU cache vs distributed lease claim: reads formal-verification, routes the single-process cache to stateful model-based or property-based testing on the real code, and keeps the concurrent lease protocol in formal verification |
| blast-radius-door | blast-radius | an applied camelCase rename and column drop: reads blast-radius, finds the Python nightly report still reading `total_cents` outside the diff, finds pre-2024 orders never backfilled, calls the drop a one-way door and proposes making it reversible; no file edited |
| loop-judge-flaky | loop-judge | a flaky TTL test after four timeout bumps: reads loop-judge, does not raise the timeout again, fixes the expiry boundary (an entry still returned at exactly the ttl) or the real-timer dependence, and logs a pivot in `attempts.md` |
| test-design-guard | test-design | two admin routes shipped without a permission: reads test-design, fixes both, and guards every admin route through one mechanism that covers routes added later instead of a test per route |
| verify-test-bloat | verify, test-design | a slug function with eight tests: reads verify, asks to drop the near-duplicate, source-reading and type-only tests before merging, keeps the accent and punctuation tests |
