def is_ok(x):
    a = []
    for i in range(N):
        if x < H[i]: return False
        a.append((x-H[i])//S[i])
    a.sort()
    for i in range(N):
        if a[i] < i: return False
    return True

N = int(input())
H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

ng = 0
ok = max(H)+max(S)*(N-1)
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
