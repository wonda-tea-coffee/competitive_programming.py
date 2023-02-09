import math

def dist(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
maxdist = 0
for i in range(N):
    mindist = 10**100
    for j in range(K):
        mindist = min(mindist, dist((X[i], Y[i]), (X[A[j]], Y[A[j]])))

    maxdist = max(maxdist, mindist)

print(maxdist)
