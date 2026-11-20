import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatCents } from '../src/lib/orders.js';

test('formatCents shows dollars with two decimals', () => {
  assert.equal(formatCents(1234), '$12.34');
});
