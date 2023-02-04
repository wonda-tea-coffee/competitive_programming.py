N, M = map(int, input().split())
p = [0] + [int(input()) for i in range(N)]

s = []
for i in range(N+1):
    for j in range(N+1):
        pair = p[i] + p[j]
        if pair <= M:
            s.append(pair)

s.sort()
ans = 0
import bisect
for si in s:
    r = bisect.bisect_right(s, M-si)
    ans = max(ans, si + s[r-1])

print(ans)
