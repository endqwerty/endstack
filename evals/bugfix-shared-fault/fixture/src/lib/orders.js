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
