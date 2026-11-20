import { formatCents } from '../lib/orders.js';

export function invoiceHtml(order) {
  let total = 0;
  for (const item of order.lines) total += item.qty * item.unitCents;
  const rows = order.lines.map((l) => `<tr><td>${l.sku}</td><td>${l.qty}</td></tr>`).join('');
  return `<table>${rows}</table><p class="total">${formatCents(total)}</p>`;
}
