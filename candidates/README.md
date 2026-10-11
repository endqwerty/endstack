# Candidates: pstack material not imported

Reference copies of Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack)
(`cursor/plugins@978ca6e`, full history at the git tag `pstack-snapshot`). Upstream
is no longer tracked here; read it by hand and import only what is valuable.

Most pstack skills have been imported into `skills/` (see
[DISTILL.md](../DISTILL.md) and `docs/import-notes/`). What remains here is
either already covered by a `skills/` entry or not wanted. Nothing here is
installed: `npx skills add` and `homelab sync` read `skills/` only (`npx skills add
--full-depth` also scans `candidates/`, so do not pass it).

To import something: `git mv candidates/<name> skills/<name>`, port it to the
rules in [AGENTS.md](../AGENTS.md), run `python3 scripts/check-skills.py`, and
record it in DISTILL.md, CHANGELOG.md and `docs/import-notes/`.

| Skill | Upstream description | Status |
| --- | --- | --- |
| [blast-radius](blast-radius/SKILL.md) | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of... | folded into `verify` |
| [poteto-help](poteto-help/SKILL.md) | Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task. Type /poteto-help with a question. | help text for poteto-mode; not needed |
| [poteto-mode](poteto-mode/SKILL.md) | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work in this style. | the always-on router and 23 playbooks; its babysit, shipping, opening-a-pr, feature, bug-fix and autopilot playbooks became build, babysit, ship, autopilot-stack, autopilot-full. Other playbooks are not imported |
| [principle-prove-it-works](principle-prove-it-works/SKILL.md) | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles. | covered by `verify` |
| [setup-pstack](setup-pstack/SKILL.md) | Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack,... | Cursor model setup; not applicable |

poteto-mode's `playbooks/` (23), `references/` and `scripts/` (upstream's
polling machinery) are the reference for the autopilot and delivery skills.
Links from these files into the deleted pstack guide and agent definitions are
dead on purpose.
