from itertools import combinations
class Solution:
    def fourSum(self, nums, target):
        result = []
        pairs = combinations(nums, 4)
        for pair in pairs:
            pair = sorted(pair)
            if sum(pair) == target and pair not in result:
                result.append(pair)
        return result

# 240/282 test cases passed 