from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
G = [set() for _ in range(N)]

for _ in range(Q):
    t, u, v = map(lambda x: int(x)-1, input().split())

    if t == 0:
        if v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
        else:
            G[u].add(v)
            G[v].add(u)
    else:
        res = False

        Q = deque([u])
        done = set({u})
        # print(G)
        while Q:
            cur = Q.popleft()
            # print("cur", cur)
            for gi in G[cur]:
                # print("  gi", gi)
                if gi in done:
                    continue
                elif gi == v:
                    res = True
                    break
                else:
                    Q.append(gi)
                    done.add(gi)

            if res:
                break

        if res:
            print("Yes")
        else:
            print("No")
