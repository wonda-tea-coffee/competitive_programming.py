def cost(i, c):
    ret = 0
    for j in range(5):
        if S[j][i] != h[c]: ret += 1

    return ret

N = int(input())
S = [input() for _ in range(5)]
# dp[i][j] := 左からi-1列目までを一番右を色jで塗り替えたときの最小値
# dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + (i-1)列目を0で塗り替えた数
# dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + (i-1)列目を1で塗り替えた数
# dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + (i-1)列目を2で塗り替えた数
dp = [[10**10]*3 for _ in range(N+1)]
h = {0: "R", 1: "B", 2: "W"}

dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(N):
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + cost(i, 0)
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + cost(i, 1)
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + cost(i, 2)

print(min(dp[N]))
