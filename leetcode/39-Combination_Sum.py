class Solution:
    def combinationSum(self, candidates, target):
        def comb_sum(remain, path, start):
            if remain < 0:
                return
            if remain == 0:
                paths.append(path[:])
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                comb_sum(remain - candidates[i], path, i)
                path.pop()
        
        paths = []
        comb_sum(target, [], 0)
        return paths
