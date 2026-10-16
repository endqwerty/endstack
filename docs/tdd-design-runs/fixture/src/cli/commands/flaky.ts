import { flakyTests } from "../../core/flaky";
import type { Api } from "../../server/api";

/** `gatekeep flaky <change>`: tests that both passed and failed on one head. */
export async function flaky(api: Api, change: string): Promise<string> {
	const names = flakyTests(await api.history(change));
	return names.length ? names.join("\n") : "no flaky tests";
}
