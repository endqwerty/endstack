import { escapeHtml } from "../../core/format";
import type { Call } from "../../server/ops";
import { page } from "../layout";

/** /runs/:id — the results of one run. */
export async function runPage(call: Call, id: number): Promise<string> {
	const rows = await call("runResults", { run: id });
	return page(`run ${id}`, `<ul>${rows.map((r) => `<li class="${r.outcome}">${escapeHtml(r.test)}</li>`).join("")}</ul>`);
}
