import heapq

N, M, _ = map(int, input().split())
A, B, C = zip(*[map(int, input().split()) for _ in range(M)])
X = list(map(int, input().split()))

A = [_-1 for _ in A]
B = [_-1 for _ in B]
E = [[] for _ in range(N)]
for i, j, cost in zip(A, B, C):
    E[i].append((cost, j))
    E[j].append((cost, i))

que = [] # (コスト, 街ID)
for cost, i in E[0]:
    heapq.heappush(que, (cost, i))

visited = {0}
res = []
for threshold in X:
    candidates = []
    while que and que[0][0] <= threshold:
        cost, i = heapq.heappop(que)
        candidates.append(i)
    for i in candidates:
        if not i in visited:
            visited.add(i)
            for new_cost, j in E[i]:
                heapq.heappush(que, (new_cost, j))
    res.append(len(visited))

for r in res:
    print(r)
