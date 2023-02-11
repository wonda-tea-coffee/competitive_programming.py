from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        G[u].append(v)
        G[v].append(u)

    q = deque([(0, N-1, set([(0, N-1)]), 0)])
    res = False
    while q:
        curt, cura, state, step = q.popleft()
        if curt == N-1 and cura == 0:
            res = True
            print(step)
            break
        for tot in G[curt]:
            for toa in G[cura]:
                if (tot, toa) in state: continue
                if C[tot] == C[toa]: continue
                q.append((tot, toa, state|{(tot, toa)}, step+1))
    if not res:
        print(-1)
