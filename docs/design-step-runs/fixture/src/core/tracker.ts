export type Issue = { key: string; url: string };

/** A request to file an issue for a failing test, and what became of it. */
export type TrackerReceipt = {
	id: number;
	test: string;
	state: "queued" | "sending" | "complete" | "failed";
	issue: Issue | null;
	error: string | null;
};

export function describe(receipt: TrackerReceipt): string {
	switch (receipt.state) {
		case "queued":
			return `${receipt.test}: waiting to be filed`;
		case "sending":
			return `${receipt.test}: filing`;
		case "complete":
			return `${receipt.test}: filed as ${receipt.issue?.key}`;
		case "failed":
			return `${receipt.test}: could not be filed (${receipt.error})`;
	}
}
