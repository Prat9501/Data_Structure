# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [x if x == val else x for x in nums]
        count = 0
        while(count < len(nums)):
            if nums[count] == val:
                del nums[count]
            else:
                count += 1
        return len(nums)
