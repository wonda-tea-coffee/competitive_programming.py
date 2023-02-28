from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, Q, K = map(int, input().split())
a = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

dist = []
for k in range(K):
    done = [False]*(N+1)
    que = deque([(a[k], 0)])
    d = [0]*(N+1)
    while que:
        cur, cost = que.popleft()
        if done[cur]: continue
        done[cur] = True
        d[cur] = cost
        for to in edges[cur]:
            if done[to]: continue
            que.append((to, cost+1))
    dist.append(d)

for _ in range(Q):
    s, t = map(int, input().split())
    ans = 10**10
    for k in range(K):
        ans = min(ans, dist[k][s] + dist[k][t])
    print(ans)
