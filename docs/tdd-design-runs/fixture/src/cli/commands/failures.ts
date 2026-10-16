import type { Api } from "../../server/api";

/** `gatekeep failures <change> <run>`: the failed tests of one run. */
export async function failures(api: Api, run: number): Promise<string> {
	const results = await api.runResults(run);
	return results.filter((r) => r.outcome === "failed").map((r) => r.test).join("\n");
}
