import math

P = int(input())
ans = 0
n = 10
while P > 0:
    fn = math.factorial(n)
    m = min(P // fn, 100)
    ans += m
    P -= fn * m
    n -= 1
print(ans)