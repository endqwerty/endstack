import unittest

from jobs import Job, Queue
from report import render


class JobTests(unittest.TestCase):
    def test_lifecycle(self):
        job = Job("a")
        self.assertEqual(job.status(), "queued")
        job.start()
        self.assertEqual(job.status(), "running")
        job.complete()
        self.assertEqual(job.status(), "done")

    def test_retry_after_failure(self):
        job = Job("a", max_attempts=2)
        job.start()
        job.fail("boom")
        self.assertTrue(job.can_retry())
        job.start()
        self.assertEqual(job.attempts, 2)
        job.fail("boom")
        self.assertFalse(job.can_retry())

    def test_queue_picks_queued_then_retryable(self):
        queue = Queue()
        a, b = Job("a"), Job("b")
        queue.add(a)
        queue.add(b)
        a.start()
        self.assertIs(queue.next_job(), b)
        a.fail("boom")
        self.assertIs(queue.next_job(), a)

    def test_expire_and_drain(self):
        queue = Queue()
        a, b = Job("a"), Job("b")
        queue.add(a)
        queue.add(b)
        a.start()
        queue.expire(a)
        self.assertEqual(a.status(), "failed")
        queue.drain()
        self.assertEqual(queue.summary()["failed"], 2)

    def test_report(self):
        queue = Queue()
        job = Job("a")
        queue.add(job)
        job.start()
        job.fail(" boom ")
        self.assertEqual(render(queue), "a: failed: boom (attempt 1)")


if __name__ == "__main__":
    unittest.main()
