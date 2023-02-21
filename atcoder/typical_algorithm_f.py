import heapq

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    E[u].append((v, c))
    E[v].append((u, c))

marked = [False]*N
marked[0] = True
marked_count = 1
ans = 0
Q = []
for to, c in E[0]:
    heapq.heappush(Q, (c, to))

while marked_count < N:
    cost, cur = heapq.heappop(Q)

    if marked[cur]: continue
    marked[cur] = True
    marked_count += 1

    # print(cur, cost)
    ans += cost

    for to, ncost in E[cur]:
        if marked[to]: continue
        heapq.heappush(Q, (ncost, to))

print(ans)
