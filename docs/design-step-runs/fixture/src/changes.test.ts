import { expect, test } from "bun:test";
import { show } from "./cli/changes";
import { Store } from "./server/api";
import { changePage } from "./web/changes";

test("show prints the verdict and the results", async () => {
	const store = new Store();
	store.push("feat", "a1", [{ test: "login", outcome: "failed" }]);
	expect(await show(store, "feat")).toBe("feat @ a1: fail\n  failed  login");
});

test("the change page shows the verdict and the results", async () => {
	const store = new Store();
	store.push("feat", "a1", [{ test: "login", outcome: "passed" }]);
	expect(await changePage(store, "feat")).toBe('<h1>feat @ a1: pass</h1><ul><li class="passed">login</li></ul>');
});
