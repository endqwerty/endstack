---
name: drift
description: Compare what each design doc says a feature does with what its code and checks actually do, and report only the differences and which side should change.
disable-model-invocation: true
---

# Drift

A design doc is its feature's spec record: its *Behaviour* scenarios say what
should happen and its *Plan* how. Code changes without the doc, and the doc
goes stale with nothing to say so. This skill finds where expected and actual
behaviour differ. It reports; fixes go through [build](../build/SKILL.md).

## When

Periodic passes over a project with design docs (weekly while it is active),
before extending a feature, or when asked whether the docs still hold.

## 1. Scope

The design doc directory the project's rules name, else `docs/design/`, or
the docs named; skip interview briefs (`*.brief.md`). Take one doc at a time,
in order, and read the current files each time, never memory.

## 2. Expected

From the doc, list each behaviour scenario with its named check, and each
claim the *Plan* makes about files, symbols, fields, states, data shapes and
libraries. Open questions and alternatives turned down are not claims.

## 3. Actual

Find the code: follow the doc's links; where there are none, search for the
symbols it names, and note the link the doc should carry so the next pass is
cheaper. Read the code. For each scenario:

- Does the named check exist, and does it assert the scenario rather than
  something weaker that could pass while the scenario is false?
- Run it when it is local, read-only and cheap, by the project's own test
  command, and keep its deciding line. A check you could not run is
  `not run` with the reason, never a pass.
- Does the code do what the scenario says, including its edge and failure
  cases?

## 4. Differences

Report only differences; what matches is not listed.

- **Missing behaviour**: a scenario or plan claim the code does not
  implement.
- **Changed behaviour**: the code does something other than a scenario says.
- **Broken check**: the named check is missing, fails, or could pass while
  its scenario is false.
- **Incomplete shape**: fields, states or types the plan names are missing.
- **Shortcut**: a fixed value where the plan describes logic.
- **Divergent design**: a different pattern, component or library than the
  plan's.
- **Unspecified behaviour**: user-visible behaviour in the feature's code
  that no scenario covers.

A doc with no scenarios (an older one with *Checks*) is reported as not
checkable, not as clean.

## 5. Which side changes

For each difference, say which side should change and why. Intent decides,
in this order:

- **The doc**, when history (the pull request or commit that changed the
  code) shows the change was intended. Tests and code are the truth for
  intended behaviour. A check that fails only because it still asserts the
  old scenario is stale: it changes with the doc.
- **The code**, when nothing shows the change was intended and the scenario
  records a decision the user made, or a check of the current intended
  behaviour fails. That is a bug; name it.
- **The user**, when the evidence does not settle it. Ask one question at a
  time, or list it as open when the user is not there.

## Report

One section per doc: each difference with the doc line quoted, the code
location, the evidence (a deciding line or the file read), the side that
should change and the smallest fix; or "No drift". Write it to a dated file
outside the tree unless the project names a place, and give the summary with
its path. Each fix that follows is its own change: doc-only fixes together,
each code bug separately.
