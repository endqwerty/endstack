import type { Task } from "../shared/task.ts";

export function renderTaskList(tasks: Task[]): string {
  const items = tasks
    .filter((t) => !t.done && !t.deletedAt)
    .map((t) => `<li data-id="${t.id}">${t.title}</li>`)
    .join("");
  return `<ul class="tasks">${items}</ul>`;
}
