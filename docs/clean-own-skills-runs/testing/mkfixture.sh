#!/bin/bash
set -e
R=$(cd "$(dirname "$0")/../../.." && pwd)
S=$1
F=$S/fixture; mkdir -p $F/src/lib $F/src/cli $F/src/web $F/src/integrations/mail $F/test
cat > $F/package.json <<'EOF'
{ "name": "shop", "type": "module", "scripts": { "test": "node --test test/" } }
EOF
cat > $F/src/lib/orders.js <<'EOF'
// An order line: { sku, qty, unitCents, refunded }
export function lineCents(line) {
  return line.qty * line.unitCents;
}

export function orderTotalCents(order) {
  return order.lines.reduce((sum, line) => sum + lineCents(line), 0);
}

export function formatCents(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
EOF
cat > $F/src/cli/receipt.js <<'EOF'
import { orderTotalCents, formatCents } from '../lib/orders.js';

export function receipt(order) {
  const rows = order.lines.map((l) => `${l.sku} x${l.qty}${l.refunded ? ' (refunded)' : ''}`);
  let total = orderTotalCents(order);
  // Refunded lines sometimes pushed totals past what was charged; cap at charged amount.
  if (order.chargedCents !== undefined && total > order.chargedCents) total = order.chargedCents;
  return [...rows, `Total: ${formatCents(total)}`].join('\n');
}
EOF
cat > $F/src/web/invoice.js <<'EOF'
import { formatCents } from '../lib/orders.js';

export function invoiceHtml(order) {
  let total = 0;
  for (const item of order.lines) total += item.qty * item.unitCents;
  const rows = order.lines.map((l) => `<tr><td>${l.sku}</td><td>${l.qty}</td></tr>`).join('');
  return `<table>${rows}</table><p class="total">${formatCents(total)}</p>`;
}
EOF
cat > $F/src/integrations/mail/summary.js <<'EOF'
import { orderTotalCents, formatCents } from '../../lib/orders.js';

export function mailSummary(order) {
  return `Your order ${order.id}: ${order.lines.length} items, ${formatCents(orderTotalCents(order))}`;
}
EOF
cat > $F/src/lib/sku.js <<'EOF'
export function normalizeSku(s) { return s.trim().toUpperCase(); }
EOF
cat > $F/test/orders.test.js <<'EOF'
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatCents } from '../src/lib/orders.js';

test('formatCents shows dollars with two decimals', () => {
  assert.equal(formatCents(1234), '$12.34');
});
EOF
cat > $F/test/sku.test.js <<'EOF'
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeSku } from '../src/lib/sku.js';
test('normalizeSku trims and uppercases', () => { assert.equal(normalizeSku(' ab '), 'AB'); });
EOF
for arm in old new; do
  A=$S/$arm; mkdir -p $A/skills; cp -r $F $A/repo; cp -r $R/skills/principles $A/skills/
  (cd $A/repo && git init -q && git add -A && git -c user.name=t -c user.email=t@t commit -qm init)
done
mkdir -p $S/old/skills/tdd $S/old/skills/test-design $S/new/skills/test-design
(cd $R && git show 05cad93:skills/tdd/SKILL.md > $S/old/skills/tdd/SKILL.md && git show 05cad93:skills/test-design/SKILL.md > $S/old/skills/test-design/SKILL.md)
cp $R/skills/test-design/SKILL.md $S/new/skills/test-design/SKILL.md
cd $S/old/repo && npm test 2>&1 | tail -3
