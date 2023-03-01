from itertools import combinations
from collections import defaultdict

N, L, K = map(int, input().split())
S = [input() for _ in range(N)]
T = defaultdict(int)
for s in S:
    for w in combinations(list(range(L)), K):
        t = []
        for i in range(L):
            if i in w:
                t.append("?")
            else:
                t.append(s[i])
        T["".join(t)] += 1

ans = 0
for t in T:
    if T[t] > ans:
        ans = T[t]
print(ans)
