N = int(input())
s = sum(map(int, input().split()))
dp = [[[201]*(s+1) for _ in range(s+1)] for _ in range(N)]
dp[0][0][0] = 0

for i in range(N-1):
    for j in range(s+1):
        for k in range(j+1):
            for l in range(s-j+1):
                dp[i+1][j+l][l] = min(dp[i+1][j+l][l], dp[i][j][k] + ((k-l)**2 + 1) ** 0.5)

print(dp[-1][s][0])
