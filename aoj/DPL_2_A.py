N, M = map(int, input().split())
E = {}
for _ in range(M):
    s, t, d = map(int, input().split())
    E[(s, t)] = d
INF = float("inf")
L = 1<<N
dp = [[INF]*N for _ in range(L)]
for i in range(N):
    dp[0][i] = 0
    dp[1][i] = 0
for n in range(L):
    if (n>>0)&1 == 0: continue
    for s, t in E:
        if (n>>s)&1 == 0: continue
        if (n>>t)&1 == 1: continue
        m = n | (1<<t)
        dp[m][t] = min(dp[m][t], dp[n][s] + E[(s, t)])

ans = INF
for i in range(N):
    if (i, 0) in E:
        ans = min(ans, dp[-1][i] + E[(i, 0)])

if ans == INF:
    print(-1)
else:
    print(ans)
