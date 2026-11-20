# Standing skill evals (2026-11-20)

## Why

Every skill change used to carry a hand-run dry run: one sample per arm, often
tool-free, summarized by the author. Verifiers caught overstated summaries
three times in one day. Daniel asked for a simpler, repeatable way. The cases
in [evals/](../evals/README.md) are those dry runs made permanent, run by
`homelab skill-eval` (homelab's CLI) on Claude (`claude plugin eval`) and
Codex (`codex exec`), and graded by checks a machine decides.

## How it works

- Each revision is archived into a temporary plugin; every case gets that
  revision's `ROUTING.md` and skills path in its system prompt, so hidden
  skills are reached the way the global rules reach them.
- Claude runs one case at a time with only that case's tools. Codex runs with
  a fresh `HOME` and `CODEX_HOME` holding only the login, so installed skills,
  global rules and MCP servers do not leak in.
- Codex runs are graded by the same graders; judge questions go to a small
  model that reasons first and takes the majority of three votes.

## Baseline at `1a256b1` (one run per case, both agents in one run)

| case | Claude | Codex |
| --- | --- | --- |
| architect-ratelimit | 1.00 | 1.00 |
| bugfix-shared-fault | 0.86 | 1.00 |
| build-design | 1.00 | 1.00 |
| interrogate-pager | 1.00 | 0.86 |
| no-comments-nine | 1.00 | 0.80 |
| principles-review | 1.00 | 1.00 |
| review-routing | 0.75 | 1.00 |
| ship-explains | 1.00 | 0.86 |
| unslop-prose | 0.88 | 1.00 |
| why-retry | 0.83 | 1.00 |
| **total** | **0.93** | **0.95** |

Claude $3.33, Codex judge $0.48. One run per case is a snapshot; compare base
and head with the default three runs. Codex's `why-retry` is regraded from its
saved trace: its `for skill in why ...; do cat ...` read missed a grader bug
fixed after the run (0.83 as run). An earlier run, before the grader fixes, is
superseded.

What this run shows:

- **Judge misses on correct replies (Claude arm):** `review-routing`'s reply
  says "`maxAttempts` now allows one extra call", yet plugin eval's own judge
  voted FAIL, PASS, FAIL; `why-retry`'s reply says the record cannot tell
  whether the partner still rotates nightly, yet the judge voted FAIL three
  times on `rotation-unknown`. The Claude arm's judge has the weakness the
  Codex judge had before its fix; follow-up.
- **Not readable back:** plugin eval keeps no trace, so Claude's
  `bugfix-shared-fault` miss on `test-failed-before-fix` cannot be checked;
  its Claude branch is tested only on synthetic traces. One run with
  `--keep-temp` settles it (follow-up).
- **Codex misses to read with the saved judge reasons on the next run:** the judge
  question on one of three pager bugs, though the reply gave a command and
  its output for it (`interrogate-pager`), the issue-link
  and platform-note comments (`no-comments-nine`), and the explicit-request
  wording in `ship-explains`. The Codex judge started saving reasons after this
  run.
- **Grader fixes from review:** graders that credited the unchanged fixture,
  order checks that accepted unrelated events, listings counted as reads,
  "email" and "mail" rejected by turns, a corrupt patch and a fixture that did
  not establish its constraint; each fixed with wrong and right controls.

Known nit: `build-design`'s consumer graders still credit a code line followed
by a block comment that names an archive field (`foo(); /* t.archivedAt */`).
Pattern graders cannot parse comments; this construction is unlikely in a real
run.

Known nit: `bugfix-shared-fault`'s final-run grader checks only what follows
the last green summary in the final test command's result, so a command that
fails, then prints a clean summary and exits 0 (possible only with `;`, not
`&&`) would pass.
