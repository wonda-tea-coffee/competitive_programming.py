from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    E[u].append(v)
    E[v].append(u)
s = int(input())-1
K = int(input())
t = list(map(lambda x: int(x)-1, input().split())) + [s]

min_dist = []
for ti in t:
    Q = deque([ti])
    INF = 10**100
    dist = [INF]*N
    dist[ti] = 0
    while Q:
        cur = Q.popleft()
        for to in E[cur]:
            if dist[to] != INF: continue
            dist[to] = dist[cur] + 1
            Q.append(to)
    res = []
    for tj in t:
        res.append(dist[tj])
    min_dist.append(res)

ALL = 1<<K
dp = [[INF]*K for _ in range(ALL)]
for i in range(K):
    dp[1<<i][i] = min_dist[K][i]

for bit in range(ALL):
    for i in range(K):
        for j in range(K):
            if (bit>>j)&1 == 1 or i == j: continue

            to = bit | (1<<j)
            dp[to][j] = min(dp[to][j], dp[bit][i] + min_dist[i][j])

print(min(dp[-1]))
