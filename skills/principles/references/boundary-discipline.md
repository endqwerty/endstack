# Boundary Discipline

Validate, narrow types, and handle errors where data crosses a system boundary (CLI args, config files, external APIs, network). A fresh import or external read is a new boundary. Parse raw data into domain types there, and keep transport and framework types out of the public surface.

- Inside, trust the guarantees actually established: no re-validation of what a schema, validating constructor or internal type already proved. A cast is not validation, and shape validation does not prove authorization or current business state.
- Catch an error only to recover, translate it into the boundary's error contract, or add context. Otherwise let it propagate with its cause. Never turn an unexpected failure into a successful-looking default.
- Business logic lives in pure functions with no framework dependencies. The shell that calls them is thin.

Two tests. What guarantee already holds, and what new unvalidated path reaches this check? Can this be pure logic the shell just calls?
