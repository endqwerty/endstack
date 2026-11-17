import { afterAll, expect, test } from "bun:test";
import { start } from "../src/server.ts";

const server = start();
afterAll(() => server.stop());

async function checkout(body: unknown) {
  const res = await fetch(new URL("/checkout", server.url), { method: "POST", body: JSON.stringify(body) });
  return { status: res.status, body: await res.json() };
}

test("checkout replies with the total in cents", async () => {
  const r = await checkout({ items: [{ sku: "a", cents: 1000, qty: 1 }] });
  expect(r).toEqual({ status: 200, body: { totalCents: 1000 } });
});

test("checkout applies a percent coupon", async () => {
  const r = await checkout({ items: [{ sku: "a", cents: 1000, qty: 1 }], coupon: { percent: 25 } });
  expect(r.body.totalCents).toBe(750);
});
