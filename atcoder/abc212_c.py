import bisect

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 10**10
for ai in A:
    bl = bisect.bisect_left(B, ai)
    if bl == 0:
        ans = min(ans, abs(ai - B[0]))
    elif bl == M:
        ans = min(ans, abs(ai - B[-1]))
    else:
        ans = min(ans, abs(ai - B[bl]), abs(ai - B[bl-1]))
print(ans)
