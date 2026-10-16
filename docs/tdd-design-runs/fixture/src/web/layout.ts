import { escapeHtml } from "../core/format";

export function page(title: string, body: string): string {
	return `<!doctype html><title>${escapeHtml(title)}</title><main>${body}</main>`;
}
