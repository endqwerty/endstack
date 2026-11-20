export type Order = { id: string; cents: number };

let warm = false;

export function warmCache(): void {
  warm = true;
}

export function start(): void {
  if (!warm) console.warn("starting cold");
}

export function onResize(): void {}
