N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)

M = 10**5+1
dp = [W+1]*M
dp[0] = 0
for i in range(N):
    ndp = list(dp)
    for j in range(M):
        if dp[j] + w[i] <= W:
            ndp[j + v[i]] = min(ndp[j + v[i]], dp[j] + w[i])
    dp = ndp

for i in range(M-1, -1, -1):
    if dp[i] <= W:
        print(i)
        exit()
