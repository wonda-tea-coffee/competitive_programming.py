N = int(input())
A = list(map(int, input().split()))
M = 20
dp = [0]*(M+1)
dp[A[0]] = 1
for i in range(1, N-1):
    ndp = [0]*(M+1)
    for j in range(M+1):
        if 0 <= j - A[i] <= M:
            ndp[j] += dp[j - A[i]]
        if 0 <= j + A[i] <= M:
            ndp[j] += dp[j + A[i]]

    dp = ndp

print(dp[A[-1]])
