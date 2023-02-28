N, W = map(int, input().split())
w = [0]
v = [0]
for _ in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)

M = 100000
dp = [[10**15]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
	for j in range(M+1):
		if j < v[i]:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]]+w[i])

for i in range(M, -1, -1):
	if dp[N][i] <= W:
		print(i)
		exit()
