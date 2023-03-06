N, M, K = map(int, input().split())
MOD = 998244353
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K+1):
        for k in range(1, min(j, M)+1):
            dp[i+1][j] += dp[i][j-k]

        dp[i+1][j] %= MOD

print(sum(dp[-1]) % MOD)
