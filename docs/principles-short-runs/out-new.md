# Review of chargeAccount fix

1. **Swallowed error returns success** (Boundary Discipline: catch only to recover/translate/add context; never turn an unexpected failure into a successful-looking default). `catch (e) { return { ok: true }; }` reports a failed Stripe charge as ok. Fix: remove the try/catch and let the error propagate with its cause. If the job needs a failure result, translate to the boundary's error contract (`{ ok: false, error }`) with the cause attached, never `ok: true`.

2. **New guard hides the bug** (Fix Root Causes). `if (!acct || !acct.plan) return { ok: true }` silently skips charging. A missing account or plan after restart is probably not a legitimate state, so the guard clamps the symptom and some users are never billed. Find what produced an account with no plan: the disk cache load on boot. Ask whether plan-less accounts are legitimate (for example a free tier). If they are, model that explicitly and return a meaningful result, not `ok: true` by accident. If not, fail loudly.

3. **Cast instead of parsing at the boundary** (Boundary Discipline; Type System Discipline: don't lie to the type system, external data is untyped until parsed). `cache.get(id) as Account` asserts a type for data loaded from disk. This is the latent crash that caused the bug. Fix: parse the persisted cache at load with a schema or validating function, returning a typed domain model, and reject or repair bad records there. The `!acct` check also shows the cast lies, because `get` can return undefined.

4. **Persisted state is the first suspect** (Fix Root Causes: a failure only after restart points to persisted state). Inspect what is written to disk and what is read back. Likely causes: the serializer drops `plan`, `Date` values round-trip as strings, or the schema or version changed. Reproduce first with a test that saves, reloads and charges. Fix the write or read path, then find every other field with the same fault (the `cancelledAt` Date is a likely one).

5. **Illegal states representable** (Type System Discipline). `{ active: boolean; cancelledAt?: Date; plan?: Plan }` allows contradictions such as active with cancelledAt, or active with no plan. Fix with a sum type, for example `{ kind: 'active'; plan: Plan } | { kind: 'cancelled'; at: Date; plan?: Plan }`. Then `chargeAccount` accepts only the chargeable variant, and the optional `plan` and the `!` disappear. Apply this only where the partiality shows up, which here it does: the guard and the non-null assertion.

6. **Non-null assertion** (Type System Discipline). `acct.plan!.priceCents` in `priceOf` is a cast that bypasses the compiler. It is the same crash waiting to happen. It goes away with item 5.

7. **Pass-through layers** (Minimize Reader Load). `getPlanPrice` forwards to `priceOf` and has one caller. `priceOf` is a one-line accessor. Neither hides a boundary or clarifies a caller. Collapse them. `getPlanPrice` also looks unused, because `chargeAccount` reads `acct.plan.priceCents` directly. That makes it dead code and a second place that could disagree about the price. Delete it, or have the one real path use a single helper.

8. **Hidden module state** (Minimize Reader Load). `chargeAccount` reads a global `cache`, so "where does X come from, and what can change it" needs tracing. Fix: pass the account in, or load it at the edge, so billing is a function from a validated `Account` to a charge. This also fits "business logic in pure functions with a thin shell": the lookup and the Stripe call are the shell, and price and eligibility are pure.

9. **No test or signal for the regression** (Fix Root Causes: reproduce first; add a cheap always-on signal). No test demonstrates the failure. Add a restart round-trip test, and log or metric on an account that fails parsing on load, so the cause is visible at first look next time.

10. **Id mismatch risk** (Boundary Discipline). It charges `acct.id`, not the `id` argument. If the cache is keyed differently from `acct.id`, that charges the wrong account. Validate that they match at load time, or use the argument.

Summary: remove the swallow and the guard. Parse the cache at load into a sum type that makes a chargeable account carry a plan. Fix the persistence round-trip. Delete the pass-through helpers.
