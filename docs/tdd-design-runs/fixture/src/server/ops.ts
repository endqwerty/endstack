import { type Gate, type Result, type Run, verdictOf } from "../core/model";
import type { Store } from "./store";

/** Every operation the server offers, by name. Clients call them through `call`. */
export function operations(store: Store) {
	return {
		changes: async (_: {}) => store.changes(),
		gate: async ({ change }: { change: string }): Promise<Gate> => {
			const run = store.latest(change);
			return { change, run: run.id, head: run.head, verdict: verdictOf(run.results) };
		},
		/** Results of the latest run of a change. */
		results: async ({ change }: { change: string }): Promise<Result[]> => store.latest(change).results,
		/** Results of one run. */
		runResults: async ({ run }: { run: number }): Promise<Result[]> => store.run(run).results,
		history: async ({ change }: { change: string }): Promise<Run[]> => store.runsOf(change),
		owners: async (_: {}) => store.owners,
		prune: async ({ change, keep }: { change: string; keep: number }) => store.prune(change, keep),
	};
}

export type Ops = ReturnType<typeof operations>;
export type Call = <O extends keyof Ops>(op: O, input: Parameters<Ops[O]>[0]) => ReturnType<Ops[O]>;

export function caller(store: Store): Call {
	const ops = operations(store);
	return ((op, input) => (ops[op] as (i: unknown) => unknown)(input)) as Call;
}
