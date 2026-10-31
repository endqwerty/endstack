Nothing was run and the working directory is empty, so the repo-specific names below (`jobqueue/…`, `claim`, `reap`, the Lua script) are my assumptions, not read from your code. The Status section says so, and the next agent must confirm them before trusting the skill.

```markdown
---
name: verify-single-runner
description: Use when a change touches how jobs are claimed, leased, heartbeated, reaped, requeued or acked in the Redis job queue (jobqueue/worker.py, jobqueue/reaper.py, jobqueue/scripts/*.lua). Runs a TLA+ model that checks a job is never run by two workers at once.
---

# Verify: a job never runs on two workers at once

## Property and harm

- Property: at no point do two workers both hold the right to run the same job.
- Harm: a job with side effects (payment, email, write) runs twice.

## Status (read first)

- Not yet run. The model, the TLC command and the broken-variant check below are written but unexecuted.
- File, function and script names under "Coverage" were assumed, not read from the repo. Open each one and correct this file before relying on it.
- Sync commit: UNSET. Set it after the first successful run (see "Keeping this in step").

## Is your change covered?

Run the check if the diff touches any of these:

| Model action | Code (confirm) |
| --- | --- |
| `Enqueue(j)` | `jobqueue/client.py: enqueue` |
| `Claim(w, j)`: atomic move from pending to running plus lease set | `jobqueue/scripts/claim.lua`, `worker.py: claim` |
| `Heartbeat(w, j)`: lease extended only if `w` still owns it | `jobqueue/scripts/heartbeat.lua`, `worker.py: heartbeat_loop` |
| `LeaseExpire(j)`: Redis TTL passes | Redis expiry on the lease key (environment step, not code) |
| `Reap(j)`: expired running job returns to pending | `jobqueue/reaper.py: reap` |
| `StartRun(w, j)`: worker begins executing the handler | `worker.py: run_job` |
| `Ack(w, j)`: worker finishes, job removed if `w` still owns it | `jobqueue/scripts/ack.lua`, `worker.py: ack` |

Each Lua script is one indivisible step in the model, because Redis runs a script atomically. Two separate Redis commands from Python are two steps. If your change splits or merges such steps, the model must change too.

## Run

    scripts/verify-single-runner.sh

The script runs `java -cp tools/tla2tools.jar tlc2.TLC -workers auto -config specs/SingleRunner.cfg specs/SingleRunner.tla`. The jar is pinned in `tools/README.md` with its version and checksum. Run time should be under a minute at the bounds below.

## What is checked

- Invariant `AtMostOneRunner`: for every job, the set of workers in the running phase has at most one member.
- Bounds in `SingleRunner.cfg`: 2 workers, 2 jobs, lease time 3 ticks, at most 2 reaps per job.
- Assumptions: Redis is a single node that does not lose data; Lua scripts are atomic; a worker can pause for any number of ticks between any two of its steps (a GC pause or a slow handler); clocks are one shared tick counter.
- Not covered: Redis failover or replication, clock skew, handler code, more than 2 workers or jobs, liveness (that jobs eventually finish).

A pass means no bad order exists within these bounds. It does not mean the whole system is safe.

## Reading a result

- Pass: TLC prints `No error has occurred`.
- Fail: TLC prints a trace. Rewrite it as steps in code terms, for example "worker A claims job 7; A's heartbeat stalls; the lease expires; the reaper requeues job 7; worker B claims it; A resumes and runs it while B runs it".
- Decide whether the trace is real:
  1. Walk each step against the code in the Coverage table. If every step can happen, it is a bug in the code. Report it with the trace. Do not weaken the invariant or the model to make it pass.
  2. If a step cannot happen in the code, the model is wrong (for example an atomicity it does not have, or one it has and the model lacks). Fix the model, then rerun the broken-variant check.

## Broken-variant check (proves the check can fail)

`specs/variants/` holds one-line mutations, each of which must make TLC fail:

- `no_owner_check_on_ack`: `Ack` drops the owner test.
- `reap_ignores_expiry`: `Reap` requeues a job whose lease has not expired.
- `claim_non_atomic`: `Claim` split into "check pending" and "set lease" as two steps.

Run `scripts/verify-single-runner.sh --variants`. Every variant must report a violation. If one passes, the model has stopped guarding that code: fix the model before trusting any pass.

## Changing the code on purpose

1. Update the model action in `specs/SingleRunner.tla` to match the new code.
2. Update the Coverage table.
3. Run the check and the variants.
4. Say in your summary what changed in the model and why.

## Keeping this in step

- Last confirmed against commit: `UNSET`.
- Check for drift: `git diff <sync-commit> -- jobqueue/worker.py jobqueue/reaper.py jobqueue/scripts/ jobqueue/client.py`. Any output means the model needs another look.
- Move the sync commit forward only after you have read that diff against the Coverage table and confirmed the model still describes the code. Passing TLC alone is not enough, since the model can pass while describing old code.
```

Before the user relies on it, the next agent still has to:
- Read the real code and fix the names, scripts and atomicity claims.
- Write and run the TLA+ spec and variants.
- Do the scratch-change catch from the skill.
- Set the sync commit.

Also expect a likely finding: lease-based queues usually allow a paused worker to keep running after its lease is reaped, so `AtMostOneRunner` may fail unless the code fences with a token. That is a guess, not a result.
