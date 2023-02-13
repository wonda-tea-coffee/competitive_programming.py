import heapq

N, M, Q = map(int, input().split())
E = [[] for i in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    E[a].append((c, b))
    E[b].append((c, a))
X = list(map(int, input().split()))

que = [] # (コスト, 街ID)
for cost, i in E[0]:
    heapq.heappush(que, (cost, i))

visited = {0}
for threshold in X:
    candidates = []
    while que and que[0][0] <= threshold:
        _, i = heapq.heappop(que)
        candidates.append(i)
    for i in candidates:
        if i in visited: continue
        visited.add(i)
        for new_cost, j in E[i]:
            heapq.heappush(que, (new_cost, j))

    print(len(visited))
