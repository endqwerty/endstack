import type { Result, Run } from "../core/model";

export class Store {
	private runs: Run[] = [];
	owners: Record<string, string> = {};

	push(change: string, head: string, author: string, results: Result[]): Run {
		const run = { id: this.runs.length + 1, change, head, author, results };
		this.runs.push(run);
		return run;
	}
	runsOf(change: string): Run[] {
		return this.runs.filter((r) => r.change === change);
	}
	latest(change: string): Run {
		const run = this.runsOf(change).at(-1);
		if (!run) throw new Error(`no runs for ${change}`);
		return run;
	}
	run(id: number): Run {
		const run = this.runs.find((r) => r.id === id);
		if (!run) throw new Error(`no run ${id}`);
		return run;
	}
	changes(): string[] {
		return [...new Set(this.runs.map((r) => r.change))];
	}
	prune(change: string, keep: number): number {
		const runs = this.runsOf(change);
		const drop = new Set(runs.slice(0, Math.max(0, runs.length - keep)).map((r) => r.id));
		this.runs = this.runs.filter((r) => !drop.has(r.id));
		return drop.size;
	}
}
