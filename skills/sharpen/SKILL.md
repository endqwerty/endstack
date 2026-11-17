---
name: sharpen
description: "Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen."
disable-model-invocation: true
---

I want a deeper version of this task, not a bigger one. Deeper changes how my
deliverables get made: rawer sources, better methods, an outside check. Bigger
adds deliverables, phases, frameworks, review rounds or process. Before
rewriting it, do four things, a few lines each:

1. Say what a top professional in this field would do differently on this task
   that I'm not asking for.
2. Name the rawest material they would start from instead of what has already
   been digested for me.
3. Name the specific methods and tools they would use. Name a method only if
   it changes the result, and say in plain words what it does.
4. Say what, other than you or me, would show the result is right.

Then rewrite my prompt to ask for exactly that, inside my scope:

- Keep my deliverables and their size. Every line of the rewrite serves
  something I asked for. A new deliverable, phase, artifact (pull request,
  doc, dashboard), review round or later stage goes in a "Left out" list of at
  most three lines after the prompt, never in it. Answer 4's check belongs in
  the prompt when it judges one of my deliverables and costs little beside it.
- Keep how firm I was. A "maybe", an aside or a half-formed idea stays an
  option the agent may skip, not a requirement or a question for me.
- A question or research stays that. Do not add code, tests, commits or
  audits I did not ask for.
- Fill each input the task needs with a default from the repository, my
  rules and our conversation, marked as a default. Leave open only a choice
  that is mine and changes the outcome, at most three, each with a
  recommendation.
- Plain words. No metaphors, named frameworks or statistics I would need to
  look up.
- Before returning, list my deliverables and the rewrite's. Cut anything in
  the rewrite that does not trace to one of mine.

Return the four answers, the rewritten prompt and the "Left out" list. Do not
carry out the task. Approving the rewrite approves the prompt, not the "Left
out" list.
