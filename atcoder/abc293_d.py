from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
c = [0]*N
for _ in range(M):
    A, _, C, _ = input().split()
    A = int(A)-1
    C = int(C)-1
    E[A].append(C)
    E[C].append(A)
    c[A] += 1
    c[C] += 1

X = 0
Y = 0
done = [False]*N
for i in range(N):
    if done[i]: continue

    que = deque([i])
    res = c[i] == 2
    while que:
        cur = que.popleft()
        for to in E[cur]:
            if done[to]: continue
            done[to] = True
            res &= c[to] == 2
            que.append(to)
    if res:
        X += 1
    else:
        Y += 1

print(X, Y)
