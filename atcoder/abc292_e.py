import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    E[u].append(v)

ans = 0
for i in range(N):
    done = [False]*N
    que = deque([(i, 0)])
    while que:
        cur, cost = que.popleft()
        if done[cur]: continue
        done[cur] = True
        if cost >= 2:
            ans += 1
        for to in E[cur]:
            if done[to]: continue
            que.append((to, cost+1))
print(ans)
