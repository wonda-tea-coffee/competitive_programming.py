import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
E1 = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    E1[u-1].append((v-1, w))
    E2[v-1].append((u-1, w))
INF = 10**100

def dijkstra(u, edges):
    dist = [INF]*N
    dist[u] = 0
    done = [False]*N
    que = [(0, u)]
    heapq.heapify(que)

    while que:
        _, cur = heapq.heappop(que)

        if done[cur]: continue
        done[cur] = True

        for to, ncost in edges[cur]:
            if dist[to] <= dist[cur] + ncost: continue
            dist[to] = dist[cur] + ncost
            heapq.heappush(que, (dist[to], to))

    return dist

dist1 = dijkstra(0, E1)
dist2 = dijkstra(N-1, E2)
for k in range(N):
    if dist1[k] == INF or dist2[k] == INF:
        print(-1)
    else:
        print(dist1[k] + dist2[k])
