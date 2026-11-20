---
name: drift
description: Compare what each design doc says a feature does with what its code and checks actually do, and report only the differences and which side should change.
disable-model-invocation: true
---

# Drift

A design doc's *Behaviour* scenarios say what its feature should do and its
*Plan* how; this skill finds where the code and checks now differ. It
reports; fixes go through [build](../build/SKILL.md).

## 1. Scope

The design doc directory the project's rules name, else `docs/design/`, or
the docs named; skip interview briefs (`*.brief.md`). One doc at a time, from
current files.

## 2. Expected

From the doc, list each behaviour scenario with its named check, and each
claim the *Plan* makes about files, symbols, fields, states, data shapes and
libraries. Open questions and alternatives turned down are not claims.

## 3. Actual

Find the code: follow the doc's links; where there are none, search for the
symbols it names and note the link the doc should carry. Read the code. For
each scenario:

- Does the named check exist and assert the scenario itself? Run it when it
  is local, read-only and cheap, and keep its deciding line; an unrun check
  is not a pass.
- Does the code do what the scenario says, including its edge and failure
  cases?

## 4. Differences

Report each way code and doc differ, and only differences:

- **Missing or changed behaviour**: a scenario or plan claim the code does
  not implement, or does differently.
- **Incomplete shape or shortcut**: fields, states or types the plan names
  are missing, or a fixed value stands where the plan describes logic.
- **Divergent design**: a different pattern, component or library than the
  plan's.
- **Broken check**: the named check is missing, fails, or could pass while
  its scenario is false.
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
- **The user**, when the evidence does not settle it: ask, or list it as
  open when the user is absent.

## Report

One section per doc: each difference with the doc line quoted, the code
location, the evidence (a deciding line or the file read), the side that
should change and the smallest fix; or "No drift".
