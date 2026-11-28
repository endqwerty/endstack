import { route } from "../router.js";

route("GET", "/admin/flags", () => ({ beta: true }), { permission: "flags:read" });
route("PUT", "/admin/flags", () => "saved");
