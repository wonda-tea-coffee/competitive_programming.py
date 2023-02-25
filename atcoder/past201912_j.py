import heapq

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def grid_dijkstra(sy, sx):
    dist = [[10**100]*W for _ in range(H)]
    que = [(0, sy, sx)]
    heapq.heapify(que)
    dist[sy][sx] = 0

    while que:
        d, y, x = heapq.heappop(que)
        if d > dist[y][x]: continue
        for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if 0 <= ny < H and 0 <= nx < W and d + A[ny][nx] < dist[ny][nx]:
                dist[ny][nx] = d + A[ny][nx]
                heapq.heappush(que, (dist[ny][nx], ny, nx))

    return dist

dist1 = grid_dijkstra(H-1, 0)
dist2 = grid_dijkstra(H-1, W-1)
dist3 = grid_dijkstra(0, W-1)

ans = 10**100
for cy in range(H):
    for cx in range(W):
        ans = min(ans, dist1[cy][cx] + dist2[cy][cx] + dist3[cy][cx] - 2*A[cy][cx])

print(ans)
