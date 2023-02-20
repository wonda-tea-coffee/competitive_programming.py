N, M = map(int, input().split())
A = [input() for _ in range(N)]
E = [[] for _ in range(11)]
for i in range(N):
    for j in range(M):
        if A[i][j] == "S":
            E[0].append((i, j))
        elif A[i][j] == "G":
            E[-1].append((i, j))
        else:
            E[int(A[i][j])].append((i, j))
INF = float("inf")
dp = [[INF]*M for _ in range(N)]
sy, sx = E[0][0]
dp[sy][sx] = 0

for i in range(10):
    for y1, x1 in E[i]:
        for y2, x2 in E[i+1]:
            dp[y2][x2] = min(dp[y2][x2], dp[y1][x1]+abs(y2-y1)+abs(x2-x1))

gy, gx = E[-1][0]
if dp[gy][gx] == INF:
    print(-1)
else:
    print(dp[gy][gx])
