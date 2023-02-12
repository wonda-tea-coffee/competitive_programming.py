from collections import deque

N, X = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))

minpath = [[10**10]*N for _ in range(N)]

for i in range(N):
    Q = deque([(i, 0)])
    visited = set([i])
    minpath[i][i] = 0
    while Q:
        cur, length = Q.popleft()

        for to, cost in G[cur]:
            if to in visited: continue
            visited.add(to)
            minpath[cur][to] = min(minpath[cur][to], cost)
            minpath[i][to] = min(minpath[i][to], length+cost)

            Q.append((to, length+cost))

for i in range(N):
    for j in range(N):
        if minpath[i][j] == X:
            print("Yes")
            exit()

print("No")
