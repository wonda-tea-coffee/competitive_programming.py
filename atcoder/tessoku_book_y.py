H, W = map(int, input().split())
c = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]

for wi in range(W):
    if c[0][wi] == "#": break
    dp[0][wi] = 1
for hi in range(H):
    if c[hi][0] == "#": break
    dp[hi][0] = 1

for hi in range(1, H):
    for wi in range(1, W):
        if c[hi][wi] == "#": continue
        dp[hi][wi] = dp[hi-1][wi] + dp[hi][wi-1]

print(dp[-1][-1])
