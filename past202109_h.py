from collections import deque

N, X = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b, c))
    edges[b].append((a, c))

for i in range(N):
    dist = [-1] * N
    dist[i] = 0
    q = deque([i])
    while q:
        x = q.pop()
        for y, cost in edges[x]:
            if dist[y] != -1: continue
            dist[y] = dist[x] + cost
            q.append(y)
    if X in dist:
        print("Yes")
        exit()

print("No")
