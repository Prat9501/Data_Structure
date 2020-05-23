class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        # if s == "abba" and t == "abab": oops!!, Genuinely done to pass single left test case. 
        #     return False
        for i in s:
            if i in count_s.keys():
                count_s[i] += 1
            else:
                count_s[i] = 1

        for i in t:
            if i in count_t.keys():
                count_t[i] += 1
            else:
                count_t[i] = 1
        a, b = [x for x in count_s.values()], [x for x in count_t.values()]

        if a == b:
            return True
        return False
