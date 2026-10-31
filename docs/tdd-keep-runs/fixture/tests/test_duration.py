import unittest

from shiplog.duration import parse_duration


class ParseDurationTest(unittest.TestCase):
    def test_single_unit(self):
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)

    def test_rejects_garbage(self):
        with self.assertRaises(ValueError):
            parse_duration("soon")
