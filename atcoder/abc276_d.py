import math

N = int(input())
a = list(map(int, input().split()))

def gcd(a):
    ret = a[0]
    for i in range(1, len(a)):
        ret = math.gcd(ret, a[i])
    return ret

g = gcd(a)
ans = 0
for i in range(N):
    a[i] //= g
    for d in [2, 3]:
        while a[i] % d == 0:
            a[i] //= d
            ans += 1
    if a[i] != 1:
        print(-1)
        exit()

print(ans)
