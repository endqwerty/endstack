import importlib.util
import sys
import unittest
from pathlib import Path

source = Path(sys.argv.pop(1)).resolve()
spec = importlib.util.spec_from_file_location('quota_under_test', source)
quota = importlib.util.module_from_spec(spec)
spec.loader.exec_module(quota)

class Contract(unittest.TestCase):
    def test_exact_limit_is_allowed(self):
        self.assertTrue(quota.can_reserve(7, 3, 10))

    def test_import_above_limit_is_rejected(self):
        with self.assertRaises(ValueError):
            quota.restore({'used': 11}, 10)

unittest.main(verbosity=2)
