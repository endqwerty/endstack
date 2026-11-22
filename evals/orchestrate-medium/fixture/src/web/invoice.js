import { orderTotalCents, formatCents } from '../lib/orders.js';

export function invoiceHtml(order) {
  const rows = order.lines.map((l) => `<tr><td>${l.sku}</td><td>${l.qty}</td></tr>`).join('');
  return `<table>${rows}</table><p class="total">${formatCents(orderTotalCents(order))}</p>`;
}
