N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[float("inf")]*N for _ in range(N)]

# 長さ0連鎖の演算量
for i in range(N):
    dp[i][i] = 0

# 長さ
for length in range(1, N):
    # 左端
    for i in range(N-length):
        # 右端
        j = i + le
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + M[i][0] * M[k][1] * M[j][1])

print(dp[0][-1])
