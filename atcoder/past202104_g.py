import heapq

N, M, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    E[a].append((c, b))
    E[b].append((c, a))
X = list(map(int, input().split()))

visited = set([0])
Q = []
for i in E[0]:
    heapq.heappush(Q, i)

for xi in X:
    candidates = []
    while Q and Q[0][0] <= xi:
        _, u = heapq.heappop(Q)
        candidates.append(u)
    for c in candidates:
        if c in visited: continue
        visited.add(c)
        for i in E[c]:
            heapq.heappush(Q, i)

    print(len(visited))
