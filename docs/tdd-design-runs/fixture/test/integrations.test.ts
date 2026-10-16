import { expect, test } from "bun:test";
import { digest } from "../src/integrations/chat/digest";
import { commitStatus } from "../src/integrations/github/status";
import { setup } from "./helpers";

test("the digest names failing tests and their owners", async () => {
	const { store, call } = setup();
	store.owners = { "auth.": "identity" };
	store.push("feat", "a1", "robin", [
		{ test: "auth.login", outcome: "failed", ms: 5 },
		{ test: "cart.add", outcome: "passed", ms: 5 },
	]);
	expect(await digest(call, "feat")).toBe("*feat* @ a1 is *fail*: 1 passed, 1 failed\n• auth.login (identity)");
});

test("the commit status follows the verdict", async () => {
	const { store, call } = setup();
	store.push("feat", "a1", "robin", [{ test: "x", outcome: "passed", ms: 1 }]);
	expect(await commitStatus(call, "feat")).toEqual({ sha: "a1", state: "success", description: "gatekeep: pass" });
});
