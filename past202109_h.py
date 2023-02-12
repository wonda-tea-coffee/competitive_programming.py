from collections import deque

N, X = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))

for i in range(N):
    dist = [-1] * N
    dist[i] = 0
    Q = deque([i])
    while Q:
        cur = Q.pop()
        for to, cost in G[cur]:
            if dist[to] != -1: continue
            dist[to] = dist[cur] + cost
            Q.append(to)

    if X in dist:
        exit(print("Yes"))

print("No")
