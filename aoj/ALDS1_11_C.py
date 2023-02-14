from collections import deque

n = int(input())
E = [[] for _ in range(n+1)]
for _ in range(n):
    u, k, *v = map(int, input().split())
    if k > 0:
        E[u] = sorted(v)

Q = deque([(1, 0)])
done = [False]*(n+1)
ans = [-1]*(n+1)
while Q:
    cur, time = Q.popleft()

    if done[cur]: continue
    done[cur] = True

    ans[cur] = time

    for to in E[cur]:
        if done[to]: continue
        Q.append((to, time+1))

for i in range(1, n+1):
    print(i, ans[i])
