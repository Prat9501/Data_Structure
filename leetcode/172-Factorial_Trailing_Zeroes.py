def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def trailingZeroes(n):
    count = 0
    num = str(factorial(n))
    for j in range(len(num)-1, 0, -1):
        # import pdb; pdb.set_trace()
        if int(num[j]) != 0:
            break
        else:
            count += 1
    print(count)
    print(num)
    # print(num[-1])

trailingZeroes(1808548329)
