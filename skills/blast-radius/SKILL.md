---
name: blast-radius
description: "Find what a change could break beyond its diff, whether it is a one-way door, and how much rigor that earns; prove the one fact it's safe because of by running real code."
disable-model-invocation: true
---

# Blast radius

Find what a change breaks somewhere else before it ships, and whether it can be taken back. Use for "blast radius of X", "what could this break", "is this a one-way door", or a small diff you don't trust yet.

Companion to `how` and `why`. `how` tells you what the code does. `why` tells you why it's shaped that way. Blast radius tells you what it breaks somewhere else, and whether a revert undoes it.

Listing the callers is not the job. The agent can search for those in a second. The job is the breakage a search won't show you.

## Don't trust your own writeup

A blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it's true. So don't hand back the writeup. Find the one or two facts the whole thing depends on and prove them by running code.

### How sure are you

For each fact the change's safety depends on, get it as far down this list as is cheap, and say where it stopped.

1. You said so. Worthless on its own.
2. You pointed at the line. A real `file:line`, or the library's own source.
3. You showed the bad case can't happen. You walked the failure step by step and it doesn't reach.
4. You ran it. A script or test that calls the real code and fails loud if you're wrong.
5. You reproduced it in the running app.

Step 4 is usually one small script that imports the same library the app ships and calls the exact function you're worried about.

## One-way or two-way door

Radius says how far it reaches. The door says whether you can take it back. Ask: if this is reverted tomorrow, what stays changed? Whatever stays is the one-way part.

- **Two-way.** A revert and redeploy leaves nothing behind: code paths, internal refactors, flags off by default, anything nothing else has read or stored yet.
- **One-way.** Something outlives the revert: data written, rewritten or deleted (a migration, a lossy transform, a dropped column); a contract others start relying on (a public API, a wire or file format, an event schema, a config key, a published package); something sent (mail, payments, notifications, calls with side effects); access, credentials or history changed.

Most changes are two-way with a small one-way core. Name the core and say how to make it two-way: expand then contract, write both shapes, back up first, put it behind a flag, dry run, roll out in stages. A door made two-way is cheaper than any review of it.

## Steps

1. Read the change. The diff, the symbols it adds, changes, and deletes, and what it now does differently, including the part the diff doesn't spell out. Use `why` to pull the pull request and commits.
2. Find the one fact it's safe because of. Most changes that look risky are safe because of a single fact, like "this call only drops already-dead cache entries and does nothing else". Find that fact. If it holds, most risky cases are cleared at once. Spend your time here, not on a long list of maybes.
3. Look where search stops. Read the source of the library you call, and check its pinned version and any local patch. Work out when things run: microtasks, unmount and teardown, the framework's render and effect order. Follow what a symbol search misses: the JSON an API returns, a DB column, a wire format, another language reading the same bytes, a feature flag, an installed or vendored copy, code three hops downstream.
4. Call the door. Name what outlives a revert, or say nothing does and why.
5. Be honest about each risk. Give it a real chance of happening and a real cost if it does. Keep the risks you confirmed. List the ones you checked and cleared separately. Same rules as `why`. Cite a real `file:line`, a search that finds nothing is still an answer, and never make up a caller or an API.
6. Prove the one fact. Write a script or test that runs the real code, run it, and paste what happened. Behind a one-way door, step 4 of the list above is the floor, not a goal.
7. For a big or wide change, run it as an [arena](../arena/SKILL.md). Ask more than one model the same question and merge the answers. Different models catch different real bugs.

## Rigor

Radius and door together set how much checking the change earns. Spend it where it pays:

- **Two-way, radius inside the diff.** The change's own checks are enough; most of review's value here is already in them.
- **Two-way, radius past the diff.** Prove the one fact and add a check at the far end: the consumer, the stored data, the other reader.
- **One-way, any radius.** Shrink the one-way part first. Prove the fact at step 4 or 5 before the door opens, get independent review aimed at what outlives the revert, and open the door only with the authority it needs.

## What to hand back

- **What it does.** What changed, including the part that isn't obvious.
- **The one fact it's safe because of.** State it, say which step you got it to, and show the proof. If you couldn't prove it, write unproven.
- **Door.** One-way or two-way, what outlives a revert, and how to make it two-way.
- **Risks.** Each names how it breaks, the `file:line`, how likely and how bad, and how to check. Paste the proof for the ones that matter.
- **Cleared.** What you checked and why it's fine.
- **Rigor.** Which row above, and the checks and review it calls for.
- **Before you merge.** The cheapest test or repro that catches the real bug, including the script you wrote.

Write it through `unslop`, cite real code, and strip anything private before it goes anywhere public.

**Reply:** the writeup above, with the one safety fact either proven or marked unproven and the door called.
