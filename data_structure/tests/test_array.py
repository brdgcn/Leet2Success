import unittest
from data_structure.array import PlusOne


class TestPlusOne(unittest.TestCase):
    """
    test the plusOne() method
    """

    def test_one_digit_no_carryover(self):
        output = PlusOne().plusOne([0])
        expected_output = [1]
        self.assertEqual(output, expected_output)

    def test_two_digits_no_carryover(self):
        output = PlusOne().plusOne([2, 2])
        expected_output = [2, 3]
        self.assertEqual(output, expected_output)

    def test_many_digits_no_carryover(self):
        output = PlusOne().plusOne([1, 2, 3, 4, 5, 6, 7, 8])
        expected_output = [1, 2, 3, 4, 5, 6, 7, 9]
        self.assertEqual(output, expected_output)

    def test_1_carryover_with_no_added_length(self):
        output = PlusOne().plusOne([1, 3, 9])
        expected_output = [1, 4, 0]
        self.assertEqual(output, expected_output)

    def test_multiple_carryovers_with_no_added_length(self):
        output = PlusOne().plusOne([1, 9, 9, 9, 9])
        expected_output = [2, 0, 0, 0, 0]
        self.assertEqual(output, expected_output)

    def test_multiple_carryovers_with_added_length(self):
        output = PlusOne().plusOne([9, 9, 9])
        expected_output = [1, 0, 0, 0]
        self.assertEqual(output, expected_output)
