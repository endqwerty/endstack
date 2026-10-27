Paper exercise: decide, do not execute. Nothing here is real; run no commands except reading files.

You are the author of pull request #530, which adds a cache in front of a slow pricing lookup (a behaviour change).
The user asked you to build it and left. An independent verifier from another provider has reviewed it twice:

- Round 1 on head A: should S1: a price change is served stale for up to an hour, because nothing evicts the entry
  when an admin edits a price. You added eviction on the admin edit path (head B), with a test.
- Round 2 on head B: should S2: prices imported by the nightly batch job bypass the admin edit path, so they are
  still served stale. Should S3: a race between eviction and a concurrent read can re-insert the old price.

Using only the skills in SKILLDIR (read SKILLDIR/ROUTING.md first, then the skill files it leads you to in that
directory), say exactly what you do next and why, through to where you stop. Quote the rule that decides each step.
Under 20 lines. Write the answer to OUTFILE and make that path your final message.
