# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        max_div = int(n ** 0.5)
        for i in range(2, 1 + max_div):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            if self.is_prime(i):
                count += 1
        return count
