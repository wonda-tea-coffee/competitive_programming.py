from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)

edge = []
for i in range(N):
    if len(G[i]) == 1:
        edge.append(i)
    elif len(G[i]) > 2:
        print("No")
        sys.exit(0)

if len(edge) != 2:
    print("No")
    sys.exit(0)

Q = deque([(edge[0], -1)])
done = set({edge[0]})
while Q:
    cur, pre = Q.popleft()
    for gi in G[cur]:
        if gi == edge[1]:
            done.add(edge[1])
            break
        elif gi == pre:
            continue
        else:
            Q.append((gi, cur))
            done.add(gi)

if len(done) == N:
    print("Yes")
else:
    print("No")
