class PlusOne(object):
    """increment one to a given non-empty array, e.g. [9,9] => [1,0,0] """
    def plusOne(self, digits: [int]) -> [int]:
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
        return [carry] + digits if carry else digits


class AddBinary(object):
    """
        Returns the sum of two decimal numbers in binary digits.

                Parameters:
                        a (int): A decimal integer
                        b (int): Another decimal integer

                Returns:
                        binary_sum (str): Binary string of the sum of a and b
    """
    def addBinary(self, a, b):
        # shortcut solution: return bin(int(a, 2) + int(b, 2))[2:]
        result, carry = "", 0
        d = len(b) - len(a)
        a = "0" * d + a
        b = "0" * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            total = int(i) + int(j) + carry
            result = str(total % 2) + result
            carry = total // 2
            print(total, carry, result)
        return "1" + result if carry else result


class ShortestToChar(object):
    """given a string and a char, return an array of integers representing the shortest distance
    from the char in the string"""
    def shortestToChar(self, string: str, char: str) -> [int]:
        res = []
        char_index = [i for i in (range(len(string))) if string[i] == char]
        for string_index in range(len_string):
            min_distance = float("inf")
            for each_char in char_index:
                min_distance = min(min_distance, abs(each_char - string_index))
            res.append(min_distance)
        return res


class KidsWithCandies(object):
    """for each item in a given array candies, if the sum of (item + extraCandies) >= to the greatest
    number in the array, return True in the output array, otherwise return False """
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        maxCandies = 0
        for i in candies:
            maxCandies = max(i, maxCandies)
        for i in candies:
            if i + extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        return res


class MinSubArrayLen(object):
    """Given an array of positive integers and a positive integer s, find the minimal length of a
    contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead"""
    def minSubArrayLen(self, s, nums):
        left_pointer = sums = 0
        min_len = len(nums) + 1
        len_nums = len(nums)
        for i in range(len_nums):
            sums += nums[i]  # add each element
            while sums >= s:
                min_len = min(
                    min_len, i - left_pointer + 1
                )  # total current index length e.g. 3-0+1
                sums -= nums[left_pointer]  # deduct left most value
                left_pointer += 1  # move left window to right
        return 0 if min_len == len(nums) + 1 else min_len


class MaxChunksToSorted(object):
    """split a given array into a maximum number of "chunks" (partitions), and individually sort each chunk.
    After concatenating them, the result equals the sorted array, output the maximum number of chucks"""
    def maxChunksToSorted(self, arr):
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        return len(stack)


class LargestRectangleArea(object):
    """
    Given an array of non-negative integers representing the histogram's bar height where the width of each bar
    is 1, find the area of largest rectangle in the histogram.
    """
    def largestRectangleArea(self, heights):
        stack = []
        heights = [0] + heights + [0]
        result = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return result






