class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord("A") - 1
        ret = 0
        for ch in s:
            ret *= 26
            ret += (ord(ch) - base)

        return ret
