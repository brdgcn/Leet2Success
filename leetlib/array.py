def plusOne(digits):
    carry = 1
    len_digits = len(digits)
    for i in reversed(range(len_digits)):
        digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
    return [carry] + digits if carry else digits


def addBinary(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        a = '0' * (len_b - len_a) + a
    else:
        b = '0' * (len_a - len_b) + b
    res, carry, val = '', 0, 0
    for i in reversed(range(max(len_a, len_b))):
        val = carry  # 0
        if i < len_a:
            val += int(a[i])
            val += int(b[i])
        carry, val = val // 2, val % 2
    if carry:
        res += str(1)
    return res[::-1]


def shortestToChar(S, C):
    prev = float('-inf')
    ans = []
    for i, x in enumerate(S):
        if x == C: prev = i
        ans.append(i - prev)

    prev = float('inf')
    for i in xrange(len(S) - 1, -1, -1):
        if S[i] == C: prev = i
        ans[i] = min(ans[i], prev - i)
    return ans


def kidsWithCandies(candies, extraCandies):
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


def minSubArrayLen(nums, s):
    l = total = 0
    res = len(nums) + 1
    for i in range(len(nums)):
        total += nums[i]
        while total >= s:
            res = min(res, i - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == len(nums) + 1 else res


def maxChunksToSorted(arr):
    stack = []
    for num in arr:
        if stack and num < stack[-1]:
            head = stack.pop()
            while stack and num < stack[-1]: stack.pop()
            stack.append(head)
        else: stack.append(num)
    return len(stack)