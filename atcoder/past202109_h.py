from collections import deque

N, X = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    E[a].append((b, c))
    E[b].append((a, c))

for i in range(N):
    dist = [-1]*N
    dist[i] = 0

    Q = deque([(i, 0)])
    while Q:
        v, _ = Q.popleft()

        for nv, ncost in E[v]:
            if dist[nv] != -1: continue
            dist[nv] = dist[v] + ncost
            Q.append((nv, dist[nv]))

    if X in dist:
        exit(print("Yes"))

print("No")
