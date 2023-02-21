import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append((b, 1))
    G[b].append((a, 1))

Q = []
done = [False]*N
heapq.heappush(Q, (0, 0))
min_dist = [-1]*N
while Q:
    dist, cur = heapq.heappop(Q)

    if done[cur]: continue
    done[cur] = True

    for to, d in G[cur]:
        ndist = dist+d
        if not done[to] and ndist <= 2 and (min_dist[to] == -1 or ndist < min_dist[to]):
            min_dist[to] = ndist
            heapq.heappush(Q, (ndist, to))

if min_dist[-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
