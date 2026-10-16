import type { Gate, Result, Run } from "../core/model";
import type { Call } from "./ops";

/** The typed client the command line uses. */
export interface Api {
	gate(change: string): Promise<Gate>;
	results(change: string): Promise<Result[]>;
	runResults(run: number): Promise<Result[]>;
	history(change: string): Promise<Run[]>;
	changes(): Promise<string[]>;
}

export function api(call: Call): Api {
	return {
		gate: (change) => call("gate", { change }),
		results: (change) => call("results", { change }),
		runResults: (run) => call("runResults", { run }),
		history: (change) => call("history", { change }),
		changes: () => call("changes", {}),
	};
}
