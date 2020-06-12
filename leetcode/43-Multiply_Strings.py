class Solution:
    def multiply(self, num1, num2):
        # mult = num1 + "*" + num2
        # ans = eval(mult)
        # return str(ans)

        l, r = [], []
        result = []
        for i in range(len(num2)):
            mult = int(num2[i]) * pow(10,len(num2)-1-i)
            r.append(mult)
        for i in range(len(num1)):
            mult = int(num1[i]) * pow(10,len(num1)-1-i)
            l.append(mult)
        
        for i in l:
            for j in r:
                result.append(i*j)
        
        return str(sum(result))