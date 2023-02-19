def stock(i, cnt1, cnt2, cnt3):
    sale = cnt1[i] + cnt3
    if i % 2 == 0: sale += cnt2
    return C[i] - sale

N = int(input())
C = list(map(int, input().split()))
minall = min(C)
minodd = min(C[::2])
Q = int(input())
ans = 0
cnt1 = [0]*N
cnt2 = 0
cnt3 = 0
for i in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        x, a = q
        x -= 1

        s = stock(x, cnt1, cnt2, cnt3)
        if s >= a:
            ans += a
            cnt1[x] += a
            s -= a
            if x % 2 == 0 and minodd > s:
                minodd = s
            if minall > s:
                minall = s
    elif t == 2:
        a = q[0]
        if minodd >= a:
            cnt2 += a
            ans += a * ((N+1)//2)
            minodd -= a
            if minall > minodd:
                minall = minodd
    elif t == 3:
        a = q[0]
        if minall >= a:
            cnt3 += a
            ans += a * N
            minall -= a
            minodd -= a

print(ans)
