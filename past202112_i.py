from heapq import heappush, heappop

N, M = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(M)]
itov = {1, N}
for a, b, c in ABC:
    itov.add(a)
    itov.add(b)
itov = sorted(itov)
l = len(itov)
vtoi = {v: i for i, v in enumerate(itov)}
adj = [[] for _ in range(l)]
for i in range(l-1):
    c = itov[i+1] - itov[i]
    adj[i].append((i+1, c))
    adj[i+1].append((i, c))

for a, b, c in ABC:
    a = vtoi[a]
    b = vtoi[b]
    adj[a].append((b, c))
    adj[b].append((a, c))

time = [0] + [10**18] * (l - 1)
seen = [False] * l
hq = [(0, 0)]
while hq:
    p = heappop(hq)[1]
    if seen[p]: continue
    seen[p] = True
    for c, t in adj[p]:
        if time[c] > time[p] + t:
            time[c] = time[p] + t
            heappush(hq, (time[c], c))

print(time[-1])
