import { test } from "node:test";
import assert from "node:assert/strict";
import { orderJson, ordersResponse } from "../src/api/orders.js";

test("orderJson exposes the total in cents", () => {
  assert.deepEqual(orderJson({ id: 7, created_at: "2024-03-01", total_cents: 1234 }), {
    id: 7,
    createdAt: "2024-03-01",
    totalCents: 1234,
  });
});

test("ordersResponse wraps the rows", () => {
  assert.equal(ordersResponse([{ id: 1, created_at: "2024-05-05", total_cents: 5 }]).orders.length, 1);
});
