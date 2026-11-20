# Review

1. **The guard hides the bug (Fix Root Causes).** `!acct || !acct.plan` returns `{ ok: true }`. The state "account in cache with no plan, or missing from the cache" may be illegitimate. It likely comes from the disk-loaded cache after restart: a serialization or load problem, such as `Date` and `plan` fields not rehydrated, a partial load, or a race where requests arrive before the cache finishes loading. Fix: reproduce with a restart, inspect the actual cached state, and find what produced the missing `plan`. Fix that producer. Only keep a "no plan" branch if free or no-plan accounts are legitimate, and then handle it explicitly, not as a silent success.

2. **Swallowed error returns success (Fix Root Causes).** `catch (e) { return { ok: true }; }` turns every Stripe failure (declined card, network error, bug) into success and discards the state. Customers are not charged, yet the job reports ok. Fix: remove the catch, or catch only specific expected errors and return or throw a typed failure so the job fails visibly and can retry.

3. **Fix the pattern, not the instance (Fix Root Causes).** Other code reads `acct.plan` or uses `cache.get` the same way. `priceOf` uses `acct.plan!`, which has the same fault. Search every `cache.get(...) as Account` and `.plan` access and fix them all at the source.

4. **Cast instead of parsing at the boundary (Boundary Discipline, Type System Discipline).** `cache.get(id) as Account` trusts data loaded from disk on boot. Disk is a system boundary and external data is untyped until parsed. Fix: parse the cache file at load with a function (schema validation) that returns a typed `Account`, rejects or reports bad records at boot, and rehydrates `cancelledAt` to `Date`. The cache then holds only valid accounts, and `cache.get` needs no cast.

5. **Impossible states are representable (Type System Discipline).** `Account` has `active: boolean`, optional `cancelledAt`, and optional `plan`. This permits an active account with `cancelledAt`, or a cancelled account with no date, or an account with no plan. Fix: use a discriminated union, such as `{ status: 'active'; plan: Plan } | { status: 'cancelled'; cancelledAt: Date; plan?: Plan }`, so `plan` is required where charging is allowed, and `chargeAccount` accepts only the chargeable variant. This also removes the need for `!`.

6. **Redundant and contradictory checks inside the boundary (Boundary Discipline).** After a parse step, `!acct || !acct.plan` re-validates inside the system. Conversely, `plan!` in `priceOf` asserts a value the type says may be absent, so the two checks disagree. Pick one place to establish the invariant, at parse, and trust the types after.

7. **Needless layers (Minimize Reader Load).** `getPlanPrice` has one caller (and by the snippet none at all) and only forwards to `priceOf`. `priceOf` is a one-line accessor. Fix: delete `getPlanPrice`, inline `priceOf` to `acct.plan.priceCents`.

8. **Mixed shell and logic (Boundary Discipline).** `chargeAccount` combines cache lookup, eligibility rules, and the Stripe call. Fix: extract a pure function, for example `chargeAmount(acct): number | null` or a chargeability decision on the typed account. The async shell only looks up the account, calls that function, and calls Stripe.

9. **Hidden mutable state (Minimize Reader Load).** A module-level `cache` filled from disk at boot is global state that is hard to reason about ("where does X come from, what can change it?"). Fix: pass the account in, or inject a repository, so the source and the writers are explicit. Derive rather than sync.

10. **Missing signal (Fix Root Causes).** The error surfaced as an opaque TypeError after a restart. Add an always-on signal, such as logging and failing boot when cache records fail parsing, so the cause shows at first look.

11. **No reproduction or test.** The fix has no regression test. Add one that loads a persisted cache with a missing `plan`, restarts, and asserts the failure is surfaced at load or that charging fails loudly.
