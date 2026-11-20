#!/usr/bin/env node  // shebang line
// Copyright 2026 Acme Inc. Licensed under the MIT License.
import type { Order } from "./runtime.ts";
import { onResize, raw, start, warmCache } from "./runtime.ts";

// Loop over the orders and add up totals
export function total(orders: Order[]): number {
  let sum = 0;
  for (const o of orders) sum += o.cents;
  return sum;
}

/** Returns the order total in cents. Throws if any order is negative. */
export function checkedTotal(orders: Order[]): number {
  if (orders.some((o) => o.cents < 0)) throw new Error("negative order");
  return total(orders);
}

// Safari 17 drops the first `resize` event after a rotation; we listen twice. See https://bugs.webkit.org/show_bug.cgi?id=271234
window.addEventListener("resize", onResize);
window.addEventListener("orientationchange", onResize);

// IMPORTANT: do not remove. cache must be warmed before start() or the first request 500s
warmCache();
start();

// prettier-ignore
export const MATRIX = [1,0,0, 0,1,0, 0,0,1];

// istanbul ignore next
function debugDump() {}

// Tracked in https://github.com/acme/app/issues/88: the API returns ids as strings until v3
export const id = Number(raw.id);
