N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

l = 0
r = N-1
ans = 0
while r-l > 0:
    t1 = A[l]/B[l]
    t2 = A[r]/B[r]
    if t1 < t2:
        ans += A[l]
        A[l] = 0
        l += 1
        A[r] -= t1*B[r]
    elif t1 > t2:
        A[r] = 0
        r -= 1
        ans += t2*B[l]
        A[l] -= t2*B[l]
    else:
        ans += A[l]
        A[l] = 0
        A[r] = 0
        l += 1
        r -= 1

if l > r or (l == r and A[l] == 0):
    print(ans)
else:
    assert l == r
    print(ans + A[l]/2)
