from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    E[u].append((v, i))
    E[v].append((u, i))

seen = [False]*N
for i in range(N):
    if seen[i]: continue

    cnt_vertex = 0
    finded_edge = set()
    que = deque([i])
    while que:
        cur = que.popleft()

        if seen[cur]: continue
        cnt_vertex += 1
        seen[cur] = True

        for to, idx in E[cur]:
            finded_edge.add(idx)
            if seen[to]: continue
            que.append(to)

    if cnt_vertex != len(finded_edge):
        print("No")
        exit()

print("Yes")
