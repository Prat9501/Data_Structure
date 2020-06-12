class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        res = []
        
        def comb_sum2(target, index):
            if target == 0:
                result.append(res[:])
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > target or (index < i and candidates[i] == candidates[i-1]):
                    continue
                res.append(candidates[i])
                comb_sum2(target - candidates[i], i+1)
                res.pop()
        comb_sum2(target, 0)
        return result