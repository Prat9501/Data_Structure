# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        literals = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in literals:
                top = stack.pop() if stack else 't'
                if literals[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
