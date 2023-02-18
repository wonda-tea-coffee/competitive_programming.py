def solve():
    dp = [[0]*(N+1) for _ in range(N+1)]

    for bet in range(2, N+1):
        for i in range(N-bet+1):
            j = i + bet
            if dp[i+1][j-1] == j-i-2:
                if abs(W[i] - W[j-1]) < 2:
                    dp[i][j] = j-i
                else:
                    dp[i][j] = j-i-2
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j])

    return dp[0][N]

while True:
    N = int(input())
    if N == 0: break
    W = list(map(int, input().split()))
    print(solve())
