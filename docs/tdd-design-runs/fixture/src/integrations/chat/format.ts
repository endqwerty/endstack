/** Chat markup: bold and a bullet list. */
export function bold(text: string): string {
	return `*${text.replace(/\*/g, "")}*`;
}

export function bullets(items: string[]): string {
	return items.map((i) => `• ${i}`).join("\n");
}
