# Does loading unslop change the text?

Daniel's question (2026-10-14): keep `unslop` if it changes what agents write,
not if loading it does nothing.

## Experiment

Ten writing tasks with the facts given (a final reply, a pull request
description, a commit message, a README section, an explanation, a status
update, a changelog entry, a decision, an incident note, an answer). Each ran
without the skill and with the skill's text before the task, on GPT 6.1 Sol
(medium) and Claude Opus 5.5, twice: 80 runs, tools blocked, none read a skill
file. A deterministic counter scored the patterns the skill names that can be
counted (dashes used as punctuation, curly quotes, bold inline headers, its
word lists, chatbot and filler phrases, title-case headings).

| Provider | Without | With |
| --- | --- | --- |
| Codex | 40 hits in 20 outputs (32 curly quotes, 8 em dashes); 6 of 20 clean | 0 hits; 20 of 20 clean |
| Claude | 10 hits (bold inline headers); 14 of 20 clean | 0 hits; 20 of 20 clean |

Applied while writing, the skill removes every counted pattern on both models.

## Real threads (since the routing table)

Final reply of each turn, threads that loaded `unslop` against threads that
never did:

| Machine, provider | Loaded | Never loaded |
| --- | --- | --- |
| omarchy, Claude | 77% clean, 4.5 hits per 1,000 words (123 replies) | 55% clean, 8.5 (163) |
| Mac, Claude | 52% clean, 7.6 (38) | 59% clean, 6.8 (82) |
| Codex, both | 22-50% clean, 13-16 per 1,000 words, mostly curly quotes | too few to compare (6 replies) |

In practice the effect is smaller than in the experiment: an agent loads the
skill at the start of a task and writes its final reply many steps later, and
Codex replies still carry curly quotes after loading it. The counter does not
judge the skill's other rules (plain words, sentence length, active voice).

## Decision

The skill changes text, so it stays in the routing table. The gap between the
experiment and real replies points at timing: the skill works when its rules
are in view as the text is written.
