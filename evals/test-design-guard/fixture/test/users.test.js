import { test } from "node:test";
import assert from "node:assert/strict";
import { handle } from "../src/app.js";

test("deleting users needs users:write", () => {
  assert.equal(handle("DELETE", "/admin/users", { permissions: ["users:read"] }).status, 403);
  assert.equal(handle("DELETE", "/admin/users", { permissions: ["users:write"] }).status, 200);
});
