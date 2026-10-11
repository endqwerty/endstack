---
name: verify
description: Get an independent check before a change is merged or called done. Use for a feature, bug fix, or anything touching auth, data, money, credentials or deployment, and when asked to verify, double-check, sign off on or break someone else's change. Not for docs, comments or mechanical edits.
---

# Verify

A change is not done because its author says so. Someone who did not write it
runs it, tries to break it, and answers on the evidence.

## Author

1. Before changing anything, write the checks that would prove the task done.
   Each runs on the real surface: the command, the page, the API call, the
   stored value. A bug gets a check that fails first.
2. Run them on the real artifact and keep the lines that decide each one.
   "It compiles" and "the tests pass" are not proof of behaviour.
3. Ask for a verifier that is independent of you: a different model lineage
   if the project can provide one, never your own earlier session. It is
   read-only.
4. Give it the task, your checks, and the exact revision range. Not your
   conclusions, not your explanation of why it works.
5. Fix real findings. Answer the rest with a concrete reason. After material
   fixes, check again once, then deliver and say what is still open.

## Verifier

- Run every check yourself. Do not accept the author's output.
- Then try to break it: other inputs, failure paths, what else uses the
  changed code, what the diff does not show.
- Suspect your method before the system when a check fails. Reproduce it.
- Answer each check: **pass**, **issues**, or **not checked**, with what you
  ran and the deciding lines. A check you could not run is never a pass.
- Name the revision you judged. A verdict on an older revision is stale.
- Change nothing.

## Never

- Verify your own work and call it independent.
- Pass on a summary. Read the diff yourself, a subagent's included.
