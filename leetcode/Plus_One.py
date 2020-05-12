# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # last_digit = digits[-1]
        # add_digit = last_digit + 1
        # digits.pop()
        # if add_digit > 9:
        #     digits.append(1)
        #     digits.append(0)
        #     digits = [1 if i==9 else i for i in digits]
        # else:
        #     digits.append(add_digit)
        # return digits

        n = len(digits)
        digit = 0
        for i in range(n):
            digit += digits[i] * (10 ** (n-i-1))
        digit = digit + 1
        return [int(x) for x in str(digit)]
