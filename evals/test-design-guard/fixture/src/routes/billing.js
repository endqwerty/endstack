import { route } from "../router.js";

route("GET", "/admin/invoices", () => ["inv-1"], { permission: "billing:read" });
route("POST", "/admin/refunds", () => "refunded");
