import type { Task } from "../shared/task.ts";

export function listLines(tasks: Task[]): string[] {
  return tasks.filter((t) => !t.done && !t.deletedAt).map((t) => `[ ] ${t.id}  ${t.title}`);
}
