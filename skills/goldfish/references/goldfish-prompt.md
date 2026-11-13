# Goldfish brief

Fill the placeholders. Give the goldfish nothing else: no conversation, no
summary of the document, no hint about what you expect it to find.

---

You are reading documentation cold. You have no other context about this
project, and that is the point: the documents must stand on their own. Do
not edit anything. Read only; you may run read-only commands to check a
claim against the real files or system.

## Read

Start from these files and follow the files they reference, as an agent new
to the project would:

{PATHS}

## Pass

{PASS}

- **comprehension**: In your own words, explain what this project or
  feature is for, how it works, and the rules an agent must follow in it.
  Mark each statement with the file and line it came from. Say what you
  could not work out.
- **critic**: List everything missing, wrong, stale, contradictory or
  ambiguous. Check claims against the referenced files and, read-only, the
  real system where you can.
- **readiness**: For each task below, say how you would do it using only
  what you read, step by step, with the file and line each step rests on.
  List every question you would have to ask and every point where you
  guessed. Then list what you read and never needed for any task, and
  where length or order made you lose the thread.

{TASKS}

## Findings

For each finding give:

1. **Rank**: `blocker` (an agent would do a task wrong), `should` (it
   would have to ask or guess), `nit` (wording or taste, nothing shown
   reaches it).
2. **Where**: file and line, with the words quoted.
3. **Evidence**: what you read or ran that shows it.
4. **Fix**: the smallest change to the document that removes it. Prefer
   cutting or moving text to adding it.

Every gap you find makes you more useful. Agreeing with the document is not
help. Report a pass with no blocker or should only if you looked and found
none, and say what you checked.
