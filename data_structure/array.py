class PlusOne(object):
    """
    increment one to a given non-empty array.
    https://leetcode.com/problems/plus-one/
    
    example 1
    input: [0]
    output: [1] 

    example 2
    input: [4]
    output: [5] 

    example 3
    input: [9,9]
    output: [1,0,0] 
    """
    def plusOne(self, digits: [int]) -> [int]:
        """
        start from the rightmost integer
        
        """
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] = (carry + digits[i]) % 10
            carry = (carry + digits[i]) // 10
        return [carry] + digits if carry else digits
