import sys
sys.setrecursionlimit(1000000)

def dfs(i):
    global time

    if i in seen: return
    seen.add(i)

    time += 1
    start = time
    for to in E[i]:
        dfs(to)
    time += 1
    end = time

    res[i] = (start, end)

n = int(input())
E = [set() for _ in range(n+1)]
for _ in range(n):
    u, _, *v = map(int, input().split())
    E[u] = sorted(v)
seen = set()
time = 0
res = [None]*(n+1)

for i in range(1, n+1):
    dfs(i)

for i in range(1, n+1):
    assert res[i] is not None
    print(i, *res[i])
