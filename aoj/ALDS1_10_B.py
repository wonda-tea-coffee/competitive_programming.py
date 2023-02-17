N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

matrices = [data[0][0]] + list(map(lambda x: x[-1], data))

for length in range(2, N+1):
    for i in range(1, N-length+2):
        j = i+length-1
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrices[i-1] * matrices[k] * matrices[j])

print(dp[1][N])
