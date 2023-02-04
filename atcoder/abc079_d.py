H, W = map(int, input().split())
c = []
for i in range(10):
    c.append(list(map(int, input().split())))

ans = 0
INF = float('inf')
mins = [[INF]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        mins[i][j] = c[i][j]

for k in range(10):
    for i in range(10):
        for j in range(10):
            mins[i][j] = min(mins[i][j], mins[i][k] + mins[k][j])

for i in range(H):
    A = list(map(int, input().split()))
    for j in range(W):
        if A[j] == -1: continue
        ans += mins[A[j]][1]

# print("A", mins)

print(ans)
