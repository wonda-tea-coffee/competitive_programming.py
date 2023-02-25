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

INF = 10**100
dist = []
# 街t1,t2,...tKと街sを始点とした各街への最短経路を求める
# O(K*log(N+M))
for ti in t:
    dist_i = [INF]*N
    dist_i[ti] = 0
    que = deque([(0, ti)])

    while que:
        d, u = que.popleft()
        for v in E[u]:
            if dist_i[v] > d + 1:
                dist_i[v] = d + 1
                que.append((dist_i[v], v))

    res = []
    for tj in t:
        res.append(dist_i[tj])
    dist.append(res)

ALL = 1<<K
cost = [[INF]*K for _ in range(ALL)]
cost[0][0] = 0
for i in range(K):
    cost[1<<i][i] = dist[K][i]

for bit in range(ALL):
    for i in range(K):
        if (bit>>i)&1 == 0: continue
        for j in range(K):
            if (bit>>j)&1 == 1: continue
            to = bit | (1<<j)
            cost[to][j] = min(cost[to][j], cost[bit][i] + dist[i][j])

print(min(cost[-1]))
