---
name: sharpen
description: "Make a task deeper, not bigger, then rewrite the prompt. Use for /sharpen."
disable-model-invocation: true
---

I want a deeper version of this task, not a bigger one. Deeper changes how my
result is made so it is more likely right: rawer sources, better methods, an
outside check. Bigger adds more things to make.

First say, in a sentence or two, what I am trying to get out of this: the
decision, answer or change the task serves. Judge everything below by one
test: would it change that result, or how far I can trust it? Keep what
passes, most important first, and drop the rest without listing it. An answer
can be "nothing here would change the result".

Then answer four questions under that test:

1. What would a top professional in this field do differently on this task
   that I'm not asking for?
2. What is the rawest material they would start from instead of what has
   already been digested for me?
3. Which methods and tools would they use? Say in plain words what each does
   for this task.
4. What, other than you or me, would show the result is right?

Then rewrite my prompt:

- It asks for my deliverables, made deeper. Something new that passes the
  test (another deliverable, phase or artifact) is a proposal, with what it
  would change. It stays out of the prompt until I take it.
- Keep how firm I was. What I asked for stays required. A "maybe", an aside
  or a half-formed idea stays an option the agent may take or skip, not a
  requirement or a question for me.
- A question or research stays that: the rewrite adds no code, tests, commits
  or audits I did not ask for.
- Decide what evidence and my known preferences can settle, and say what you
  assumed. Ask me only what changes the outcome and only I can answer, with
  your recommendation.
- Have the rewritten prompt ask the agent to prototype any choice an
  experiment can settle and recommend an option from what it observed. Product
  and preference choices that no experiment can settle stay with me.

Return, in this order: the goal; proposals and questions for me, most
important first; the four answers; the rewritten prompt. Do not carry out the
task. Approving the rewrite approves the prompt, not the proposals.
