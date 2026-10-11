# Decision-run protocol

Date: 2026-10-10. Four separate T3 child tasks used the same
[`delivery-fixtures.json`](../delivery-fixtures.json), without expected answers.
Codex used GPT 6.1 Sol, medium reasoning; Claude used Opus 5.5, high effort.
Each child owned only its corresponding result Markdown file. They did not
execute any scenario operation, mutate a remote, commit or delegate work.

## Shared brief

Run a bounded read-only decision simulation, not actual implementation or
delivery. Evaluate each case independently under its common project policy.
Do not read README, DISTILL, other results, cookbook or delivery-checks.
For each A–P, record selection, proposed next actions, prohibited actions and
stopping point/reason. Include deciding wording, not just “pass”. Keep the result
under 1100 words; record uncertainty and that no actual case operation happened.
Inherited project/global policy may influence behavior; this is bounded routing
evidence, not live command/discovery proof.

**Baseline arm:** no catalog supplied; do not read `skills/`. Name the natural
workflow rather than selecting a catalog skill.

**Catalog arm:** first read only frontmatter names/descriptions from build,
babysit, ship, autopilot-stack, autopilot-full and verify. Select entries for
each case from those descriptions, then read selected bodies. Record the cues
that selected each entry. All six were selected across the cases.

## Outputs and task correlation

| Provider | Arm | Result | Task client request ID |
| --- | --- | --- | --- |
| Codex | baseline | [decisions](codex-baseline.md) | `endstack-split-codex-baseline-20261010-r1` |
| Codex | catalog | [decisions](codex-catalog.md) | `endstack-split-codex-catalog-20261010-r1` |
| Claude | baseline | [decisions](claudeAgent-baseline.md) | `endstack-split-claudeAgent-baseline-20261010-r1` |
| Claude | catalog | [decisions](claudeAgent-catalog.md) | `endstack-split-claudeAgent-catalog-20261010-r1` |

Keep these returned decisions intact, including inconvenient baseline results
and stated uncertainty. The parent grades them in
[delivery-checks.md](../delivery-checks.md). Separate sessions are not clean-room
contexts: inherited instructions, directory names and recent history can prime
the answers. Claude explicitly disclosed that priming. These are simulations,
not an enforcement or installed-discovery test.
