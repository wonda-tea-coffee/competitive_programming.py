N, M = map(int, input().split())
dist = [[float("inf")]*N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for _ in range(M):
    u, v, c = map(int, input().split())
    dist[u][v] = c
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

ans = 0
for x in range(N):
    for y in range(N):
        ans += dist[x][y]
print(ans)
