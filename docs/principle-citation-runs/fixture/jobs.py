"""A tiny in-memory job queue."""


class Job:
    def __init__(self, name, max_attempts=3):
        self.name = name
        self.max_attempts = max_attempts
        self.attempts = 0
        self.started = False
        self.done = False
        self.failed = False
        self.error = None

    def start(self):
        if self.done:
            raise ValueError("job already finished")
        if self.started and not self.failed:
            raise ValueError("job already running")
        self.started = True
        self.failed = False
        self.attempts += 1

    def complete(self):
        if not self.started or self.failed:
            raise ValueError("job is not running")
        self.done = True

    def fail(self, error):
        if not self.started or self.done:
            raise ValueError("job is not running")
        self.failed = True
        self.error = error

    def can_retry(self):
        return self.failed and self.attempts < self.max_attempts

    def status(self):
        if self.done:
            return "done"
        if self.failed:
            return "failed"
        if self.started:
            return "running"
        return "queued"


class Queue:
    def __init__(self):
        self.jobs = []

    def add(self, job):
        self.jobs.append(job)

    def next_job(self):
        for job in self.jobs:
            if job.status() == "queued" or job.can_retry():
                return job
        return None

    def expire(self, job):
        """Give up on a job that ran too long."""
        job.failed = True

    def drain(self):
        """Fail every unfinished job, for example at shutdown."""
        for job in self.jobs:
            if not job.done:
                job.failed = True

    def summary(self):
        counts = {"queued": 0, "running": 0, "failed": 0, "done": 0}
        for job in self.jobs:
            counts[job.status()] += 1
        return counts
