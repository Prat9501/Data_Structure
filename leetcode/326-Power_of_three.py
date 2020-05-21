# Example 1:
#
# Input: 27
# Output: true
# Example 2:
#
# Input: 0
# Output: false
# Example 3:
#
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 1:
            if (3 ** 20) % n == 0:
                return True
        return False
