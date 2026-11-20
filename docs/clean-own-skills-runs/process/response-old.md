(a) **First message.** Before the first unit, I send the user one message with every question I can anticipate, each with a stated default. The questions: endpoint order and which endpoints get stacked together, based on shared middleware (default: I group them by middleware). Whether the old router is removed in its own final PR (default: yes, after all 14 land). Any compatibility or API-shape decisions. Any holds or areas I shouldn't touch. I also say that deployment and destructive operations are outside my authority, and that I proceed on the defaults if they don't answer. I don't ask whether to merge or whether to keep going.

(b) **First three actions.**
1. Create the durable notes file in the repo or tracker. It holds the goals, the per-endpoint checks, the stack dependencies, standing orders, ownership, and slots for briefs, PR links, verdicts and blockers. I start the decision trail with show-me-your-work.
2. Send the early-questions message above.
3. Launch a pilot for one endpoint through the harness's delegation. Its owner gets a self-contained kickoff: goal, allowed and forbidden paths, exclusive branch ownership, forbidden actions, the evidence that proves completion, and landing authority. A fresh read-only verifier who isn't the author follows. I only fan out to the remaining endpoints, about ten in flight, after the pilot has merged.

(c) **Endpoint 3 typo.** I don't fix it, because I never edit code. I log it in the notes and put it in endpoint 3 owner's kickoff. If it blocks the program, it's fixed in that PR. Otherwise it's parked as a follow-up.

(d) **Merges.** Each PR's owner lands it through ship's gates. That needs a passing independent verdict on the current head, required checks green and holds honoured. No one waits for the user's approval. The pilot merges first. Stacked PRs land in dependency order, and owners handle the rebases. The old-router removal lands last. I never merge.
