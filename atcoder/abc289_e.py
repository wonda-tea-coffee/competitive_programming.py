from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)

    Q = deque([(0, N-1, 0)])
    ans = -1
    D = [[-1]*N for _ in range(N)]
    D[0][-1] = 0
    while Q:
        t, a, step = Q.popleft()

        if t == N-1 and a == 0:
            break

        for tot in E[t]:
            for toa in E[a]:
                if D[tot][toa] >= 0: continue
                if C[tot] == C[toa]: continue
                D[tot][toa] = D[t][a] + 1
                Q.append((tot, toa, step+1))

    print(D[-1][0])
