# Type System Discipline

Make the compiler reject impossible states, mismatched primitives, and unhandled variants.

- **Make illegal states unrepresentable.** Model variants as sum types, not optional fields whose contradictory combinations compile: `{ kind: 'open' } | { kind: 'done'; at: Date }`, not `{ completed: boolean; completedAt?: Date }`.
- **Brand semantic primitives.** If two arguments share a primitive type but mean different things, give each its own type. Validate once at creation.
- **External data is untyped until parsed.** JSON, RPC payloads, CLI args, config, environment variables, and database rows go through a parse function at the boundary that returns the typed model.
- **Don't lie to the type system.** A cast or assertion that bypasses the compiler is a latent crash. Prove the fact at the boundary instead.
- **Make matches exhaustive,** so adding a variant fails compilation where a case is missing.
- **Derive types from authoritative schemas** instead of hand-rolling a parallel one.
- **Strengthen a type only where partiality appears:** where a runtime assertion or "never happens" throw would otherwise sit. Then stop.

For TypeScript syntax, see the [typescript-best-practices](../../typescript-best-practices/SKILL.md) skill.
