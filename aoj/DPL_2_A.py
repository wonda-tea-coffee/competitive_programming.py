import math

N, M = map(int, input().split())
E = {}
for _ in range(M):
    s, t, d = map(int, input().split())
    E[(s, t)] = d
INF = float("inf")
L = 1<<N
ans = INF
for start in range(1):
    dp = [[INF]*N for _ in range(L)]
    for i in range(N):
        dp[0][i] = 0
        dp[1<<start][i] = 0
    for n in range(L):
        if (n>>start)&1 == 0: continue
        # print("n =", n)
        for s, t in E:
            if (n>>s)&1 == 0: continue
            if (n>>t)&1 == 1: continue

            m = n | (1<<t)
            # print("  (s, t, m) = (%d, %d, %d)" % (s, t, m), "dp[n][s] = ", dp[n][s])
            dp[m][t] = min(dp[m][t], dp[n][s] + E[(s, t)])

    # print(dp)
    for i in range(N):
        if (i, start) in E:
            ans = min(ans, dp[-1][i] + E[(i, start)])

if ans == INF:
    print(-1)
else:
    print(ans)
