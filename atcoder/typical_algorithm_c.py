N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = float("inf")
dp = [[INF]*N for _ in range(1<<N)]
dp[0][0] = 0

for bit in range(1<<N):
    if dp[bit] == INF: continue
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if bit&(1<<j): continue
            to = bit | (1<<j)
            ncost = dp[bit][i] + A[i][j]
            dp[to][j] = min(dp[to][j], ncost)

print(dp[-1][0])
