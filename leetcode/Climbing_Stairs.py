# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution:
    def countWays(self, s):
        if s <= 1:
            return s
        return self.countWays(s-1) + self.countWays(s-2)


    def climbStairs(self, n: int) -> int:
        return self.countWays(n+1)

        # if n == 1:
        #     return 1
        # ways = [0] * (n + 1)
        # ways[1] = 1
        # ways[2] = 2
        # for i in range(3, n):
        #     ways[i] = ways[i-1] + ways[i-2]
        # return ways[n]
