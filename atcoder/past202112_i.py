import heapq
from collections import defaultdict

N, M = map(int, input().split())
edges = defaultdict(lambda: [])
B = set([1, N])
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
    B.add(a)
    B.add(b)
B = sorted(B)
# エレベーター間の辺（階段）を用意
for i in range(len(B)-1):
    d = B[i+1] - B[i]
    edges[B[i+1]].append((d, B[i]))
    edges[B[i]].append((d, B[i+1]))

Q = [(0, 1)]
done = set()
while Q:
    c0, u = heapq.heappop(Q)

    if u in done: continue
    done.add(u)

    if u == N: exit(print(c0))

    for c1, v in edges[u]:
        if v in done: continue
        heapq.heappush(Q, (c0+c1, v))
