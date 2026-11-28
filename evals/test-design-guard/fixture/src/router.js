export const routes = [];

export function route(method, path, handler, options = {}) {
  routes.push({ method, path, handler, permission: options.permission });
}

export function handle(method, path, user) {
  const found = routes.find((r) => r.method === method && r.path === path);
  if (!found) return { status: 404 };
  if (found.permission && !user.permissions.includes(found.permission)) return { status: 403 };
  return { status: 200, body: found.handler(user) };
}
