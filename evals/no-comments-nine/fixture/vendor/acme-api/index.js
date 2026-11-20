export async function fetchOrderRef() {
  const res = await fetch("https://api.acme.example/v2/orders/latest");
  return res.json();
}
