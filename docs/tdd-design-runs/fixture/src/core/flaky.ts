import type { Run } from "./model";

/** Tests that both passed and failed across the given runs of one head. */
export function flakyTests(runs: Run[]): string[] {
	const seen = new Map<string, Set<string>>();
	for (const run of runs)
		for (const r of run.results) {
			const key = `${run.head}:${r.test}`;
			const outcomes = seen.get(key) ?? new Set<string>();
			outcomes.add(r.outcome);
			seen.set(key, outcomes);
		}
	const flaky = new Set<string>();
	for (const [key, outcomes] of seen) if (outcomes.has("passed") && outcomes.has("failed")) flaky.add(key.split(":")[1]);
	return [...flaky].sort();
}
