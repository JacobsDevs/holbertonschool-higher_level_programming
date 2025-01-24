"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(max_integer([1,2,3]), 3)

    def test_basic_middle(self):
        self.assertEqual(max_integer([1,3,2]), 3)

    def test_basic_reversed(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_two_max_values(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
    
    def test_one_value(self):
        self.assertEqual(max_integer([1]), 1)

    def test_no_values(self):
        self.assertEqual(max_integer(), None)

if __name__ == "__main__":
    unittest.main()
