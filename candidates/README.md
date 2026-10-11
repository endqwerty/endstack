# Candidates: pstack skills not yet imported

Reference copies of Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack)
skills (`cursor/plugins@978ca6e`, full history at the git tag `pstack-snapshot`),
kept so a skill worth importing is one step away. They are **not installed** and
not maintained here; upstream is no longer tracked. Look at upstream by hand when
you want something new and import only what is valuable.

They sit outside `skills/` on purpose: `npx skills add` and `homelab sync` read
`skills/` only, so these are never installed by accident.

## Importing one

1. Copy `candidates/<name>/` to `skills/<name>/` (`git mv`).
2. Distill it to the rules in [AGENTS.md](../AGENTS.md): outcome and roles,
   no tool, command, model, provider or harness names; about 2 KB; one job.
   Links to sibling candidates must be rewritten or dropped.
3. Add a dry run (what the agent did with and without it), then record it in
   [DISTILL.md](../DISTILL.md) and [CHANGELOG.md](../CHANGELOG.md).

## Index

| Skill | What it does (upstream description) | Status | Bytes |
| --- | --- | --- | --- |
| [architect](architect/SKILL.md) | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the... | not imported | 5469 |
| [arena](arena/SKILL.md) | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the... | not imported | 4279 |
| [automate-me](automate-me/SKILL.md) | Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via... | not imported | 7164 |
| [benchmark-checklist](benchmark-checklist/SKILL.md) | Vet a perf measurement (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark or report a speedup or regression you measured. | not imported | 5002 |
| [blast-radius](blast-radius/SKILL.md) | Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it's safe because of by running real code instead of writing it up. Use for 'blast radius of X', 'what could this break',... | folded into `verify` ("what else uses the changed code") | 3856 |
| [bro](bro/SKILL.md) | Restate the last message in plain human language, with no jargon. | not imported | 267 |
| [correct](correct/SKILL.md) | Find the mistakes agents keep repeating in this repo and make each one impossible. Try architecture first, then types, then a lint whose error names the fix, then a test, and write docs last. Prove each check fails on a real... | not imported | 2445 |
| [create-verification-skill](create-verification-skill/SKILL.md) | Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for /create-verification-skill, \"make a control skill for this repo\", or when a project has no... | not imported | 5879 |
| [figure-it-out](figure-it-out/SKILL.md) | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions. Use... | not imported | 3978 |
| [how](how/SKILL.md) | Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains... | not imported | 2518 |
| [interrogate](interrogate/SKILL.md) | Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple LLM reviewers challenge changes from independent... | single-reviewer part distilled into `verify` | 4317 |
| [ketchup](ketchup/SKILL.md) | Catch the user up on everything in this chat since their last message, in plain words. Give each action item an executive summary with enough context to make the call. Use for /ketchup. | not imported | 1976 |
| [maintain-verification-skill](maintain-verification-skill/SKILL.md) | Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. Use for... | not imported | 4922 |
| [make-bot-ui](make-bot-ui/SKILL.md) | Use when building a custom UI (page, dashboard, buttons) that should wake a Grok Bot over a webhook, when the user must provide a webhook sender key, or when exposing that UI on Tailscale. | not imported | 4649 |
| [no-comments](no-comments/SKILL.md) | Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints. | not imported | 2560 |
| [poteto-help](poteto-help/SKILL.md) | Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task. Type /poteto-help with a question. | not imported | 13646 |
| [poteto-mode](poteto-mode/SKILL.md) | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work in this style. | its babysit, shipping, opening-a-pr, feature, bug-fix and autopilot playbooks became build, babysit, ship, autopilot-stack, autopilot-full; the other playbooks are not imported | 19341 |
| [principle-attack-the-premise](principle-attack-the-premise/SKILL.md) | Apply when two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it. | not imported | 1941 |
| [principle-boundary-discipline](principle-boundary-discipline/SKILL.md) | Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions. | not imported | 1883 |
| [principle-build-the-lever](principle-build-the-lever/SKILL.md) | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your subagents follow) instead of working by hand. The... | not imported | 2386 |
| [principle-encode-lessons-in-structure](principle-encode-lessons-in-structure/SKILL.md) | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text. | not imported | 2001 |
| [principle-exhaust-the-design-space](principle-exhaust-the-design-space/SKILL.md) | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing. | not imported | 1152 |
| [principle-experience-first](principle-experience-first/SKILL.md) | Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones. | not imported | 1184 |
| [principle-explain-the-number](principle-explain-the-number/SKILL.md) | Apply before you trust, report, or act on a number you measured: a speedup, a regression, a throughput, a latency, or an eval result. Find what limits it, and rule out that it measured something other than the work you think. | not imported | 1663 |
| [principle-fix-root-causes](principle-fix-root-causes/SKILL.md) | Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes. | not imported | 1246 |
| [principle-foundational-thinking](principle-foundational-thinking/SKILL.md) | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious. | not imported | 1530 |
| [principle-guard-the-context-window](principle-guard-the-context-window/SKILL.md) | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads. | not imported | 939 |
| [principle-laziness-protocol](principle-laziness-protocol/SKILL.md) | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem. | not imported | 1371 |
| [principle-make-operations-idempotent](principle-make-operations-idempotent/SKILL.md) | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs. | not imported | 1390 |
| [principle-migrate-callers-then-delete-legacy-apis](principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers. | not imported | 1146 |
| [principle-minimize-reader-load](principle-minimize-reader-load/SKILL.md) | Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope. | not imported | 1996 |
| [principle-model-the-domain](principle-model-the-domain/SKILL.md) | Apply when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. | not imported | 1858 |
| [principle-never-block-on-the-human](principle-never-block-on-the-human/SKILL.md) | Apply when tempted to ask 'should I do X?' on reversible work. | not imported | 910 |
| [principle-outcome-oriented-execution](principle-outcome-oriented-execution/SKILL.md) | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code. | not imported | 1078 |
| [principle-prove-it-works](principle-prove-it-works/SKILL.md) | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles. | distilled into `verify` | 1371 |
| [principle-redesign-from-first-principles](principle-redesign-from-first-principles/SKILL.md) | Apply when integrating a new requirement into an existing design. | not imported | 758 |
| [principle-separate-before-serializing-shared-state](principle-separate-before-serializing-shared-state/SKILL.md) | Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant. | not imported | 1565 |
| [principle-sequence-verifiable-units](principle-sequence-verifiable-units/SKILL.md) | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the... | not imported | 1705 |
| [principle-subtract-before-you-add](principle-subtract-before-you-add/SKILL.md) | Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base. | not imported | 909 |
| [principle-test-behavior-not-implementation](principle-test-behavior-not-implementation/SKILL.md) | Apply when you write, change, or keep a test. Call the code as its users do and assert the exact result they see. Rewrite or delete a test that would pass if every imported function returned undefined. | not imported | 1386 |
| [principle-type-system-discipline](principle-type-system-discipline/SKILL.md) | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, refuse to lie to... | not imported | 3661 |
| [recall](recall/SKILL.md) | Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. Use for 'recall my work on X', 'catch me... | not imported | 5212 |
| [reflect](reflect/SKILL.md) | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect. | not imported | 4633 |
| [setup-pstack](setup-pstack/SKILL.md) | Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, "configure pstack models",... | not imported | 5716 |
| [show-me-your-work](show-me-your-work/SKILL.md) | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for... | not imported | 6418 |
| [swarm](swarm/SKILL.md) | Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration. | not imported | 2949 |
| [tdd](tdd/SKILL.md) | Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is unclear, expensive, integration-heavy, or not requested. | not imported | 3143 |
| [teach](teach/SKILL.md) | Explain a body of work plainly so a person actually understands it. Runs the `how` and `why` skills and weaves what they find into one clear explanation. Use for 'teach me this', 'help me really understand X', 'explain this... | not imported | 5623 |
| [technical-writing](technical-writing/SKILL.md) | Layered technical-writing standard: Diátaxis structure, Google developer style sentences, STE instruction rules, Global English syntax. Use for /technical-writing or when writing or reviewing docs, RFCs, readmes, PR... | not imported | 9093 |
| [typescript-best-practices](typescript-best-practices/SKILL.md) | TypeScript best practices. Use when reading or editing any .ts or .tsx file. | not imported | 2684 |
| [unslop](unslop/SKILL.md) | Cut AI tells from any writing. Must always apply. | not imported | 5846 |
| [why](why/SKILL.md) | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence category (source control, issue tracker,... | not imported | 8770 |

`poteto-mode` also carries the 23 playbooks (`playbooks/`), `references/` and
helper scripts (`scripts/`) that the skills above reference; the scripts are
upstream's polling machinery and are not wanted as they are.
