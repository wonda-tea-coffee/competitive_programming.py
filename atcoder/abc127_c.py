N, M = map(int, input().split())
lmax = 0
rmin = 10**100
for _ in range(M):
    l, r = map(int, input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)

if lmax <= rmin:
    print(rmin-lmax+1)
else:
    print(0)
