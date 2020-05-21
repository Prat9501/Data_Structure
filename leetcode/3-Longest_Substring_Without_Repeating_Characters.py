class Solution:
    def lengthOfLongestSubstring(self, s):
        dict = {}
        maxlength = start = 0
        for i, val in enumerate(s):
            if val in dict:
                su = dict[val] + 1
                if su > start:
                    start = su
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dict[val] = i
        return maxlength
