# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        reverse = string[::-1]

        if string == reverse:
            return True
        return False
