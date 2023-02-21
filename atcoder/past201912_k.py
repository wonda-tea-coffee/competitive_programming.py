import sys
sys.setrecursionlimit(1000000)

N = int(input())
R = -1
edges = [[] for _ in range(N)]
for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

Q = int(input())
queries = [[] for _ in range(N)]
for q in range(Q):
    a, b = map(lambda x: int(x)-1, input().split())
    queries[a].append((q, b))

ans = [False]*Q
boss = [False]*N

def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]
    boss[i] = True
    for j in edges[i]:
        dfs(j)
    boss[i] = False

dfs(R)

for q in range(Q):
    if ans[q]:
        print("Yes")
    else:
        print("No")
