import copy

n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [50000]*(n+1)
dp[0] = 0
for i in range(m):
    for j in range(n):
        if j + c[i] <= n:
            dp[j + c[i]] = min(dp[j + c[i]], dp[j] + 1)
    ndp = copy.deepcopy(dp)

    for j in range(n):
        if j + c[i] <= n:
            ndp[j + c[i]] = min(ndp[j + c[i]], dp[j] + 1)

    dp = ndp

print(dp[n])
