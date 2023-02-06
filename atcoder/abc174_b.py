import math

N, D = map(int, input().split())
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    if math.sqrt(x*x + y*y) <= D:
        ans += 1

print(ans)
