class PlusOne(object):
    # instance method
    def plusOne(self, digits):
        carry = 1
        len_digits = len(digits)
        for i in reversed(range(len_digits)):
            digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
        return [carry] + digits if carry else digits


class AddBinary(object):
    def addBinary(self, a, b):
        # shortcut solution: return bin(int(a, 2) + int(b, 2))[2:]
        string, carry = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):  # zip
            total = int(i) + int(j) + carry
            string = str(total % 2) + string
            carry = total // 2
            print(total, carry, string)
        return '1' + string if carry else string


class ShortestToChar(object):
    def shortestToChar(self, string, char):
        charGPS = []
        res = []
        len_string = len(string)
        charGPS = [i for i in (range(len_string)) if string[i] == char]
        for i in range(len_string):
            if string[i] == char:
                charGPS.append(i)
        for string_index in range(len_string):
            min_distance = float('inf')
            for char_index in charGPS:
                min_distance = min(min_distance, abs(char_index - string_index))
            res.append(min_distance)
        return res


class KidsWithCandies(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        great = 0
        for i in candies:
            great = max(i, great)
        for i in candies:
            if i + extraCandies >= great:
                res.append(True)
            else:
                res.append(False)
        return res


class MinSubArrayLen(object):
    def minSubArrayLen(self, s, nums):
        l = total = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                res = min(res, i - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == len(nums) + 1 else res


class MaxChunksToSorted(object):
    def maxChunksToSorted(self, arr):
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]: stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        return len(stack)
