import { duration, escapeHtml } from "../../core/format";
import type { Call } from "../../server/ops";
import { page } from "../layout";

/** /changes/:name — the gate's verdict and the results behind it. */
export async function changePage(call: Call, name: string): Promise<string> {
	const verdict = await call("gate", { change: name });
	const rows = await call("results", { change: name });
	const items = rows
		.map((r) => `<li class="${r.outcome}">${escapeHtml(r.test)} <small>${duration(r.ms)}</small></li>`)
		.join("");
	return page(name, `<h1>${escapeHtml(name)} @ ${verdict.head}: ${verdict.verdict}</h1><ul>${items}</ul>`);
}
