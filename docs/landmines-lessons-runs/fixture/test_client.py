import io
import json
import unittest

from client import fetch_invoice


def opener(payload):
    return lambda url: io.BytesIO(json.dumps(payload).encode())


class ClientTest(unittest.TestCase):
    def test_returns_invoice(self):
        self.assertEqual(fetch_invoice("http://b", 1, opener({"id": 1})), {"id": 1})
