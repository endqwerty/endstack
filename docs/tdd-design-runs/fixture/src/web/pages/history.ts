import { counts } from "../../core/model";
import { escapeHtml } from "../../core/format";
import type { Call } from "../../server/ops";
import { page } from "../layout";

/** /changes/:name/history — every run of a change. */
export async function historyPage(call: Call, name: string): Promise<string> {
	const runs = await call("history", { change: name });
	const rows = runs
		.map((run) => {
			const c = counts(run.results);
			return `<tr><td>#${run.id}</td><td>${escapeHtml(run.head)}</td><td>${c.failed}</td><td>${c.passed}</td></tr>`;
		})
		.join("");
	return page(`${name} history`, `<table>${rows}</table>`);
}
