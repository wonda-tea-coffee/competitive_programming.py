import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
E = [set() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    if v in E[u]: continue
    E[u].add(v)

que = deque()
for a in range(1, N+1):
    for b in E[a]:
        que.append((a, b))

memo = [None]*(N+1)
for a in range(1, N+1):
    memo[a] = (set(range(1, N+1)) - {a} - E[a])

ans = 0
added_edge = set()
while que:
    a, b = que.popleft()
    c = E[b] & memo[a]
    for ci in c:
        if (a, ci) in added_edge: continue
        added_edge.add((a, ci))
        ans += 1
        E[a].add(ci)
        que.append((a, ci))

print(ans)
