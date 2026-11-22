export function lineCents(line) {
  return line.refunded ? 0 : line.qty * line.unitCents;
}

export function orderTotalCents(order) {
  return order.lines.reduce((sum, line) => sum + lineCents(line), 0);
}

export function formatCents(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}

export function createOrder({ id, lines }) {
  if (!Array.isArray(lines) || lines.length === 0) throw new Error('order needs lines');
  return { id, lines };
}
