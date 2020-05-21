# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict.keys():
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict.keys():
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        if s_dict == t_dict:
            return True
        else:
            return False
