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

Protocol deviations: Claude's baseline has 1129 whitespace-delimited words
(table pipes included), above the requested 1100-word limit; retained verbatim
rather than trimming evidence. Both Claude children reported using their
available file-write tool because apply_patch was absent. Reasoning settings
above are the requested settings, not an independently observed runtime value.

## Focused follow-up

Two GPT 6.1 Sol tasks (requested medium reasoning, priority service tier)
evaluated [Q–S](../delivery-follow-up-fixtures.json) before/after review fixes.
The first loaded only skill blobs from `8a6fee3`; the second loaded revised
working-tree files and recorded their hashes. T was added after the first run
and appears only in the second. The briefs asked for proposed next actions,
readiness, stopping points and deciding words without self-grading or assuming
a failure was expected; neither ran scenario operations.

- [Before](codex-followup-before.md): `endstack-split-followup-before-20261010-r1`.
- [After](codex-followup-after.md): `endstack-split-followup-after-20261010-r1`.

Both disclosed required project-doc reads exposing historical summaries despite
the requested isolation. Retain that limitation rather than claiming blindness.
