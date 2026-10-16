import type { Call } from "../../server/ops";

export type CommitStatus = { sha: string; state: "success" | "failure" | "pending"; description: string };

/** The commit status reported to the forge for a change's latest head. */
export async function commitStatus(call: Call, change: string): Promise<CommitStatus> {
	const g = await call("gate", { change });
	const state = g.verdict === "pass" ? "success" : g.verdict === "fail" ? "failure" : "pending";
	return { sha: g.head, state, description: `gatekeep: ${g.verdict}` };
}
