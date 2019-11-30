import time

def check_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        # print(f"Function name {func.__name__ }: {stop-start:.2f} secs")
        print(stop-start)
        return result
    return wrapper

# using recursion
@check_time
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(1701, 3768))

#using loops
@check_time
def compute_gcd(a,b):
    if a>b:
        min = b
    else:
        min = a
    for i in range(1, min+1):
        if ((a%i == 0) and (b%i == 0)):
            x = i
    return x
print(compute_gcd(1701, 3768))
