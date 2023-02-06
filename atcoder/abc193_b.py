N = int(input())
INF = 10**100
ans = INF
for _ in range(N):
    a, p, x = map(int, input().split())
    if a < x:
        ans = min(ans, p)

if ans == INF:
    print(-1)
else:
    print(ans)