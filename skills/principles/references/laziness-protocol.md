# Laziness Protocol

Aim for the most result with the least code.

- **Prefer deletion.** Look for removals before additions.
- **Consolidate decisions.** Do not repeat the same choice in several places. Put it behind one source of truth and pass the result as a simple flag.
- **Minimize the diff.** Make the smallest change that solves the problem. Fewer lines beat "elegant" boilerplate.
- **Question the threading.** Before passing a new signal through types, schemas, or pipelines, look for a more direct path.
