# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        if len(nums) == 0:
            return False
        for num in nums:
            if not numbers.get(num):
                numbers[num] = True
            else:
                return True
        return False

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
