import unittest
from data_structure.array import *


class TestPlusOne(unittest.TestCase):
    def test_plusOne_one(self):
        output = PlusOne().plusOne([1, 2, 9])
        ans = [1, 3, 0]
        self.assertEqual(ans, output)

    def test_plusOne_all_carry_over(self):
        output = PlusOne().plusOne([9, 9, 9])
        ans = [1, 0, 0, 0]
        self.assertEqual(ans, output)

    def test_plusOne_two(self):
        output = PlusOne().plusOne([0])
        ans = [1]
        self.assertEqual(ans, output)


class TestAddBinary(unittest.TestCase):
    def test_addBinary_one(self):
        output = AddBinary().addBinary('11', '1')
        ans = "100"
        self.assertEqual(ans, output)

    def test_addBinary_two(self):
        output = AddBinary().addBinary('1010', '1011')
        ans = "10101"
        self.assertEqual(ans, output)


class TestShortestToChar(unittest.TestCase):
    def test_ShortestToChar(self):
        output = ShortestToChar().shortestToChar("loveleetcode", 'e')
        ans = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        self.assertEqual(ans, output)


class TestKidsWithCandies(unittest.TestCase):
    def test_kidsWithCandies_one(self):
        output = KidsWithCandies().kidsWithCandies([2, 3, 5, 1, 3], 3)
        ans = [True, True, True, False, True]
        self.assertEqual(ans, output)

    def test_kidsWithCandies_two(self):
        output = KidsWithCandies().kidsWithCandies([4, 2, 1, 1, 2], 1)
        ans = [True, False, False, False, False]
        self.assertEqual(ans, output)

    def test_kidsWithCandies_three(self):
        output = KidsWithCandies().kidsWithCandies([12, 1, 12], 10)
        ans = [True, False, True]
        self.assertEqual(ans, output)


class TestMinSubArrayLen(unittest.TestCase):
    def test_minSubArrayLen(self):
        output = MinSubArrayLen().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
        ans = 2
        self.assertEqual(ans, output)


class TestMaxChunksToSorted(unittest.TestCase):
    def test_maxChunksToSorted_one(self):
        output = MaxChunksToSorted().maxChunksToSorted([5, 4, 3, 2, 1])
        ans = 1
        self.assertEqual(ans, output)

    def test_maxChunksToSorted_two(self):
        output = MaxChunksToSorted().maxChunksToSorted([2, 1, 3, 4, 4])
        ans = 4
        self.assertEqual(ans, output)

