class Solution:
    def letterCombinations(self, digits):
        d = {'2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']}
        
        def join_pairs(comb, next_dig):
            if len(next_dig) == 0:
                res.append(comb)
            else:
                for letter in d[next_dig[0]]:
                    join_pairs(comb+letter, next_dig[1:])
        
        res = []
        if digits:
            join_pairs("", digits)
        return res
