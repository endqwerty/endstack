Apply the skill to this diff. You have no tools and no separate workers: act as the comment reviewer yourself. For EACH numbered comment, say keep or delete, and for a keep, the exact text it would have after your pass. Then list any MUST KILL flags. No other output.

```ts
// (1) Copyright 2026 Acme Inc. Licensed under the MIT License.
#!/usr/bin/env node  // (2) shebang line
// (3) Loop over the orders and add up totals
export function total(orders: Order[]): number {
  let sum = 0;
  for (const o of orders) sum += o.cents;
  return sum;
}

/** (4) Returns the order total in cents. Throws if any order is negative. */
export function checkedTotal(orders: Order[]): number { /* ... */ }

// (5) Safari 17 drops the first `resize` event after a rotation; we listen twice. See https://bugs.webkit.org/show_bug.cgi?id=271234
window.addEventListener("resize", onResize);

// (6) IMPORTANT: do not remove. cache must be warmed before start() or the first request 500s
warmCache();
start();

// prettier-ignore  (7)
const MATRIX = [1,0,0, 0,1,0, 0,0,1];

// istanbul ignore next  (8)
function debugDump() {}

// (9) Tracked in https://github.com/acme/app/issues/88: the API returns ids as strings until v3
const id = Number(raw.id);
```
