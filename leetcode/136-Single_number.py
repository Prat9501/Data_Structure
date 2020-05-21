# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # duplicates = []
        # for num in nums:
        #     if num not in duplicates:
        #         duplicates.append(num)
        #     else:
        #         duplicates.remove(num)
        # return duplicates.pop()

        duplicates = {}
        for num in nums:
            if num in duplicates.keys():
                duplicates[num] += 1
            else:
                duplicates[num] = 1
        for key, value in duplicates.items():
            if value == 1:
                return key
