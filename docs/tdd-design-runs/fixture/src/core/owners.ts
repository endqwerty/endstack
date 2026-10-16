/** Map a test name to its owning team by the longest matching prefix. */
export function ownerOf(test: string, owners: Record<string, string>): string | null {
	let best: string | null = null;
	for (const prefix of Object.keys(owners)) if (test.startsWith(prefix) && (!best || prefix.length > best.length)) best = prefix;
	return best ? owners[best] : null;
}
