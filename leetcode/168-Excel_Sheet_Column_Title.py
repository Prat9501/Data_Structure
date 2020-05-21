class Solution:
    def convertToTitle(self, n: int) -> str:
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        dic = {}
        for i, word in enumerate(string, 1):
            dic[i] = word
        while n:
            rem = n % 26
            n = n // 26
            if rem == 0:
                n += -1
            result += dic[rem] if rem != 0 else "Z"
        return result[::-1]
