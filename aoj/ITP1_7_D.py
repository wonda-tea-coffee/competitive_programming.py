n, m, l = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

# print(a, b)

c = [[0] * l for _ in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    print(*c[i])
