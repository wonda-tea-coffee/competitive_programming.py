from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    E[a].append(b)
    E[b].append(a)

S = 0
done = [False]*N
for i in range(N):
    if done[i]: continue
    S += 1
    Q = deque([i])
    while Q:
        cur = Q.popleft()
        if done[cur]: continue
        done[cur] = True
        for to in E[cur]:
            if done[to]: continue
            Q.append(to)

print(M - N + S)
