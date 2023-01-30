import math

N, M = map(int, input().split())

ans = ""
for i in range(M):
    if (i+1)*math.log(N, 10) <= 9:
        ans += "o"
    else:
        ans += "x"

print(ans)
