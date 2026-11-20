---
name: principles-review
tags:
- principles
- verify
- typescript-best-practices
runs: 3
max_turns: 12
timeout_seconds: 300
allowed_tools:
- Read
- Glob
- Grep
---

Review this TypeScript fix before I merge it. List every problem you would raise, each with its fix. There is no checkout; the code below is all there is.

The bug: after a server restart, some users see "Cannot read properties of undefined (reading 'plan')". The author's fix:

```ts
// billing/service.ts
type Account = { id: string; active: boolean; cancelledAt?: Date; plan?: Plan };

export async function chargeAccount(id: string) {
  const acct = cache.get(id) as Account;          // cache is loaded from disk on boot
  if (!acct || !acct.plan) return { ok: true };    // NEW: guard added by this fix
  try {
    return await stripeCharge(acct.id, acct.plan.priceCents);
  } catch (e) {
    return { ok: true };                           // NEW: don't fail the job
  }
}

function getPlanPrice(acct: Account) { return priceOf(acct); }  // one caller
function priceOf(acct: Account) { return acct.plan!.priceCents; }
```
