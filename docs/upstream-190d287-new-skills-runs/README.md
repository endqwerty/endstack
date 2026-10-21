# Round-3 routing run records

See [the requests, method and deciding quotes](../upstream-190d287-new-skills.md#round-3-concurrency-routing-rerun).

Each `r3-<request>-<old|new>.prompt.txt` contains the full CLI prompt, including
the index. Matching `.response.txt`, `.stderr.txt` and `.exit.txt` files retain
stdout, stderr and exit status. Request names are `cache`, `workers`, `proof`,
`drift` and `queue`. Old is ROUTING.md at `5bab0ed`; new is the final index in this
commit. All ten scratch samples exited 0, with one sample per request/arm. The
`workers` request uses the short wording in the follow-up; `queue` uses the
verifier's full recorded wording. The extra pair addresses ambiguity in the
short request; no response was discarded.

`pilot-repo-cwd/` retains an earlier eight-response pilot excluded from the
comparison because the CLI inherited the repository working directory. Its
cache/new launch first returned a server error and no model answer. The
`r3-cache-new-attempt1.*` records retain that error; the pilot's successful
retry used the identical `r3-cache-new.prompt.txt`. No completed response
was replaced within either run set.

The invocation for each saved prompt was:

```sh
claude -p "<prompt>" --model claude-sonnet-5-5 --effort medium --tools '' --no-session-persistence < /dev/null
```

The reported comparison ran in a new `mktemp -d` directory, with at most two
active calls and a 600-second subprocess limit. The runner explicitly set
`cwd=Path(__file__).parent` for each CLI subprocess and lived in scratch.
That directory was deleted after recording the results. The files here are
the retained artifacts. No product code ran. No skill bodies were supplied.
These are author dry runs, not an independent verification verdict.

[r3-checks.txt](r3-checks.txt) retains checker and unit-test deciding lines.
