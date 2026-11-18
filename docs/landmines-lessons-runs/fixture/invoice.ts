export type Line = { sku: string; cents: number; qty: number };
export type Invoice = { id: string; lines: Line[] };

export function invoiceTotal(invoice: Invoice) {
  return invoice.lines.reduce((sum, line) => sum + line.cents * line.qty, 0);
}
