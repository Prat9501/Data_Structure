# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

#         pattern = []
#         string = ""
#         for i in haystack:
#             string += i
#             pattern.append(string)

#         if needle in pattern:
#             return pattern.index(needle)
#         return -1
