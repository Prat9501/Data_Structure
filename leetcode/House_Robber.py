# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

class Solution:
    def rob(self, nums: List[int]) -> int:
        amount = 0
        if len(nums) == 0:
            return 0
        val_1 = nums[0]
        if len(nums) == 1:
            return val_1
        val_2 = max(nums[0], nums[1])
        if len(nums) == 2:
            return val_2
        for i in range(2, len(nums)):
            amount = max(nums[i] + val_1, val_2)
            val_1 = val_2
            val_2 = amount
        return amount

        # total = 0
        # if len(nums) > 2:
        #     for i in range(0, len(nums), 2):
        #         total += nums[i]
        #     return total
        # elif len(nums) == 0:
        #     return 0
        # else:
        #     return max(nums)

#         odd_total, even_total = 0, 0
#         if len(nums) == 0:
#             return 0
#         else:
#             for i in range(0, len(nums), 2):
#                 odd_total += nums[i]
#             for i in range(1, len(nums), 2):
#                 even_total += nums[i]

#         if odd_total > even_total:
#             return odd_total
#         return even_total
