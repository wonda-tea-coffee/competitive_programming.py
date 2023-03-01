import sys
input = lambda: sys.stdin.readline().rstrip()

N, W = map(int, input().split())
M = 10**5
dp = [[10**15]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    w, v = map(int, input().split())
    for j in range(M+1):
        if j >= v:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v]+w)
        else:
            dp[i+1][j] = dp[i][j]

for i in range(M, -1, -1):
    if dp[N][i] <= W:
        print(i)
        exit()
