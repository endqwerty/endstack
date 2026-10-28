# Boundary Discipline

Place validation, type narrowing, and error handling at system boundaries. Pass validated domain values inward and trust the guarantees actually established. Business logic lives in pure functions. The shell is thin and mechanical.

**Why:** Scattered validation is noisy, redundant, and gives a false sense of safety. Keep logic out of framework wiring so it can be tested without the framework.

**The pattern:**
- **At boundaries** (CLI args, config files, external APIs, network protocols): validate, return errors, handle defensively.
- **Inside the system:** typed data, error propagation, no re-validation. Trust the types.
- **Across the boundary.** Expose domain concepts, not the boundary's private representation. Keep general-purpose mechanism inside and special-purpose policy at the edge.

**Applications:**

Validation and error handling:
- Validate config at parse time (the boundary), not inside business logic
- Parse raw data into domain types at the boundary
- Do not re-export transport, storage, framework, or wire types through the public surface
- Validate unknown values once at the boundary that owns them. Pass typed values inward instead of repeating object and property-existence checks.
- Do not defensively revalidate guarantees established by a schema, validating constructor or internal type. A cast or type annotation does not validate external data. Shape validation does not establish authorization or mutable business state.
- A fresh import or external read is a new boundary. Checking a valid union's variant or a changing business condition is ordinary logic, not redundant validation.
- Catch errors where you can recover, translate them into the boundary's error contract, or add necessary context. Otherwise let them propagate. Keep the protected operation narrow, preserve the original cause, and do not turn unexpected failures into successful-looking defaults. Use finally for cleanup even when no catch is needed.

Code organization:
- Business logic in pure functions with no framework dependencies
- Parse functions: pure transforms from raw bytes to typed state
- Prompt construction: structured state in, string out
- Scoring and assessment: pure transforms from state to results

**The tests:**
- What guarantee already holds, and what new unvalidated path reaches this check?
- Can this be pure logic? Keep it free of framework wiring, then apply the [reader-load rule](minimize-reader-load.md) to decide whether extraction helps.
