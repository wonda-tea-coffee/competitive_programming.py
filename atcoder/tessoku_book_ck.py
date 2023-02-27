N = int(input())

def check(x):
    return x**3 + x >= N

ng = 0
ok = N
while abs(ok - ng) > 10**(-4):
    mid = (ok + ng) / 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
