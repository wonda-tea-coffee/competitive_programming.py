n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for _ in range(m):
    b.append(int(input()))

# print(a, b)

c = []
for i in range(n):
    d = 0
    for j in range(m):
        d += a[i][j]*b[j]
    
    c.append(d)

for i in range(n):
    print(c[i])
