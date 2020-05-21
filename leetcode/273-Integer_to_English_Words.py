class Solution:
    def numberToWords(self, num: int) -> str:
        word = []
        dic = {
            10 ** 9: "Billion", 10 ** 6: "Million", 10 ** 3: "Thousand", 10 ** 2: "Hundred", 90: "Ninety", 80: "Eighty", 70: "Seventy", 60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty", 20: "Twenty", 19: "Nineteen", 18: "Eighteen", 17: "Seventeen", 16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen", 12: "Twelve", 11: "Eleven", 10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One"
        }
        two_digits = [90, 80, 70, 60, 50, 40, 30, 20]
        if num == 0:
            return "Zero"
        if num <= 20:
            return dic[num]
        else:
            for val in dic.keys():
                q = (num // val)
                # while q < 10:
                if q > 0:
                    word.append(q)
                    word.append(dic[val])
                    num = num % val
        for i in range(0, len(word), 2):
            sub = ""
            if 1 < word[i] <= 20:
                sub += dic[word[i]]
            if word[i] == 1 and word[i+1] in ["Billion", "Million", "Thousand", "Hundred"]:
                sub += dic[1]
            else:
                sub += ""
            if word[0] == 1:
                sub += dic[1]
            if word[i] > 99:
                q2 = word[i] // 100
                sub += dic[q2]
                sub += " " + dic[100]
                q2 = word[i] % 100
                if q2 < 20 and q2 != 0:
                    sub += " " + dic[q2]
                else:
                    for j in two_digits:
                        d = (q2 // j)
                        if d < 9 and d != 0:
                            sub += " " + dic[j]
                            rem = q2%j
                            if rem != 0:
                                sub += " " + dic[rem]
                            break
            if 20 < word[i] <= 99 :
                for j in two_digits:
                    if (word[i] // j) < 9 and (word[i] // j) != 0:
                        sub += dic[j]
                        rem = word[i] % j
                        if rem != 0:
                            sub += " " + dic[rem]
                        break
            word[i] = sub
        if word[1] not in ["Billion", "Million", "Thousand", "Hundred"]:
            word[0] = ""
        word = [i for i in word if i]
        word = ["One" if x == "OneOne" else x for x in word]

        res = ' '.join([row for row in word]).lstrip()
        return res
