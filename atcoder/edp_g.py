import sys
sys.setrecursionlimit(1000000)

def solve(x):
    if memo[x] >= 0: return memo[x]

    ret = 0
    for y in E[x]:
        ret = max(ret, solve(y)+1)

    memo[x] = ret
    return memo[x]

N, M = map(int, input().split())
E = [[] for _ in range(N)]
indeg = [0]*N
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    E[x].append(y)
    indeg[y] += 1
memo = [-1]*N

ans = 0
for i in range(N):
    if indeg[i] == 0:
        ans = max(ans, solve(i))
print(ans)
