N = int(input())
a = list(map(int, input().split()))

ans = 0
min2 = 10**10
min3 = 10**10
cnt2 = [0]*N
cnt3 = [0]*N
for i in range(N):
    t = a[i]

    c2 = 0
    while t % 2 == 0:
        t //= 2
        c2 += 1
    cnt2[i] = c2
    min2 = min(min2, c2)

    c3 = 0
    while t % 3 == 0:
        t //= 3
        c3 += 1
    cnt3[i] = c3
    min3 = min(min3, c3)

ans = 0
for i in range(N):
    while cnt2[i] > min2:
        ans += 1
        cnt2[i] -= 1
        a[i] //= 2
    while cnt3[i] > min3:
        ans += 1
        cnt3[i] -= 1
        a[i] //= 3

if len(set(a)) == 1:
    print(ans)
else:
    print(-1)
