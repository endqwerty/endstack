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

## Baseline at `2508bde` plus grader fixes (one run per case)

| case | Claude | Codex |
| --- | --- | --- |
| architect-ratelimit | 1.00 | 1.00 |
| bugfix-shared-fault | 1.00 | 0.89 |
| build-design | 1.00 | 0.86 |
| interrogate-pager | 0.86 | 0.57 |
| no-comments-nine | 0.90 | 0.80 |
| principles-review | 1.00 | 1.00 |
| review-routing | 1.00 | 1.00 |
| ship-explains | 1.00 | 0.57 |
| unslop-prose | 0.88 | 1.00 |
| why-retry | 1.00 | 1.00 |
| **total** | **0.96** | **0.87** |

Claude $3.81 (the full run plus a `review-routing` rerun after the grader
fixes); Codex judge $0.39 for the Codex column. One run per case is a snapshot: Codex's
`ship-explains` scored 0.86 in an earlier run and 0.57 here on a reasonable
reply that did not name review findings or mergeability. Compare base and head
with the default three runs.

What the baseline found:

- **Grader misfires, fixed:** skill reads done in a shell loop or a `{a,b}`
  path were not counted; the extra-retry judge question demanded the `>=` to
  `>` detail; the Codex judge, one strict vote, passed a correct reply 1 time
  in 6 while its reason said the criterion was met (now 5 of 5, and 0 of 3 on
  a reply that misses the point).
- **Open questions, not yet skill gaps:** both agents deleted the issue-link
  comment, but the fixture never showed the external constraint it cites, so
  deletion was defensible; the fixture now establishes it. On
  `interrogate-pager`, Codex's reply named all three bugs and included the
  command it ran (`reply-shows-commands` passed), yet the three judge questions
  that combine each bug with its evidence failed; read the judges' reasons on
  the next run before calling this a skill gap.
- **Graders that credited the unchanged fixture, fixed after review:** three
  `bugfix-shared-fault` outcome graders matched text already in the fixture,
  its order graders accepted unrelated events, a directory listing counted as a
  read, and `build-design`'s consumer graders passed a whitespace-only edit. The
  baseline above predates these fixes, so its `bugfix-shared-fault` and
  `build-design` scores are upper bounds.
