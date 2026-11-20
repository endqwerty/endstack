import { test } from "node:test";
import assert from "node:assert/strict";
import { withRetry } from "../src/queue/retry.ts";

test("withRetry returns the first success", async () => {
  let calls = 0;
  const result = await withRetry(async () => {
    calls++;
    if (calls < 2) throw new Error("flaky");
    return "ok";
  }, { maxAttempts: 3, baseMs: 1, capMs: 10, sleep: async () => {} });
  assert.equal(result, "ok");
});
