import { expect, test } from "bun:test";
import { describe } from "./core/tracker";
import { Requests } from "./server/trackers";

test("a delivered request records its issue", async () => {
	const requests = new Requests({ create: async () => ({ key: "BUG-1", url: "https://t.example/BUG-1" }) });
	const r = requests.request("login");
	await requests.deliver();
	expect(describe(requests.get(r.id)!)).toBe("login: filed as BUG-1");
});

test("a failed request records the error", async () => {
	const requests = new Requests({ create: async () => { throw new Error("tracker down"); } });
	const r = requests.request("login");
	await requests.deliver();
	expect(describe(requests.get(r.id)!)).toBe("login: could not be filed (Error: tracker down)");
});
