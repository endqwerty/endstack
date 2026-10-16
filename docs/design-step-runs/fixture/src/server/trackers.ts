import type { Issue, TrackerReceipt } from "../core/tracker";

export type Tracker = { create(test: string): Promise<Issue> };

export class Requests {
	private receipts = new Map<number, TrackerReceipt>();
	private next = 1;
	constructor(private tracker: Tracker) {}

	request(test: string): TrackerReceipt {
		const receipt: TrackerReceipt = { id: this.next++, test, state: "queued", issue: null, error: null };
		this.receipts.set(receipt.id, receipt);
		return receipt;
	}

	get(id: number): TrackerReceipt | undefined {
		return this.receipts.get(id);
	}

	/** Send every queued request. */
	async deliver(): Promise<void> {
		for (const receipt of this.receipts.values()) {
			if (receipt.state !== "queued") continue;
			receipt.state = "sending";
			try {
				receipt.issue = await this.tracker.create(receipt.test);
				receipt.state = "complete";
			} catch (e) {
				receipt.error = String(e);
				receipt.state = "failed";
			}
		}
	}
}
