---
name: why
description: Find why code took its current shape, from history, with cited evidence.
disable-model-invocation: true
---

# Why

Investigate the motivation and intent behind code. The companion `how` skill answers what the code does and how it works. `why` answers what forces led to its shape.

Investigators and the synthesizer are separate roles. Give the work to separate workers, if the harness has them; otherwise do it yourself in sequence and say so. They need read-only access to available local and remote evidence. Do not select a mode that strips the remote access needed for investigation or citation checks. They must not write files or modify external state.

## Operating Posture

Operate as a **careful, cautious, and precise investigator**. Be honest about what you know vs what you're inferring. Read [references/epistemics.md](references/epistemics.md) for the full confidence framework and phrasing guide. The synthesizer must follow it.

## Step 1. Understand the Target and the Question

The **target** is usually a chunk of code, a pattern, a feature, or a named design decision. The **question** is usually a design rationale, a tradeoff, a motivating edge case, an external constraint, dead code, or a broad history sweep.

If the target is vague ("why do we do it this way?" with no clear referent), make your best guess from conversation context (open files, recent edits, active selection, what was just discussed). State your interpretation briefly so the user can redirect if you're off, then proceed.

## Step 2. Establish the Code Anchor

Before assigning investigators, build the seed context inline: file paths and line ranges, key symbols (functions, classes, constants), the last few commits touching the target, PR numbers from merge commits (pattern `(#1234)` in the subject line), and any linked ticket IDs. Trace last-touch history for the relevant lines, full patches through renames, recent commit subjects, and complete commit messages to recover PR numbers. Read the bodies, linked issues, discussion and reviews of every substantive PR. This anchor goes to every investigator and to the synthesizer.

## Step 3. Assign Parallel Investigators

**Default to the full parallel investigation.** The goal is a complete coverage map, not a minimal one. Document the null, don't skip the search.

### Discovery

Before assigning investigators, discover the evidence sources available in this environment through its capability catalog or source descriptions.

Map each available source integration to one evidence category:

1. Source control history
2. Issue / ticket tracker
3. Long-form documents
4. Real-time team chat
5. Infrastructure observability
6. Error / exception tracking
7. Product analytics warehouse

Always investigate source-control history and PR discussion; report an access gap if either is unavailable. For the other six, classify using the source name, access instructions, capabilities, and resource descriptions. If a source integration could fit more than one category, choose the one matching its primary evidence. Record ambiguous cases in the coverage map.

Assign one investigator per available evidence category, concurrently if possible, each owning exactly one source integration. Do not ask one worker to cover multiple integrations.

Each investigator's prompt is [references/investigator-prompt.md](references/investigator-prompt.md) filled in, plus:

- the category playbook `references/sources/<source>.md` for the selected source integration, adapted from the examples in [references/source-playbook.md](references/source-playbook.md)
- [references/sources/incident-postmortem.md](references/sources/incident-postmortem.md) **if the target code looks defensive** (null checks, retry logic, timeout handling, rate limiting, feature flags, egress guards, OOM handlers)
- the code anchor and the user's original question

Read [references/investigator-roster.md](references/investigator-roster.md) when assigning sources. It maps all seven categories to the kind of rationale each can reveal and the gap an empty search leaves.

Read [references/coverage-rules.md](references/coverage-rules.md) before skipping any category or answering inline. Unavailable sources are gaps; irrelevance requires an explicit justification in Sources Consulted.

## Step 4. Synthesize

Assign one synthesizer. It gets:

1. The investigator findings, including any null results and any categories skipped with justification
2. The code anchor
3. The user's original question
4. The epistemics framework from [references/epistemics.md](references/epistemics.md)
5. The synthesizer prompt template from [references/synthesizer-prompt.md](references/synthesizer-prompt.md)

## Step 5. Present

Present the synthesizer's output to the user. You may lightly edit for clarity or add context from the conversation, but **do not rewrite the confidence language**.

## Output Format

The structure is the one in [references/synthesizer-prompt.md](references/synthesizer-prompt.md): The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don't Know, Sources Consulted, Confidence Summary. Adapt as needed, but keep the confidence separation intact, and keep Sources Consulted as one line per investigator, including the ones that returned nothing or were skipped, with the reason.

After Sources Consulted, if the user's `why` question is a precursor to changing this code, convert the lineage findings into a Preserve / Change / Avoid / Risk constraint set for planning the change.

## Common Failure Modes to Avoid

- **Recency bias**. Assuming the most recent commit is authoritative. The current shape is often the accretion of many earlier decisions. Trace back.
