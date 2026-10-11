---
name: automate-me
description: "Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via skill authoring and plain-prose editing, optionally pulling fresh evidence from recent transcripts."
disable-model-invocation: true
---

# Automate me

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

This skill orchestrates three others: an inline mining pass (see step 1), an available skill-authoring workflow, and the **unslop** skill (prose discipline). It sequences them. It doesn't replace them.

## Flow

### 0. Check for an existing skill

Look recursively in the project's and user's skill locations for a `-mode` skill matching the user's handle, including personal category directories. If one exists, confirm intent unless they already asked to update it:

- Update the existing skill (default for repeat runs)
- Start fresh (rare, ask why before doing it)

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited (use its recorded revision history).
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Locate transcripts using only the active workspace-scoped location supplied by the harness. Never search unrelated workspaces or private chats.

Survey recent conversations for recurring patterns. Give slices of history (for example, the last 2–4 weeks split into three slices) to separate workers in parallel, if available; otherwise mine the slices yourself in sequence and say so. Each slice miner reads transcripts from the workspace-scoped path the parent provides, looks for the signals below, and returns a short structured list of patterns it saw with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Use structured multiple-choice questions if supported; otherwise present the same concise choices in text.

Shape: one or two questions with 4-6 options each, allow multiple selections for category questions. Start broad ("Which areas matter most?"), then follow up on selected areas with specific options. After the structured rounds, one free-form chat question catches anything the options missed.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, connected-source use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: separate checkouts, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

Use an existing personal mode skill, if available, as a granularity reference. Do not copy its content; the user's rules are their own.

### 4. Draft the skill

Use an available skill-authoring workflow to author the skill. Placement:

- Path: preserve an existing mode skill's category. For a new mode, follow an established personal category in the project's skill location; otherwise use its normal skill location, or the user's personal skill location if preferred.
- Handle: the user's first name or chosen identifier.
- Frontmatter `description`: trigger on their name + the mode skill name + "work in their style", not on generic keywords like "write code" or "review PR".
- Frontmatter formatting: follow the authoring workflow’s YAML rules. Keep `description` as one YAML scalar. Quote it or use `description: >-` with indented continuation lines when punctuation or wrapping requires it.
- Frontmatter `disable-model-invocation: true` by default. Opt out only if the user explicitly wants their mode to apply on every turn.

### 5. Iterate on prose

Apply the **unslop** skill and the authoring workflow’s writing guidelines to every line.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

Work in an isolated branch checkout. Commit and open a pull request for review; do not publish directly to the default branch.

## Guardrails and evaluation

Read [guardrails and evaluation](references/guardrails-and-evaluation.md) before drafting and reviewing the mode skill.
