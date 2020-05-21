# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        word = strs[0]
        for i in range(1, len(strs)):
            string = ""
            if len(word) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(word) and word[j] == strs[i][j]:
                    string += word[j]
                else:
                    break
            word = string
        return word
