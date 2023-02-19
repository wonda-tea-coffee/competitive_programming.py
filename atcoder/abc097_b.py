import math

X = int(input())
ans = 1
for b in range(2, int(math.sqrt(X))+1):
    p = 2
    while b**p <= X:
        ans = max(ans, b**p)
        p += 1
print(ans)
