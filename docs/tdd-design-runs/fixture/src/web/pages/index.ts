import { escapeHtml } from "../../core/format";
import type { Call } from "../../server/ops";
import { page } from "../layout";

/** / — every change with its verdict. */
export async function indexPage(call: Call): Promise<string> {
	const rows: string[] = [];
	for (const change of await call("changes", {})) {
		const g = await call("gate", { change });
		rows.push(`<tr><td><a href="/changes/${escapeHtml(change)}">${escapeHtml(change)}</a></td><td>${g.verdict}</td></tr>`);
	}
	return page("gatekeep", `<table>${rows.join("")}</table>`);
}
