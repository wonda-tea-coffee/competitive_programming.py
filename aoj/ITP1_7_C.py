r, c = map(int, input().split())
G = []
for i in range(r):
    G.append(list(map(int, input().split())))

for i in range(r):
    G[i].append(sum(G[i]))

G.append([])
for ci in range(c):
    s = 0
    for ri in range(r):
        s += G[ri][ci]
    G[r].append(s)
G[r].append(sum(G[r]))

for i in range(r+1):
    print(*G[i])
