import type { Api } from "../server/api";

/** The change page: the gate's verdict, then the results behind it. */
export async function changePage(api: Api, change: string): Promise<string> {
	const gate = await api.gate(change);
	const results = await api.results(change);
	const rows = results.map((r) => `<li class="${r.outcome}">${r.test}</li>`).join("");
	return `<h1>${change} @ ${gate.head}: ${gate.verdict}</h1><ul>${rows}</ul>`;
}
