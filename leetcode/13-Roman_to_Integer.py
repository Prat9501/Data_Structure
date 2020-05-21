# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        while s:
            if len(s) == 1 or dic[s[0]] >= dic[s[1]]:
                total += dic[s[0]]
                s = s[1:]
            else:
                total += dic[s[1]] - dic[s[0]]
                s = s[2:]
        return total
