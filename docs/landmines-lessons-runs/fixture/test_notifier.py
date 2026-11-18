import time
import unittest

from notifier import Notifier


class NotifierTest(unittest.TestCase):
    def test_send_delivers_stripped_message(self):
        got = []
        Notifier(got.append).send("  hi  ")
        deadline = time.time() + 0.05
        while not got and time.time() < deadline:
            time.sleep(0.005)
        self.assertEqual(got, ["hi"])
