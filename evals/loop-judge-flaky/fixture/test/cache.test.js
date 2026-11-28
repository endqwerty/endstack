import { test } from "node:test";
import assert from "node:assert/strict";
import { TtlCache } from "../src/cache.js";

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

test("keeps a fresh entry", () => {
  const cache = new TtlCache(50);
  cache.set("a", 1);
  assert.equal(cache.get("a"), 1);
});

test("expires an entry once its ttl has passed", { timeout: 1000 }, async () => {
  const cache = new TtlCache(50);
  cache.set("a", 1);
  await sleep(50);
  assert.equal(cache.get("a"), undefined);
});
