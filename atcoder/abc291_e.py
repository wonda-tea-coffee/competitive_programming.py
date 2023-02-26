import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
E = [[] for _ in range(N)]
indeg = [0]*N
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    E[x].append(y)
    indeg[y] += 1

s = -1
for i in range(N):
    if indeg[i] == 0:
        s = i
        break

visited = [False]*N
def dfs(cur, memo):
    # print(cur, memo)
    if len(memo) == N:
        print("Yes")
        memo.sort()
        print(*map(lambda x: x[1], memo))
        exit()

    if visited[cur]: return
    visited[cur] = True

    for to in E[cur]:
        if visited[to]: continue
        dfs(to, memo + [(to+1, memo[-1][1]+1)])

    visited[cur] = False

dfs(s, [(s+1, 1)])

print("No")
