import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, X, Y = map(int, input().split())
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    E[U].append(V)
    E[V].append(U)

parents = [-1]*(N+1)
que = deque([X])
while que:
    cur = que.popleft()

    for to in E[cur]:
        if parents[to] > 0: continue
        parents[to] = cur
        que.append(to)

ans = [Y]
while X != parents[Y]:
    ans.append(parents[Y])
    Y = parents[Y]

ans.append(X)
print(*ans[::-1])
