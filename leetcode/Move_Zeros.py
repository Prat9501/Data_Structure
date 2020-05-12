# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        for i in range(zero_count):
            nums.remove(0)
            nums.append(0)
