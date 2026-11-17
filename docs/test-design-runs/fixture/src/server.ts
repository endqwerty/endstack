import { total, type Item, type Coupon } from "./cart.ts";

export function start(port = 0) {
  return Bun.serve({
    port,
    async fetch(req) {
      const url = new URL(req.url);
      if (req.method === "POST" && url.pathname === "/checkout") {
        const body = (await req.json()) as { items: Item[]; coupon?: Coupon };
        return Response.json({ totalCents: total(body.items, body.coupon) });
      }
      return new Response("not found", { status: 404 });
    },
  });
}
