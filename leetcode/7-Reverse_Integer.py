# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def check_bit(self, num):
        min_int = (-2 ** 31)
        max_int = ((2 ** 31) - 1)
        if min_int > num or num > max_int:
            return 0
        else:
            return num

    def reverse_digit(self, x):
        rev_digit = 0
        digit = [int(i) for i in str(x)]
        for i in range(len(digit)):
            rev_digit += digit[i] * (10 ** i)
        return rev_digit

    def reverse(self, x: int) -> int:
        if x > 0:
            x = self.check_bit(x)
            if x != 0:
                rev_digit = self.reverse_digit(x)
                rev_digit = self.check_bit(rev_digit)
                return rev_digit
            else:
                return 0
        else:
            x = self.check_bit(x)
            if x != 0:
                x = x * -1
                rev_digit = self.reverse_digit(x)
                rev_digit = self.check_bit(rev_digit)
                return rev_digit * -1
            else:
                return 0
