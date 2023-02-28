from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
E = [set() for _ in range(N)]
for _ in range(Q):
    t, u, v = map(lambda x: int(x)-1, input().split())
    if t == 0:
        if v in E[u]:
            E[u].remove(v)
            E[v].remove(u)
        else:
            E[u].add(v)
            E[v].add(u)
    else:
        que = deque([u])
        seen = set()
        res = False
        while que:
            cur = que.popleft()
            if cur == v:
                res = True
            if cur in seen: continue
            seen.add(cur)
            for to in E[cur]:
                if to in seen: continue
                que.append(to)
        if res:
            print("Yes")
        else:
            print("No")
