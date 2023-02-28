N = int(input())
P = [0]
A = [0]
for i in range(N):
	pi, ai = map(int, input().split())
	P.append(pi)
	A.append(ai)

# 動的計画法（bet は r-l の値)
dp = [[0]*(N+1) for _ in range(N+1)]

for bet in reversed(range(N-1)):
	for l in range(1, N-bet+1):
		r = l+bet

		# l-1 番目のブロックを取り除くときの得点を求める
		score1 = 0
		if l > 1 and l <= P[l-1] and P[l-1] <= r:
			score1 = A[l-1]

		# r+1 番目のブロックを取り除くときの得点を求める
		score2 = 0
		if r < N and l <= P[r+1] and P[r+1] <= r:
			score2 = A[r+1]

		if l == 1:
			dp[l][r] = dp[l][r+1] + score2
		elif r == N:
			dp[l][r] = dp[l-1][r] + score1
		else:
			dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)

ans = 0
for i in range(1, N+1):
	ans = max(ans, dp[i][i])
print(ans)
