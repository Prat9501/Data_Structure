def intToRoman(num):
    roman = ""
    dic = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50:'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    for val in dic.keys():
        q = num // val
        if q > 0:
            roman += q * dic[val]
            num = num % val
    print(roman)

intToRoman(3)
