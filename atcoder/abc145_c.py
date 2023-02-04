import math

N = int(input())
G = []
for i in range(N):
    G.append(tuple(map(int, input().split())))

dist = 0

def dfs(d, x, y, visited):
    if len(visited) == N:
        return d

    ret = 0
    for i in range(N):
        if i in visited: continue
        visited.add(i)
        ret += dfs(d + math.sqrt((x - G[i][0])**2 + (y - G[i][1])**2), G[i][0], G[i][1], visited)
        visited.remove(i)

    return ret

for i in range(N):
    dist += dfs(0, G[i][0], G[i][1], set({i}))

print(dist / math.factorial(N))
