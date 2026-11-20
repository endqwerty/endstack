---
name: how
description: Explain how code works and where a change belongs, from runtime flow to ownership and layering.
disable-model-invocation: true
---

# How

Explore the codebase to answer "how does X work?" questions.

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

## 1. Explain

Give one read-only worker the user's question and this brief, if the harness has separate workers; otherwise follow the brief yourself and say so:

> You are writing an architectural explanation for a senior engineer. Explore the codebase and write an explanation that a senior engineer unfamiliar with this area could read and walk away with a solid mental model. They should understand the architecture well enough to start working in it confidently. You have read-only access to the codebase.

## 2. Present

Present the worker's output. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.
