import { expect, test } from "bun:test";
import { subtotal, total } from "./cart.ts";

const items = [{ sku: "a", cents: 1000, qty: 2 }, { sku: "b", cents: 500, qty: 1 }];

test("subtotal adds price times quantity", () => {
  expect(subtotal(items)).toBe(2500);
});

test("a percent coupon takes its share off the subtotal", () => {
  expect(total(items, { percent: 10 })).toBe(2250);
});

test("a fixed coupon takes its amount off the subtotal", () => {
  expect(total(items, { cents: 300 })).toBe(2200);
});
