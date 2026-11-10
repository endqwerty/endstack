# Upstream de8ee15 paired runs

Run on 2026-11-10 with Codex CLI, `gpt-6.1-sol`, low reasoning, one sample per
arm. These are hypothetical response exercises, not independent reviewers or
implementation workers. They run in a fresh scratch directory, outside the
repository, read-only, and explicitly forbid tools, file reads, edits and
agents. All eight exits were 0 and JSONL records contain no tool calls.

Both arms get the same scenario and neutral exercise instruction. The
`without` arm gets "Use your normal engineering judgment." The `with` arm
gets complete changed skill text, or, for number, the principle reference
and benchmark checklist together. Links are explicitly unavailable.
This tests decisions with supplied text, not discovery or reference loading.
Default user configuration and rule discovery are disabled; project document
bytes are set to zero. Both arms still share the CLI's built-in instructions.
No installed skill cache, repository fixture, remote PR or real benchmark is
changed.

Each stem has the exact `.prompt.txt`, complete `.response.txt`, raw `.jsonl`
and `.stderr.txt`. The scenario is the text after `SCENARIO` in each prompt.
The empty stderr files are retained to show no diagnostic was omitted.

Replay any saved prompt from a new `mktemp -d` scratch directory, substituting
its literal path for `<scratch>`:

```sh
codex exec --ignore-user-config --ignore-rules --skip-git-repo-check \
  --ephemeral -m gpt-6.1-sol -c 'model_reasoning_effort="low"' \
  -c project_doc_max_bytes=0 -C <scratch> -s read-only --json - \
  < /absolute/path/to/goal-with.prompt.txt
```

| Pair | Without, deciding quote | With, deciding quote | Read |
| --- | --- | --- | --- |
| Goal | "preserve their original text in the CSV export, and check that numeric totals stay unchanged" | "I’ll fix the CSV export so account IDs keep their leading zeros while numeric totals stay unchanged" | Both retain the goal through the requested four artifacts. No measured uplift. With is more directly phrased; that is not proof of better implementation. |
| Cache | "I recommend keeping a corrected local copy outside the plugin cache" and "Nothing will be published" | "copy the whole `reports` folder to `/work/local-skills/reports/`" after "explicit approval" | Both avoid cache writes and publication and show the destination before approval. No measured uplift; with makes whole-folder copying explicit. |
| Seats | "report the arena comparison as blocked or incomplete" | "report the comparison incomplete because only one independent candidate is available" | Both use an authorized same-family independent replacement and disclose the limit; both hold an impossible comparison. No measured uplift. |
| Number | "Run a controlled comparison on representative exports before integrating" | "No minimum worthwhile improvement has been supplied, so leave that threshold unresolved. The noise floor is also unknown and must be measured" | With explicitly records the unknown decision threshold and noise floor before running. Both keep the current serializer on the noisy hypothetical result. Planning specificity improves in this sample; no adoption-outcome uplift. |

No statistical claim follows from one response per arm. The baseline number
response correctly notes that spread alone does not determine statistical
significance; the policy's conservative "no measurable difference" label is a
reporting decision, not a significance test. The real measurement procedure
and integration remain untested. Goal's one-line exception, Reflect's
maintained-source branch and Arena's single-requested-candidate exception are
not separately exercised. No robustness or provider comparison is claimed.
