import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createOrder, formatCents, orderTotalCents } from '../src/lib/orders.js';
import { receipt } from '../src/cli/receipt.js';

test('formatCents shows dollars with two decimals', () => {
  assert.equal(formatCents(1234), '$12.34');
});

test('refunded lines do not count toward the total', () => {
  const order = createOrder({ id: 'o1', lines: [{ sku: 'A', qty: 2, unitCents: 500 }, { sku: 'B', qty: 1, unitCents: 300, refunded: true }] });
  assert.equal(orderTotalCents(order), 1000);
  assert.match(receipt(order), /Total: \$10\.00/);
});
