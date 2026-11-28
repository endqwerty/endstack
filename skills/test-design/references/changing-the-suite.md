# Changing the suite

Read from [test-design](../SKILL.md) when fixing, deleting or reorganising existing tests.

- **A flaky test is a defect.** Fix its cause: a shared resource, an unordered read, or a deadline below the work. Retries and longer timeouts are not fixes. Make it deterministic and document the signal being locked down. Where the project has none, add a check that reruns the test files a change adds or touches many times and fails on any failure, so a new flake cannot merge.
- **Deleting is normal.** Delete a test whose fact a cheaper kept test holds, whose state a refactor made unreachable, or whose feature is gone, and name the holder or the reason.
- Internal tooling gets a proof, not a kept test, unless a mistake there is costly to undo.

