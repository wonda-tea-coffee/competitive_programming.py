N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]
dp = [[10**10]*(M+1) for _ in range(N+1)]

for m in range(M):
    dp[0][m] = 0

for n in range(N):
    for m in range(M):
        dp[n+1][m+1] = min(dp[n+1][m], dp[n][m] + C[m]*D[n])

print(dp[N][M])
