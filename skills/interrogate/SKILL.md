---
name: interrogate
description: Challenge a change or design with independent adversaries; only findings proven by a run survive.
disable-model-invocation: true
---

# Interrogate

Adversaries try to break a change or a design. A finding survives only when a run proves it. Report the findings. Do not apply fixes.

## Frame

The scope is what the user names. Otherwise it is the branch diff from its merge base with the base branch, through the working tree. Restate the intent in your own words, from the user's message, the commits, and the pull request description. Ask the user when the intent is unclear.

## Fan out

Choose at least two adversaries suited to the scope, from different model families if available. Give each its own isolated checkout and copy the scope's uncommitted changes into it. If the harness has separate workers, launch them all in parallel; otherwise play each adversary yourself in sequence and say so, since the findings are then not independent. If an adversary cannot start or returns nothing, continue with the rest and say so. Give each adversary the scope, the intent, and this brief:

> Break this change. Prove each finding with a run against the real code, such as a failing test, a repro script, or command output that shows the wrong behavior. For a design or plan, run a prototype or probe the current tree. Report each finding with a title, the exact command, including any repro script's full text so it runs from the scope's own checkout, the output it printed, and the output the intent requires. Leave out anything you did not run. That covers style, naming, structure, and risks that need a future change to matter. No findings is a valid result.

## Verify

Rerun each finding's command. Keep a finding when the output shows the failure and the failure breaks the intent. Drop the rest. Merge findings that share a root cause.

There is no judge, base or graft: adversaries find different failures, so the verdict keeps every verified finding, not one adversary's list.

## Output

- **Intent**: the restatement.
- **Findings**: for each verified finding, the command, its output, how it breaks the intent, and the adversaries that found it. Say "no verified findings" when none survive.
- **Dropped**: for each adversary, the count of dropped findings and why.
