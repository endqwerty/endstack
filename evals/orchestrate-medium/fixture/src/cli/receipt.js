import { orderTotalCents, formatCents } from '../lib/orders.js';

export function receipt(order) {
  const rows = order.lines.map((l) => `${l.sku} x${l.qty}${l.refunded ? ' (refunded)' : ''}`);
  return [...rows, `Total: ${formatCents(orderTotalCents(order))}`].join('\n');
}
