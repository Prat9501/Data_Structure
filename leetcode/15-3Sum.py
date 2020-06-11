from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # nums = list(set(nums))
        pairs = combinations(nums, 3)
        for pair in pairs:
            pair = sorted(pair)
            if sum(pair) == 0 and pair not in result:
                result.append(pair)
        return result

# 270/313 test cases passed
