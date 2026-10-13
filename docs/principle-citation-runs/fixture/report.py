"""Plain-text report over a queue."""


def render(queue):
    lines = []
    for job in queue.jobs:
        label = job.status()
        if label == "failed":
            label = "failed: " + job.error.strip()
        lines.append(f"{job.name}: {label} (attempt {job.attempts})")
    return "\n".join(lines)
