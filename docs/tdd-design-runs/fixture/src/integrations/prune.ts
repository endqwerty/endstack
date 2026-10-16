import type { Call } from "../server/ops";

/** Keep only the newest `keep` runs of every change. */
export async function pruneAll(call: Call, keep: number): Promise<number> {
	let dropped = 0;
	for (const change of await call("changes", {})) dropped += await call("prune", { change, keep });
	return dropped;
}
