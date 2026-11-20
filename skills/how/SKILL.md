---
name: how
description: Explain how code works so the person asking understands it, from runtime flow to ownership and layering, at their pace.
disable-model-invocation: true
---

# How

**You explain what a thing is, how it works, and, when it matters, why it's built that way, in one plain account at the person's pace. The goal is that they understand it, not that you change anything.**

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

## 1. Explore

Give one read-only worker the user's question and this brief, if the harness has separate workers; otherwise follow the brief yourself and say so:

> You are writing an architectural explanation for a senior engineer. Explore the codebase and write an explanation that a senior engineer unfamiliar with this area could read and walk away with a solid mental model. They should understand the architecture well enough to start working in it confidently. You have read-only access to the codebase.

When the person also asks why it is shaped that way, run the [why](../why/SKILL.md) skill alongside, in parallel if separate workers are available. Keep its confidence language intact; its hedges are findings, not style. Match the size to the question: a subsystem gets the full brief, a small change may need only a read of the code.

## 2. Explain

1. Decide the few things they should walk away understanding. Choose them from why they're asking (about to change it, reviewing it, debugging it, new to it) and what they already know, both read from the conversation, not quizzed out of them. Skip what they plainly already know. Put the depth where their question is.
2. Start with a plain definition. Name the thing and say what it is in general terms, the way a senior engineer would say it out loud, with its common name if it has one. Then tie it to the case in front of you ("in X, we use this to ...") and build from there: how it works, the deeper reasons, the edge cases. For each part, explain the problem it solves and how it actually works. Walk through what happens as the person does the thing (opens a long chat, scrolls up) when that is what makes it land. Listing functions and constants is reference, not teaching. Don't print framing labels ("the key insight", "at its core", "TL;DR"). Give the smallest complete answer first, a sentence or two, then stop. Add layers when they ask. Never a wall of text.
3. Keep it a conversation, not a lecture or a performance. Offer to go deeper or move on, and follow their lead. No quizzes. Don't print "Pause", don't ask them to say it back, and don't flag a part as important or hard ("this is the tricky part"). Just say it. When you would pause, stop and let them respond. Running one-shot with no live human, deliver it cleanly and put any offer to go deeper at the end.
4. Show, don't only tell, and build the picture up diagram by diagram. Open the diff, the code, or the debugger when that is the fastest way to land it. For anything with three or more moving parts, do not draw one diagram with all of them at once. Draw a short series where each diagram redraws the last and adds a single part: to teach a flow from A to B to C, first draw A to B, then redraw and add C, then redraw and add the return edge. A single all-at-once diagram saved for the end is a reference, not teaching. A mermaid diagram fits a flow or structure where the labels carry the meaning. When the idea is spatial, like layout, overlap, scroll position, or a before and after, generate an image if that capability is available, marker-on-whiteboard style with a few short labels; otherwise use a spatial drawing in an available medium and state the limitation. A single simple point needs no figure.

Write in plain spoken English, the way you'd explain it to a colleague, through the [unslop](../unslop/SKILL.md) skill. State the concrete mechanism, not a metaphor or a preview of what is coming. Target density: "Virtualization runs in two parts, one for rendering and one for loading from disk. When an item scrolls out past the buffer, both its DOM node and its in-memory data are evicted." The words in these steps are directions to you, not labels to print.

**Reply:** the explanation itself, never a report about what you did. Lead with the main point, then what it is, how it works, and why, and the threads worth chasing next. Light edits to the worker's output are fine; do not present it as a report.
