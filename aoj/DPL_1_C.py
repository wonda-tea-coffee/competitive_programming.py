import copy

N, W = map(int, input().split())
v = []
w = []
for _ in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

dp = [0]*(W+1)
for i in range(N):
    for j in range(W+1):
        if j + w[i] <= W:
            dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i])
    ndp = copy.deepcopy(dp)

    for j in range(W+1):
        if j + w[i] <= W:
            ndp[j + w[i]] = max(ndp[j + w[i]], dp[j] + v[i])

    dp = ndp

print(max(dp))
