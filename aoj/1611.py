# オリジナル
# https://drken1215.hatenablog.com/entry/2020/03/10/160500

def solve():
    dp = [[-1]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = 0
        if i < N: dp[i][i+1] = 0

    for bet in range(2, N+1):
        for i in range(N-bet+1):
            j = i + bet
            if dp[i+1][j-1] == j-i-2:
                if abs(w[i] - w[j-1]) <= 1:
                    dp[i][j] = max(dp[i][j], j-i)
                else:
                    dp[i][j] = max(dp[i][j], j-i-2)
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])

    return dp[0][N]

while True:
    N = int(input())
    if N == 0: break
    w = list(map(int, input().split()))
    dp = [[-1]*N for _ in range(N)]
    print(solve())
