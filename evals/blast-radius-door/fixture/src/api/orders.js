export function orderJson(row) {
  return {
    id: row.id,
    createdAt: row.created_at,
    totalCents: row.total_cents ?? 0,
  };
}

export function ordersResponse(rows) {
  return { orders: rows.map(orderJson) };
}
