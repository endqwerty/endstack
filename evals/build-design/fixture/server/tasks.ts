import type { Task } from "../shared/task.ts";

export type TaskPatch = { title?: string; done?: boolean; deleted?: boolean };

export class TaskStore {
  private tasks = new Map<string, Task>();

  create(id: string, title: string): Task {
    const task: Task = { id, title, done: false, deletedAt: null };
    this.tasks.set(id, task);
    return task;
  }

  list(): Task[] {
    return [...this.tasks.values()];
  }

  // PATCH /tasks/:id
  patch(id: string, patch: TaskPatch, now: Date = new Date()): Task {
    const task = this.tasks.get(id);
    if (!task) throw new Error(`no task ${id}`);
    const next: Task = { ...task };
    if (patch.title !== undefined) next.title = patch.title;
    if (patch.done !== undefined) next.done = patch.done;
    if (patch.deleted !== undefined) next.deletedAt = patch.deleted ? (task.deletedAt ?? now) : null;
    this.tasks.set(id, next);
    return next;
  }
}
