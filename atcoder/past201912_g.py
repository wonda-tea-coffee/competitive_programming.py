from itertools import combinations

N = int(input())
A = [[0]*N for _ in range(N)]
offset = 1
for i in range(N-1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        A[i][j + offset] = a[j]
        A[j + offset][i] = a[j]
    offset += 1

ans = -10**10
for bit in range(3**N):
    g = [[] for _ in range(3)]
    for i in range(N):
        g[bit // 3**i % 3].append(i)
    c = 0
    for i in range(3):
        for x, y in combinations(g[i], 2):
            c += A[x][y]
    ans = max(ans, c)

print(ans)
