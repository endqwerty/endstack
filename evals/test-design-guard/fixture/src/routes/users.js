import { route } from "../router.js";

route("GET", "/admin/users", () => ["ana", "bo"], { permission: "users:read" });
route("DELETE", "/admin/users", () => "deleted", { permission: "users:write" });
