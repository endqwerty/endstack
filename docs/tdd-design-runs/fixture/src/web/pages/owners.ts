import { escapeHtml } from "../../core/format";
import type { Call } from "../../server/ops";
import { page } from "../layout";

/** /owners — which team owns which test prefix. */
export async function ownersPage(call: Call): Promise<string> {
	const owners = await call("owners", {});
	const rows = Object.entries(owners).map(([p, t]) => `<tr><td>${escapeHtml(p)}</td><td>${escapeHtml(t)}</td></tr>`);
	return page("owners", `<table>${rows.join("")}</table>`);
}
