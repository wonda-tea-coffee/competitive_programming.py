S = input()
T = input()
N = len(S)
M = len(T)
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if S[i] != T[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[N-1][M-1])
