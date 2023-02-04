import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

visited = set()
heiro = set()
def dfs(cur, pre):
    if cur in visited: return
    visited.add(cur)

    for gi in G[cur]:
        if gi == pre: continue
        if gi in visited:
            # print(pre, cur, gi)
            heiro.add((cur, gi))
            heiro.add((gi, cur))
        else:
            dfs(gi, cur)

for i in range(N):
    dfs(i, -1)

print(len(heiro)//2)
