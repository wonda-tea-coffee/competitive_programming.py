import bisect

d = int(input())
n = int(input())
m = int(input())
S = [0]
for _ in range(n-1):
    S.append(int(input()))
S.sort()
k = [int(input()) for _ in range(m)]

ans = 0
for ki in k:
    bi = bisect.bisect_right(S, ki)
    if bi == 0:
        i1 = -1
        i2 = bi
    elif bi == n:
        i1 = 0
        i2 = -1
    else:
        i1 = bi - 1
        i2 = bi
    d1 = min(abs(ki - S[i1]), d - abs(ki - S[i1]))
    d2 = min(abs(ki - S[i2]), d - abs(ki - S[i2]))
    ans += min(d1, d2)

print(ans)
