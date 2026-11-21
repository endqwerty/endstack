# Principles loads (2026-11-20)

## Why

Agents had almost stopped reading the principles index. #43 cut the pointers
to it: `build` lost "read the principles index … report each principle that
changed a choice", the `tdd` merge into `test-design` dropped its
fix-root-causes link and its line asking to name the principles used, and
design.md lets a fix whose shape is settled skip step 1.

## Field reads

Read-only scan of this machine's top-level Claude transcripts and Codex
rollouts outside the endstack and homelab repositories: sessions that read
the installed `build` skill and then edited a file, and how many of them also
read `principles/SKILL.md`. File matching, so about ±10%.

| Window | Codex | Claude |
| --- | --- | --- |
| 26 Oct – 1 Nov | 85 of 99 | 13 of 25 |
| 2 – 8 Nov | 81 of 92 | 27 of 36 |
| 9 – 13 Nov | 28 of 37 | 3 of 3 |
| 14 – 19 Nov | 27 of 41 | 4 of 11 |

The drop starts before #43, with the 16 November install (routing trim: the
standalone "Stateful or branchy logic, or a design call: `principles`" line
became a clause under "Design:"; `test-design` added). 20 November has too few
sessions to count.

## What changed

- `build`: read the principles index before the first production edit, a fix
  included, then design.md; report each principle that changed a choice.
- design.md: a fix whose shape is settled still does step 1.
- `test-design`'s bug fix traces the cause per fix-root-causes.
- `build-design` and `bugfix-shared-fault` grade a read of the index before the
  first source edit (Read tool, a reader command, a loop over skill names, a
  path variable, or `rg -n '^'` inside such a loop; not `ls`, a search or a
  direct `rg -n '^'`) and a principle named in
  the reply.

## Eval

`homelab skill-eval --skill build --skill test-design --runs 2 main HEAD`,
graders as committed here, regraded from the saved traces.

| | Claude main | Claude head | Codex main | Codex head |
| --- | --- | --- | --- | --- |
| index read before first edit | 4 of 4 | 4 of 4 | 4 of 4 | 4 of 4 |
| a principle named in the reply | 1 of 4 | 2 of 4 | 0 of 4 | 0 of 4 |

The eval cannot show the field drop: in its sandbox both revisions read the
index every time, so its read grader guards against a regression rather than
measuring this change. Naming a principle in the reply stays rare on both
revisions, despite the restored line. Not done: putting the index in the
always-loaded global rules (about 950 tokens a request); the field scan after
this installs decides it.
