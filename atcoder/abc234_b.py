import math

def dist(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

N = int(input())
p = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, dist(p[i], p[j]))
print(ans)