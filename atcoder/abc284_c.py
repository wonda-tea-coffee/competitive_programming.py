from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    edges[u].append(v)
    edges[v].append(u)
seen = [False]*N
ans = 0
for i in range(N):
    if seen[i]: continue
    que = deque([i])
    seen[i] = True
    ans += 1
    while que:
        cur = que.popleft()
        for to in edges[cur]:
            if seen[to]: continue
            seen[to] = True
            que.append(to)

print(ans)
