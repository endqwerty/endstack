import { expect, test } from "bun:test";
import { history } from "../src/cli/commands/history";
import { list } from "../src/cli/commands/list";
import { show } from "../src/cli/commands/show";
import { setup } from "./helpers";

test("show prints the verdict and the results", async () => {
	const { store, api } = setup();
	store.push("feat", "a1", "robin", [{ test: "login", outcome: "failed", ms: 1200 }]);
	expect(await show(api, "feat")).toBe("feat @ a1: fail\n  failed  login (1.2 s)");
});

test("list prints one line per change", async () => {
	const { store, api } = setup();
	store.push("feat", "a1", "robin", [{ test: "login", outcome: "passed", ms: 10 }]);
	store.push("fix", "b2", "sam", [{ test: "login", outcome: "failed", ms: 10 }]);
	expect(await list(api)).toBe("pass    feat @ a1\nfail    fix @ b2");
});

test("history lists runs newest first", async () => {
	const { store, api } = setup();
	store.push("feat", "a1", "robin", [{ test: "login", outcome: "failed", ms: 10 }]);
	store.push("feat", "a2", "robin", [{ test: "login", outcome: "passed", ms: 10 }]);
	expect(await history(api, "feat")).toBe("#2 a2 by robin: 0 failures, 1 passed\n#1 a1 by robin: 1 failure, 0 passed");
});
