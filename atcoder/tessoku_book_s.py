N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+w[i] <= W:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])

print(max(dp[-1]))
