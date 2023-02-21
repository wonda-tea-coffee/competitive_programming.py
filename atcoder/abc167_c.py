N, M, X = map(int, input().split())
A = []
C = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

INF = float("inf")
ans = INF
for bit in range(1<<N):
    rikaido = [0]*M
    cost = 0
    for i in range(N):
        if (bit>>i)&1 == 0: continue
        cost += C[i]
        for j in range(M):
            rikaido[j] += A[i][j]

    res = True
    for r in rikaido:
        res &= r >= X
    if res:
        ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)
