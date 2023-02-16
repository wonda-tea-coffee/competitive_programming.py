import sys
sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    E[a].append(b)
    E[b].append(a)
cnt = [0]*N

for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p-1] += x

done = [False]*N
done[0] = True
def dfs(n):
    for i in E[n]:
        if done[i]: continue
        done[i] = True
        cnt[i] += cnt[n]
        dfs(i)

dfs(0)

print(*cnt)
