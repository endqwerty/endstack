# Migrate Callers Then Delete Legacy APIs

When a new internal API replaces an old one and no external user needs compatibility, inventory the callers, migrate them, and delete the old API in the same wave. A temporary adapter is an exception with an end date. Update tests to assert the new contract, and delete tests that only protect the old implementation.
