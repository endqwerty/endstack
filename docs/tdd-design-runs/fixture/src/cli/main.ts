import type { Api } from "../server/api";
import { failures } from "./commands/failures";
import { flaky } from "./commands/flaky";
import { history } from "./commands/history";
import { list } from "./commands/list";
import { show } from "./commands/show";
import { slowest } from "./commands/slowest";

export async function main(api: Api, argv: string[]): Promise<string> {
	const [command, ...args] = argv;
	switch (command) {
		case "list":
			return list(api);
		case "show":
			return show(api, args[0]);
		case "history":
			return history(api, args[0]);
		case "failures":
			return failures(api, Number(args[0]));
		case "flaky":
			return flaky(api, args[0]);
		case "slowest":
			return slowest(api, Number(args[0]), args[1] ? Number(args[1]) : undefined);
		default:
			return "usage: gatekeep list|show|history|failures|flaky|slowest";
	}
}
