# EGM plugin trial

Should endstack use Google's Elephant-Goldfish Model plugin
(`google/elephant-goldfish-model` at `8b1553f`, 2026-11-22) instead of its own
port of it (`goldfish`, `interview`, `drift`, ported from `72d06f5` on
2026-11-17, see [egm-port.md](egm-port.md))? The main upstream addition
since the port is `egm-lite`, a loop for small changes: critique, checklist,
fresh spec review, implementation, fresh diff review.

## Arms

- `main` (254bf13): endstack as merged.
- `fe756fb`: EGM's skills, personas, standards and harness docs vendored in;
  `goldfish`, `interview` and `drift` removed; one routing line sends design
  work to EGM and changes through `egm-lite`, telling the agent to give EGM's
  next command itself at each halt. `build`'s design reference runs
  `egm-review` instead of `goldfish`.
- `d9ff197`: as `fe756fb`, plus a bullet in `build` itself to open `egm-lite`.

Cases: `bugfix-shared-fault`, `build-design`, `orchestrate-medium`, with
longer turn and time limits for every arm (EGM runs longer). Run 2026-11-22
with `homelab skill-eval`.

## Results

`main` against `fe756fb`, one run each:

| Case | Codex main | Codex EGM | Claude main | Claude EGM |
|---|---|---|---|---|
| bugfix-shared-fault | 0.94 | 0.81 (0.94 after the grader gap below) | 0.81 | 0.75 |
| build-design | 0.79 | 0.93 | 0.71 | 0.93 |
| orchestrate-medium | 0.50 | 0.75 | 1.00 | 0.75 |

`fe756fb` against `d9ff197`, Claude, two runs each:

| Case | `fe756fb` | `d9ff197` |
|---|---|---|
| bugfix-shared-fault | 0.78 | 0.72 |
| build-design | 0.75 | 0.89 |
| orchestrate-medium | 1.00 | 1.00 |

How often Claude used EGM, from the traces (read `egm-lite` / ran its full
loop with the checklist and both fresh reviews):

| | `fe756fb` | `d9ff197` |
|---|---|---|
| Read `egm-lite` | 4 of 6 | 4 of 6 |
| Full loop | 2 of 6 | 3 of 6 |
| On the small fix | 1 of 2 | 0 of 2 |

## Read of the result

- Codex follows EGM every time and through every halt when told to run it
  unattended; Claude reads it in two runs of three and skips it on small
  fixes, whether the instruction sits in routing or inside `build`.
- Where EGM ran on the designed feature, both providers wrote the design doc
  before code and named the rejected alternative; the case scored higher on
  both. On the small fix it cost score nothing and on Claude cost roughly
  1.5 to 2 times as much per run.
- One or two runs per arm: the direction holds on both providers, the size
  does not.
- The bullet inside `build` did not change how often Claude used EGM.

## Defects found

- The test-order graders in `bugfix-shared-fault` miss `set -o pipefail`
  before `node --test`; Codex's EGM run wrote and ran the failing test first
  and lost both checks.
- `homelab skill-eval` with `--jobs 12` hung after its Codex runs exited, every
  thread waiting on a lock and no child process left; a Codex-only rerun with
  `--jobs 6` finished.
