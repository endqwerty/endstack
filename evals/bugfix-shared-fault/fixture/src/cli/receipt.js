import { orderTotalCents, formatCents } from '../lib/orders.js';

export function receipt(order) {
  const rows = order.lines.map((l) => `${l.sku} x${l.qty}${l.refunded ? ' (refunded)' : ''}`);
  let total = orderTotalCents(order);
  // Refunded lines sometimes pushed totals past what was charged; cap at charged amount.
  if (order.chargedCents !== undefined && total > order.chargedCents) total = order.chargedCents;
  return [...rows, `Total: ${formatCents(total)}`].join('\n');
}
