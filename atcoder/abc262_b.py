from itertools import combinations

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)

ans = 0
for a, b, c in combinations(range(N), 3):
    if b in G[a] and c in G[b] and a in G[c]:
        ans += 1

print(ans)
