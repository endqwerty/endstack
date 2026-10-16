import { duration } from "../../core/format";
import type { Api } from "../../server/api";

/** `gatekeep slowest <run> [n]`: the n slowest tests of a run. */
export async function slowest(api: Api, run: number, n = 5): Promise<string> {
	const results = (await api.runResults(run)).slice().sort((a, b) => b.ms - a.ms).slice(0, n);
	return results.map((r) => `${duration(r.ms).padStart(10)} ${r.test}`).join("\n");
}
