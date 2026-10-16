import { api } from "../src/server/api";
import { caller } from "../src/server/ops";
import { Store } from "../src/server/store";

export function setup() {
	const store = new Store();
	const call = caller(store);
	return { store, call, api: api(call) };
}
