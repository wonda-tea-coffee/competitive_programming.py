import sys
sys.setrecursionlimit(1000000)

N = int(input())
done = set()
G = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(u):
    done.add(u)
    for v in G[u]:
        if v in done:
            continue
        dfs(v)

dfs(1)

if len(done) == N:
    print("Yes")
else:
    print("No")
