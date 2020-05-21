# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for char in s:
            if char in letters.keys():
                letters[char] += 1
            else:
                letters[char] = 1

        for post, char in enumerate(s):
            if letters[char] == 1:
                return post
        return -1
                
