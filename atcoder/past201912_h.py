N = int(input())
C = list(map(int, input().split()))
sell = [0]*N
cnt2 = 0
cnt3 = 0
min2 = min(C[0::2])
minall = min(C)

Q = int(input())
for _ in range(Q):
    t, *q = map(int, input().split())

    if t == 1:
        x, a = q
        x -= 1
        sx = C[x] - sell[x] - cnt3
        if x % 2 == 0: sx -= cnt2
        if sx >= a:
            sx -= a
            sell[x] += a
            if x % 2 == 0: min2 = min(min2, sx)
            minall = min(minall, sx)
    elif t == 2:
        a = q[0]
        if min2 >= a:
            min2 -= a
            cnt2 += a
            minall = min(minall, min2)
    else:
        a = q[0]
        if minall >= a:
            min2 -= a
            minall -= a
            cnt3 += a

# print(sell, cnt2, cnt3)
print(sum(sell) + cnt2*((N+1)//2) + cnt3*N)
