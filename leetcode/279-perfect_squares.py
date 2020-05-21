"""
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import math
class Solution:
	def numSquares(self, n):
		res = n
		for i in range(1, int(math.floor(n ** 0.5)) + 1):
			tmp = i ** 2
			if tmp > n:
				break
			else:
				res = min(res, 1 + self.numSquares(n - tmp))

		return res

		
obj = Solution()
print(obj.numSquares(13))