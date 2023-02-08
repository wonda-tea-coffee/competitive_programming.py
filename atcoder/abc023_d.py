def check(X):
    a = []
    for h, s in baloon:
        if X < h: return False
        a.append((X-h)//s)
    a.sort()
    for i in range(N):
        if i > a[i]: return False

    return True

N = int(input())
baloon = [list(map(int, input().split())) for _ in range(N)]

ng = 0
ok = 10**18
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
