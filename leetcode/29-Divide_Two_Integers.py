class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:return 2147483647
        sign = 1
        if dividend<0:
            sign *= -1
            dividend *= -1 
        if divisor < 0:
            sign *= -1
            divisor *= -1 
        loop = 0
        while(dividend >= divisor):
            c = 1
            a = 0
            num = divisor
            prev = 0
            while num < dividend:
                a = c
                c += c
                prev = num
                num += num
            if num == dividend:
                if sign > 0:
                    return c + loop
                else:
                    return -c - loop
            dividend -= prev
            loop += a
        if sign > 0:
            return loop
        else:
            return -loop