import sys
sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edge[a].append(b)
    edge[b].append(a)

cnt = [0]*N
for j in range(Q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x

seen = [True]*N
seen[0] = False
def dfs(u):
    for v in edge[u]:
        if seen[v] == False: continue

        seen[u] = False
        cnt[v] += cnt[u]
        dfs(v)

dfs(0)

print(*cnt)
