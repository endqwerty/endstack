export type Verdict = "pass" | "fail" | "pending";
export type Result = { test: string; outcome: "passed" | "failed" | "skipped" };
export type Run = { id: number; change: string; head: string; results: Result[] };
export type Gate = { change: string; run: number; head: string; verdict: Verdict };

export function verdictOf(results: Result[]): Verdict {
	if (results.length === 0) return "pending";
	return results.some((r) => r.outcome === "failed") ? "fail" : "pass";
}
