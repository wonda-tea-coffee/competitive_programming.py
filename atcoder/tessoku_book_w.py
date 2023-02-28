N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

ALL = 1<<N
INF = 10**10
dp = [INF]*ALL
dp[0] = 0
for bit in range(ALL):
    for m in range(M):
        to = bit
        for n in range(N):
            to |= A[m][n]<<n
        dp[to] = min(dp[to], dp[bit]+1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
