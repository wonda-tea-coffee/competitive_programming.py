import itertools

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].add(b)
    G[b].add(a)

ans = 0
for x in itertools.permutations(list(range(1, N))):
    s = 0
    res = True
    for xi in x:
        if not xi in G[s]:
            res = False
            break

        s = xi
    
    if res:
        ans += 1

print(ans)
