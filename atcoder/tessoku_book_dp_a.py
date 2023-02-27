N = int(input())
h = [0] + list(map(int, input().split()))
dp = [0]*(N+1)
dp[2] = abs(h[1] - h[2])
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]), dp[i-2] + abs(h[i]-h[i-2]))

print(dp[N])
