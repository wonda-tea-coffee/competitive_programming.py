H, W = map(int, input().split())
a = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]

for i in range(H):
    if a[i][0] == "#": break
    dp[i][0] = 1
for i in range(W):
    if a[0][i] == "#": break
    dp[0][i] = 1

for i in range(1, H):
    for j in range(1, W):
        if a[i][j] == "#": continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007

print(dp[-1][-1])
