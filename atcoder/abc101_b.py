def s(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

N = int(input())
if N % s(N) == 0:
    print("Yes")
else:
    print("No")