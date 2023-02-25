import bisect

N = int(input())
L = sorted(list(map(int, input().split())))
ans = 0

for i in range(N):
    a = L[i]
    for j in range(i+1, N):
        b = L[j]
        l = bisect.bisect_right(L, b-a)
        r = bisect.bisect_left(L, a+b)-1
        if l > r: continue
        v = r-l+1
        if l <= i <= r: v -= 1
        if l <= j <= r: v -= 1
        ans += max(v, 0)

print(ans//3)
