import heapq
from collections import defaultdict

N, M = map(int, input().split())
v = [0, N-1]
edges = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b, c))
    edges[b].append((a, c))
    v.append(a)
    v.append(b)
v.sort()
for i in range(len(v)-1):
    v1 = v[i]
    v2 = v[i+1]
    edges[v1].append((v2, abs(v2-v1)))
    edges[v2].append((v1, abs(v1-v2)))

que = [(0, 0)]
heapq.heapify(que)
done = set()

while que:
    cost, cur = heapq.heappop(que)

    if cur == N-1:
        print(cost)
        exit()
    if cur in done: continue
    done.add(cur)

    for to, ncost in edges[cur]:
        if to in done: continue
        heapq.heappush(que, (ncost+cost, to))
