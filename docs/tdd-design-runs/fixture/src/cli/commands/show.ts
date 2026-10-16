import { duration } from "../../core/format";
import type { Api } from "../../server/api";

/** `gatekeep show <change>`: the verdict, then one line per result. */
export async function show(api: Api, change: string): Promise<string> {
	const gate = await api.gate(change);
	const results = await api.results(change);
	const lines = results.map((r) => `  ${r.outcome.padEnd(7)} ${r.test} (${duration(r.ms)})`);
	return [`${change} @ ${gate.head}: ${gate.verdict}`, ...lines].join("\n");
}
