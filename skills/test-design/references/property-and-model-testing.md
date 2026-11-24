# Property-based and model-based testing

Use generated tests when a reachable fault lives across a large input space or many operation orders that hand-picked examples miss. Keep every kept property or model test fast, deterministic, and able to fail.

## Stateless property-based testing

Choose stateless property-based tests for pure or isolated logic with an observable invariant across many inputs:

- **Round-trips.** Encoding then decoding returns the original value.
- **Idempotence.** Applying a normalizer, formatter, or deduplicator twice matches applying it once.
- **Conservation and bounds.** Totals, balances, quotas, or item counts stay conserved and within domain bounds across splits, merges, or reallocations.
- **Reference equivalence.** An optimized implementation or refactor matches a simpler reference implementation on the same generated inputs.

Use properties when edge cases such as empty inputs, duplicates, boundary numbers, or unusual encodings are likely to break the invariant.

## Stateful model-based testing

Choose stateful model-based tests for components whose faults come from operation order: caches, queues, leases, state machines, storage layers, and sync loops.

1. Define a small reference model that tracks only the observable state of the component.
2. Define the public commands the component accepts, with preconditions that keep generated sequences in valid domain states.
3. Run generated command sequences against both the real code and the reference model, checking return values, errors, and state invariants after every step.

Prefer a stateful model test over a separate formal specification when single-process state transitions are the risk, because the test drives the real implementation and cannot drift silently from it. Use [formal-verification](../../formal-verification/SKILL.md) instead when you need exhaustive checks up to a bound, every concurrency interleaving, or an unbounded proof.

## When to stay with examples

Stick to example-based tests for thin glue code, route wiring, layout checks, one-off scripts, or rules with a small fixed set of cases. Do not write a property if asserting it would only duplicate the production algorithm.

## Guardrails

- **Independent oracle.** Derive expected results from the requirement, a simpler reference model, or an algebraic law, never by copying production logic into the test.
- **Targeted generators.** Generate valid domain shapes directly rather than filtering out most random inputs.
- **Deterministic every-change runs.** Fix the seed and bound the number of examples or command sequences in the every-change suite so runs stay fast and reproducible. Put deeper fuzzing or longer sequences on a daily or code-change schedule.
- **Shrinking and regression pins.** Keep shrinking enabled so a failure prints a minimal input or command sequence. When a generated run catches a real bug, pin the shrunk counterexample as a permanent regression case alongside the property.
- **Prove it fails.** Before keeping a property or model test, confirm it fails on a broken variant of the code it guards, such as a removed check or wrong state transition.
