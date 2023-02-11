from collections import deque, defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))
X = list(map(int, input().split()))

T = [-1] * N
visited = defaultdict(lambda: set())
visited[0].add(0)
deq = deque([(0, 0)])
while deq:
    cur, day = deq.popleft()
    # print("cur:", cur, "day:", day, "G[cur]:", G[cur])
    if day == Q: break

    deq.append((cur, day+1))
    visited[day].add(cur)

    for to, cost in G[cur]:
        if (T[to] == -1 or T[to] < X[day]) and cost <= X[day]:
            T[to] = X[day]
            deq.append((to, day+1))
            visited[day].add(to)

for i in range(Q):
    print(len(visited[i]))
