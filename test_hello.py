import unittest
from unittest.runner import TextTestResult

class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func('こんにちは'))
