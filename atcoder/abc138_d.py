import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edge[a].append(b)
    edge[b].append(a)
cnt = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p-1] += x

done = [False]*N
done[0] = True
def dfs(n):
    for i in edge[n]:
        if done[i]: continue
        done[i] = True
        cnt[i] += cnt[n]
        dfs(i)

dfs(0)

print(*cnt)
