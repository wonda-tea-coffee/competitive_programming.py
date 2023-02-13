def is_ok(x):
    cnt = 0

    for i in range(N):
        if x < B[i]: continue
        # B[i]+C[i]*s <= x
        # s <= (x - B[i])/C[i]
        cnt += min((x - B[i])//C[i] + 1, A[i])

    return cnt >= K

N, K = map(int, input().split())
A, B, C = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

ng = 0
ok = 10**30
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
