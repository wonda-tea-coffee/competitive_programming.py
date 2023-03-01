import sys
input = lambda: sys.stdin.readline().rstrip()

N, X = map(int, input().split())
dp = [[(0, 10**9)]*(X+1) for _ in range(N+1)]

for i in range(N):
    A, B, C = map(int, input().split())
    for j in range(X+1):
        if j+B <= X:
            gold, silver = dp[i][j+B]
            dp[i+1][j] = max(dp[i][j], (gold+C, silver-A))
        else:
            dp[i+1][j] = dp[i][j]

ans = (0, 0, 0)
for i in range(X+1):
    gold, silver = dp[N][i]
    ans = max(ans, (gold, silver, i))
print(*ans)
