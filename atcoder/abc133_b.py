import math

def dist(p, q):
    ret = 0
    for i in range(len(p)):
        ret += abs(p[i] - q[i])**2
    return math.sqrt(ret)

N, D = map(int, input().split())

X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        d = dist(X[i], X[j])
        if d == int(d):
            ans += 1

print(ans)
