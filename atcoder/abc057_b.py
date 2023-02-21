N, M = map(int, input().split())
a = []
b = []
for _ in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
c = []
d = []
for _ in range(M):
    ci, di = map(int, input().split())
    c.append(ci)
    d.append(di)

for n in range(N):
    num = -1
    mindist = float("inf")
    for m in range(M):
        dist = abs(a[n] - c[m]) + abs(b[n] - d[m])
        if dist < mindist:
            mindist = dist
            num = m+1
    print(num)
