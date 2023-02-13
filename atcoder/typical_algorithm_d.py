import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

Q = []
heapq.heappush(Q, (0, 0))
dist = [-1] * N
dist[0] = 0
done = [False] * N
done[0] = True

while Q:
    d, v = heapq.heappop(Q)
    for nv, c in G[v]:
        nd = d+c
        if (dist[nv] == -1 or dist[nv] > nd) and not done[nv]:
            dist[nv] = nd
            heapq.heappush(Q, (nd, nv))

print(dist[-1])
