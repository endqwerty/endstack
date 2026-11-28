import { test } from "node:test";
import assert from "node:assert/strict";
import { slugify } from "../src/slug.js";

test("lowercases and joins words", () => {
  assert.equal(slugify("Hello World"), "hello-world");
});

test("lowercases a single word", () => {
  assert.equal(slugify("Hello"), "hello");
});

test("lowercases two words", () => {
  assert.equal(slugify("Hello There"), "hello-there");
});

test("lowercases three words", () => {
  assert.equal(slugify("Hello There Friend"), "hello-there-friend");
});

test("strips accents", () => {
  assert.equal(slugify("Crème Brûlée"), "creme-brulee");
});

test("collapses punctuation and trims separators", () => {
  assert.equal(slugify("  Hello, World!  "), "hello-world");
});

test("uses the SEPARATORS regex", async () => {
  const source = await import("node:fs").then((fs) => fs.readFileSync(new URL("../src/slug.js", import.meta.url), "utf8"));
  assert.ok(source.includes("const SEPARATORS = /[^a-z0-9]+/g;"));
});

test("returns a string", () => {
  assert.equal(typeof slugify("x"), "string");
});
