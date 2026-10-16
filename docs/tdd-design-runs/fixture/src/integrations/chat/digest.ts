import { counts } from "../../core/model";
import { ownerOf } from "../../core/owners";
import type { Call } from "../../server/ops";

/** The message posted to the team chat when a change's gate settles. */
export async function digest(call: Call, change: string): Promise<string> {
	const { verdict, head } = await call("gate", { change });
	const latest = await call("results", { change });
	const owners = await call("owners", {});
	const c = counts(latest);
	const failing = latest
		.filter((r) => r.outcome === "failed")
		.map((r) => `• ${r.test}${ownerOf(r.test, owners) ? ` (${ownerOf(r.test, owners)})` : ""}`);
	return [`*${change}* @ ${head} is *${verdict}*: ${c.passed} passed, ${c.failed} failed`, ...failing].join("\n");
}
