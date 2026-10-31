I haven't read the repo (the working directory is empty and not a git repo) and ran nothing. The file and function names below (`jobqueue/worker.py`, `claim`, `reap_expired`, and so on) are my assumptions about a typical Redis queue. Check each one against the code before you rely on this. The sync commit is also unset, because I have no commit to record. By the skill's own rule, this is a draft until it has been run against a scratch break.

````markdown
---
name: verify-single-runner
description: Use when a change touches job claiming, leases, heartbeats, requeueing, acking or retry in the Redis job queue. Checks with a TLA+ model that no job is ever run by two workers at once.
---

# Verify: a job is never run by two workers at once

## The property

**Property:** at no point do two workers both believe they are running the same job.

**Harm if broken:** the job's side effects happen twice (double charge, duplicate email, double write).

The model is in `verification/single_runner/`. It is a small model of the claim, lease, reap and ack steps, not of the whole queue. A pass covers the model within its bounds. It does not cover the Python code line by line.

## When this applies

Open the coverage table below. If your change touches any listed function, run the check. If you add a new step that moves a job between Redis keys, or changes who may run it, the model needs a new action: update it before you rely on a pass.

## Run it

```
verification/single_runner/run.sh
```

The script runs TLC from `verification/tools/tla2tools.jar` (TLA+ tools 1.8.0, checked in by sha256 in `verification/tools/SHA256SUMS`). It needs Java 17 or later. It takes about a minute with the default bounds in `SingleRunner.cfg`: 3 workers, 2 jobs, lease clock 0..4, up to 2 retries.

Exit 0 means no invariant violation within those bounds. Exit 1 means TLC found a counterexample.

Read every result with the `statechart` skill. It shows a violation as its shortest path in plain words and, on a pass, draws how the system moves between states. Do not copy its commands into this file.

## What the model contains, and where the code is

Each model action is one indivisible step. It matches one Redis call or one Lua script, because those are atomic. Anything the code does in two separate Redis calls is two actions.

| Model action | Code | Atomic because |
| --- | --- | --- |
| `Claim(w, j)` | `claim` in `jobqueue/worker.py`, Lua script `jobqueue/lua/claim.lua` | one Lua script |
| `Heartbeat(w, j)` | `extend_lease` in `jobqueue/worker.py` | one Redis call |
| `Run(w, j)` / `Finish(w, j)` | `run_job` in `jobqueue/worker.py`, worker side only | local to the worker |
| `Ack(w, j)` | `ack` in `jobqueue/worker.py`, Lua script `jobqueue/lua/ack.lua` | one Lua script |
| `Tick` | lease expiry by Redis TTL | the clock |
| `Reap(j)` | `reap_expired` in `jobqueue/reaper.py` | one Lua script |

Invariants checked: `SingleRunner` (no job has two workers in the `running` state) and `LeaseMatchesRunner` (the lease owner of a running job is the worker running it).

Left out: Redis failover and replication, network partitions, clock skew between hosts, worker crashes after `Finish` but before `Ack` beyond the single crash action, priorities, and scheduled jobs.

## Reading a failure

1. Take the counterexample from `statechart`. Write it as steps in code terms (for example "worker A claims job 1, its lease expires, `reap_expired` requeues it, worker B claims it, A is still in `run_job`").
2. Open the code for each step and check that it can happen. If a step cannot happen in the real code, the model is wrong: fix the model and say what you changed. If every step can happen, it is a real bug. Report it with the steps. Do not weaken an invariant, widen the model's atomic steps, or remove an action to make the check pass.
3. Do not change product code unless the user asked.

## Known finding

A job whose `run_job` outlasts its lease can be reaped and claimed by a second worker while the first is still running. The invariant `SingleRunner` fails on this unless the worker stops work when `extend_lease` fails. The model has the switch `WorkerStopsOnLostLease` in `SingleRunner.cfg`. Keep it set to match the code. If the code does not stop the worker, the check fails, and that failure is the finding to report.

## Proof that the check can fail

`verification/single_runner/mutants/` holds three broken copies of the model, each matching a break in the code:

- `no_lease_check.tla`: `Ack` no longer checks the lease owner.
- `reap_before_expiry.tla`: `Reap` ignores the lease clock.
- `claim_non_atomic.tla`: `Claim` split into read and write.

`run.sh --mutants` must report a violation for every one. If one passes, the model has lost its power: fix that before trusting any pass.

## When your change is intended

1. Change the code.
2. Change the model action and the table above to match.
3. Run the check and `run.sh --mutants`.
4. Only then move the sync commit below to the commit where you confirmed that the model describes the code.

## Sync record

- Covered files: `jobqueue/worker.py`, `jobqueue/reaper.py`, `jobqueue/lua/claim.lua`, `jobqueue/lua/ack.lua`.
- Sync commit: unset until the first confirmed run. Record the full hash here.
- To see whether the covered code changed since the sync commit: `git diff <sync commit> HEAD -- jobqueue/worker.py jobqueue/reaper.py jobqueue/lua/`. A non-empty diff means the model needs another look.
````
