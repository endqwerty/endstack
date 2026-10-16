import { expect, test } from "bun:test";
import { flakyTests } from "../src/core/flaky";
import { duration } from "../src/core/format";
import { ownerOf } from "../src/core/owners";

test("duration", () => {
	expect(duration(250)).toBe("250 ms");
	expect(duration(1500)).toBe("1.5 s");
	expect(duration(125000)).toBe("2 min 5 s");
});

test("ownerOf takes the longest prefix", () => {
	expect(ownerOf("auth.login.sso", { "auth.": "identity", "auth.login.": "sso-team" })).toBe("sso-team");
});

test("flakyTests finds a test that passed and failed on one head", () => {
	const r = (outcome: "passed" | "failed") => [{ test: "t", outcome, ms: 1 }];
	expect(flakyTests([{ id: 1, change: "c", head: "h", author: "a", results: r("passed") }, { id: 2, change: "c", head: "h", author: "a", results: r("failed") }])).toEqual(["t"]);
});
