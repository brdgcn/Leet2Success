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


class TestAddBinary(unittest.TestCase):
    """Given two binary strings a and b, return their sum as a binary string"""
    def test_addBinary_one(self):
        output = AddBinary().addBinary("11", "1")
        ans = "100"
        self.assertEqual(ans, output)

    def test_addBinary_two(self):
        output = AddBinary().addBinary("1010", "1011")
        ans = "10101"
        self.assertEqual(ans, output)


class TestShortestToChar(unittest.TestCase):
    """given a string and a char, return an array of integers representing the shortest distance
        from the char in the string"""
    def test_ShortestToChar(self):
        output = ShortestToChar().shortestToChar("loveleetcode", "e")
        ans = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        self.assertEqual(ans, output)


class TestKidsWithCandies(unittest.TestCase):
    """for each item in a given array candies, if the sum of (item + extraCandies) >= to the greatest
    number in the array, return True in the output array, otherwise return False """
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
    """Given an array of positive integers and a positive integer s, find the minimal length of a
        contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead"""
    def test_minSubArrayLen(self):
        output = MinSubArrayLen().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
        ans = 2
        self.assertEqual(ans, output)


class TestMaxChunksToSorted(unittest.TestCase):
    """split a given array into a maximum number of "chunks" (partitions), and individually sort each chunk.
        After concatenating them, the result equals the sorted array, output the maximum number of chucks"""
    def test_maxChunksToSorted_one(self):
        output = MaxChunksToSorted().maxChunksToSorted([5, 4, 3, 2, 1])
        ans = 1
        self.assertEqual(ans, output)

    def test_maxChunksToSorted_two(self):
        output = MaxChunksToSorted().maxChunksToSorted([2, 1, 3, 4, 4])
        ans = 4
        self.assertEqual(ans, output)


class TestLargestRectangleArea(unittest.TestCase):
    """
    Given an array of non-negative integers representing the histogram's bar height where the width of each bar
    is 1, find the area of largest rectangle in the histogram.
    """
    def test_largestRectangleArea_one(self):
        output = LargestRectangleArea().largestRectangleArea([2, 1, 5, 6, 2, 3])
        ans = 10
        self.assertEqual(ans, output)

    def test_largestRectangleArea_two(self):
        output = LargestRectangleArea().largestRectangleArea([2, 4])
        ans = 4
        self.assertEqual(ans, output)
