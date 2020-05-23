def giveSum(n):
    ans = 0
    n = str(n)
    for i in range(len(n)):
        ans += int(n[i]) ** 2
    return ans

def isHappy(num):
    # import pdb; pdb.set_trace()
    res = giveSum(num)
    if res == 1:
        print("true")
    else:
        isHappy(res)


isHappy(4)
