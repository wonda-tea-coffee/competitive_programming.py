def is_ok(x):
    c = 0
    for i in range(N):
        if x < B[i]: continue
        k = (x - B[i]) // C[i] + 1
        c += min(k, A[i])

    return c >= K

N, K = map(int, input().split())
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

ok = max(B) + max(A)*max(C)
ng = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
