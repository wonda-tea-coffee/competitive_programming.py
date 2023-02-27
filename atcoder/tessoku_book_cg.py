N = int(input())
M = 1500
P = [[0]*(M+1) for _ in range(M+1)]
for _ in range(N):
    x, y = map(int, input().split())
    P[x][y] += 1

D = []
for i in range(M+1):
    di = []
    d = 0
    for j in range(M+1):
        d += P[i][j]
        di.append(d)
    D.append(di)
for i in range(M):
    for j in range(M+1):
        D[i+1][j] += D[i][j]

# for di in D:
#     print(di)

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    ans = D[c][d] + D[a-1][b-1] - D[c][b-1] - D[a-1][d]
    print(ans)
