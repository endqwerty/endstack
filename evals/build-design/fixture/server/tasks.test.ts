import { test } from "node:test";
import assert from "node:assert/strict";
import { TaskStore } from "./tasks.ts";

test("patch marks a task done", () => {
  const store = new TaskStore();
  store.create("1", "write report");
  assert.equal(store.patch("1", { done: true }).done, true);
});

test("patch deletes a task and keeps the first deletion time", () => {
  const store = new TaskStore();
  store.create("1", "write report");
  const first = new Date("2026-01-01T00:00:00Z");
  store.patch("1", { deleted: true }, first);
  const again = store.patch("1", { deleted: true }, new Date("2026-02-01T00:00:00Z"));
  assert.deepEqual(again.deletedAt, first);
});
