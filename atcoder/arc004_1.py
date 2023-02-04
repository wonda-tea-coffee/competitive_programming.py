import math

def dist(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

N = int(input())
G = []
for _ in range(N):
    G.append(tuple(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, dist(G[i], G[j]))

print(ans)
