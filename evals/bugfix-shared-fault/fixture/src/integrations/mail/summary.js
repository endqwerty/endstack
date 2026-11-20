import { orderTotalCents, formatCents } from '../../lib/orders.js';

export function mailSummary(order) {
  return `Your order ${order.id}: ${order.lines.length} items, ${formatCents(orderTotalCents(order))}`;
}
