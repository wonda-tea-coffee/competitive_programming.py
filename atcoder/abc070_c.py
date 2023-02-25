import math

def lcm(a):
    ret = 1
    for ai in a:
        ret = ret * ai // math.gcd(ret, ai)
    return ret

N = int(input())
T = [int(input()) for _ in range(N)]
print(lcm(T))
