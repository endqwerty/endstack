import { type Gate, type Result, type Run, verdictOf } from "../core/model";

export interface Api {
	gate(change: string): Promise<Gate>;
	/** Results of the latest run of a change. */
	results(change: string): Promise<Result[]>;
	/** Results of one run. */
	runResults(run: number): Promise<Result[]>;
}

export class Store implements Api {
	private runs: Run[] = [];
	push(change: string, head: string, results: Result[]): Run {
		const run = { id: this.runs.length + 1, change, head, results };
		this.runs.push(run);
		return run;
	}
	private latest(change: string): Run {
		const run = this.runs.filter((r) => r.change === change).at(-1);
		if (!run) throw new Error(`no runs for ${change}`);
		return run;
	}
	async gate(change: string): Promise<Gate> {
		const run = this.latest(change);
		return { change, run: run.id, head: run.head, verdict: verdictOf(run.results) };
	}
	async results(change: string): Promise<Result[]> {
		return this.latest(change).results;
	}
	async runResults(id: number): Promise<Result[]> {
		const run = this.runs.find((r) => r.id === id);
		if (!run) throw new Error(`no run ${id}`);
		return run.results;
	}
}
