import type { Api } from "../../server/api";

/** `gatekeep list`: every change and its verdict. */
export async function list(api: Api): Promise<string> {
	const lines: string[] = [];
	for (const change of await api.changes()) {
		const gate = await api.gate(change);
		lines.push(`${gate.verdict.padEnd(7)} ${change} @ ${gate.head}`);
	}
	return lines.join("\n");
}
