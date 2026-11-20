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
homelab skill-eval --agents claude --runs 1 main HEAD
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
- `trace`: the run's event stream as JSON lines. A skill read shows up as
  `"file_path":".../skills/<skill>/SKILL.md"` on Claude and as a `cat` or
  `sed` command on Codex; patterns here match both. A directory listing does
  not count as a read.
- `{source: file, path: <relative path>}`: one file's content at the end of
  the run. Use it to check what an edit kept or removed.
- `files`: the list of files the run created, by path. It holds no content
  and does not list edited files.

To check order in the trace, such as a test written before the fix, use
`^(?:(?!SECOND)[\s\S])*FIRST`: it matches when FIRST occurs before any SECOND.

### Limits of the Claude arm

Claude runs inside the eval sandbox. Its shell can read and run programs but
cannot write files, reach the network or run `git`; edits go through the edit
tools, and `npm test` fails, so prompts name `node --test`. A case therefore cannot grade commits on Claude. Grade the
order of edits and test runs in the trace instead.

## Cases

| Case | Skills | Checks |
| --- | --- | --- |
| ship-explains | ship | "How would you ship PR #12?" runs no merge command and the reply explains the gates |
| build-design | build, principles, architect | archive tasks: design doc before production code, both list consumers changed, tests added, no merge or push |
| review-routing | verify | a pre-merge review reads verify, not how, why or swarm, and finds the extra retry attempt |
| bugfix-shared-fault | test-design | refunded lines: shared total, invoice and receipt fixed, failing test before the fix, redundant cap removed |
| interrogate-pager | interrogate | three planted pager bugs, each with a command; no source edited |
| no-comments-nine | no-comments | nine comments: licence, API doc, platform note, issue link and formatter ignore kept; narration and "do not remove" gone |
| unslop-prose | unslop | three pieces of prose without dashes, curly quotes, bold-label colons, rule 7's words or chatbot phrases |
| principles-review | principles | guard hiding the bug, swallowed catch, cast on disk data |
| why-retry | why | cites PR #812, marks inference, says the record does not show the rotation, advises keeping 7 |
| architect-ratelimit | architect | two shapes compared, router middleware with a shared counter, jobs exempt by construction |
