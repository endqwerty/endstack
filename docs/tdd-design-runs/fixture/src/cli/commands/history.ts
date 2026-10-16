import { counts } from "../../core/model";
import { plural } from "../../core/format";
import type { Api } from "../../server/api";

/** `gatekeep history <change>`: one line per run, newest first. */
export async function history(api: Api, change: string): Promise<string> {
	const runs = (await api.history(change)).slice().reverse();
	return runs
		.map((run) => {
			const c = counts(run.results);
			return `#${run.id} ${run.head} by ${run.author}: ${plural(c.failed, "failure")}, ${c.passed} passed`;
		})
		.join("\n");
}
