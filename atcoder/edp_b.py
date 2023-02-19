N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [float("inf")]*N
dp[0] = 0
for i in range(N):
    j = 1
    while j <= K and i-j >= 0:
        dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))
        j += 1
print(dp[-1])
