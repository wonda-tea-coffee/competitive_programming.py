def is_bomb(n):
    for i in range(M):
        if ((n>>A[i]) & 1) == ((n>>B[i]) & 1) == ((n>>C[i]) & 1) == 1:
            return True
    return False

N, M = map(int, input().split())
A = []
B = []
C = []
for _ in range(M):
    a, b, c = map(lambda x: int(x)-1, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

ans = 0
for n in range(1<<N):
    if is_bomb(n): continue

    c = 0
    for mazeru in range(N):
        # もう混ざってる
        if (n>>mazeru)&1 == 1: continue

        mazeta = n | (1<<mazeru)
        assert n != mazeta

        if is_bomb(mazeta):
            c += 1

    # print(n, c)
    if ans < c:
        ans = max(ans, c)

print(ans)
