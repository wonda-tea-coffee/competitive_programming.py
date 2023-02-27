N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    ret = 0
    for i in range(N):
        ret += x // A[i]
    return ret >= K

ok = 10**9+1
ng = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
