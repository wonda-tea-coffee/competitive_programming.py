from collections import *

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        G[u] += [v]
        G[v] += [u]

    D = [[-1] * N for _ in range(N)]
    D[0][-1] = 0
    Q = deque([(0, N-1)])
    while Q:
        vt, va = Q.popleft()
        for ct in G[vt]:
            for ca in G[va]:
                if C[ct] != C[ca] and D[ct][ca] < 0:
                    D[ct][ca] = D[vt][va] + 1
                    Q.append((ct, ca))
    print(D[-1][0])
