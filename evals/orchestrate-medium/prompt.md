---
name: orchestrate-medium
tags:
- orchestrate
- build
runs: 2
max_turns: 60
timeout_seconds: 1500
allowed_tools:
- Read
- Glob
- Grep
- Write
- Edit
- Bash
- Agent
---

Add multi-currency support to this shop, as one pull request. An order gets a `currency` of `USD`, `EUR` or `JPY`, defaulting to `USD`, and `createOrder` in `src/lib/orders.js` rejects any other code. Money is formatted by currency: `$12.34`, `€12.34`, and `¥1234` (yen has no minor unit, so `unitCents` holds whole yen). The command-line receipt, the web invoice and the mail summary each show the order's total in its currency. Add `src/export/csv.js`, exporting `ordersCsv(orders)`: a header row `id,currency,total` and one row per order with the total in minor units. Every part has tests. Tests run with `node --test`. There is no remote, so put the pull request title and description in your final reply. Do not ask questions; finish and summarize.
