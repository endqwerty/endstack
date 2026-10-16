export type Verdict = "pass" | "fail" | "pending";
export type Outcome = "passed" | "failed" | "skipped";
export type Result = { test: string; outcome: Outcome; ms: number };
export type Run = { id: number; change: string; head: string; author: string; results: Result[] };
export type Gate = { change: string; run: number; head: string; verdict: Verdict };

export function verdictOf(results: Result[]): Verdict {
	if (results.length === 0) return "pending";
	return results.some((r) => r.outcome === "failed") ? "fail" : "pass";
}

export function counts(results: Result[]): Record<Outcome, number> {
	const c = { passed: 0, failed: 0, skipped: 0 };
	for (const r of results) c[r.outcome]++;
	return c;
}
