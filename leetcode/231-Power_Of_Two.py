class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >= 1:
            if (2 ** 30) % n == 0:
                return True
        return False
