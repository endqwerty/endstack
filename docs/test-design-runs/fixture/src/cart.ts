export type Item = { sku: string; cents: number; qty: number };
export type Coupon = { percent: number } | { cents: number };

export function subtotal(items: Item[]): number {
  return items.reduce((sum, i) => sum + i.cents * i.qty, 0);
}

export function total(items: Item[], coupon?: Coupon): number {
  const s = subtotal(items);
  if (!coupon) return s;
  if ("percent" in coupon) return Math.round(s * (1 - coupon.percent / 100));
  return s - coupon.cents;
}
