class PlusOne(object):
    """
    https://leetcode.com/problems/plus-one/
    Given a non-empty array of decimal digits representing a non-negative integer,
    increment one to the integer.

    Think of this problem as transforming a number into a list,
    e.g. 99 becomes [9, 9]
    if we add 1 to it, 99 + 1 = 100, and the returned list should be [1, 0, 0]

    example 1 - 1 digit with no carryovers
    input:  [0]
    output: [1]

    example 2 - 2 digits with no carryovers
    input:  [2, 2]
    output: [2, 3]

    example 3 - a lot of digits with no carryovers
    input:  [1, 2, 3, 4, 5, 6, 7, 8]
    output: [1, 2, 3, 4, 5, 6, 7, 9]

    example 4 - 1 carryover, with no added length
    input:  [1, 3, 9]
    output: [1, 4, 0]

    example 5 - multiple carryovers, with no added length
    input:  [1, 9, 9, 9, 9]
    output: [2, 0, 0, 0, 0]

    example 6 - multiple carryovers, with added length
    input:  [9, 9, 9]
    output: [1, 0, 0, 0]

    """

    def plusOne(self, digits: [int]) -> [int]:
        """
        just like adding an integer, we want to start adding 1 to the rightmost digit,
        then if there are carryovers, move left 1 digit at a time and repeat this process,
        until either there are no carryovers or the leftmost digit is reached.

        if the leftmost number is >= 10, then we add a 1 to the left of the list.
        Finally, returned the modified list.
        """
        carry = 1  # carry value should either be 0 or 1 for this function

        for i in reversed(range(len(digits))):  # start from the last int of the list
            digit_plus_1 = carry + digits[i]  # add 1 to the current digit

            # update the value of the current digit and the carry,
            # handling the cases when the current digit is >= 10
            digits[i], carry = digit_plus_1 % 10, digit_plus_1 // 10

            # if carry is 0, there's no need to continue the loop, just return the modified digits
            if carry == 0:
                return digits
        # to reach this point, carry has to be 1.
        # Return [1, <digits>] as a combined list
        return [carry] + digits
