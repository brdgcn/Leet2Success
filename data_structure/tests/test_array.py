import unittest
from data_structure.array import *


class TestPlusOne(unittest.TestCase):
    def test_plusOne_one(self):
        output = PlusOne().plusOne([1, 2, 9])
        ans = [1, 3, 0]
        self.assertEqual(ans, output)

    def test_plusOne_all_carry_over(self):
        output = PlusOne().plusOne([9, 9])
        ans = [1, 0, 0]
        self.assertEqual(ans, output)

    def test_plusOne_two(self):
        output = PlusOne().plusOne([0])
        ans = [1]
        self.assertEqual(ans, output)
