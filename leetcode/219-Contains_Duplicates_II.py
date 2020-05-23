class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        diff = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                diff = i - d[nums[i]]
                if diff <= k :
                    return True
                else :
                    d[nums[i]] = i
        return False
