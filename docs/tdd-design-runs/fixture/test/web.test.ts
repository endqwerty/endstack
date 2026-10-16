import { expect, test } from "bun:test";
import { changePage } from "../src/web/pages/change";
import { setup } from "./helpers";

test("the change page shows the verdict and the results", async () => {
	const { store, call } = setup();
	store.push("feat", "a1", "robin", [{ test: "login", outcome: "passed", ms: 5 }]);
	expect(await changePage(call, "feat")).toContain("<h1>feat @ a1: pass</h1>");
});
