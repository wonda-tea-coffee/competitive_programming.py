import math
N = int(input())

ans = 10**100
for b in range(int(math.log(N, 2)) + 1):
    a = N // 2**b
    c = N - a * 2**b
    ans = min(ans, a+b+c)

print(ans)