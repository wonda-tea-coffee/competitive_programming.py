N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    t1, l1, r1 = S[i]
    for j in range(i+1, N):
        t2, l2, r2 = S[j]

        if (t1 == 1 or t1 == 3) and (t2 == 1 or t2 == 2):
            p1 = r1 < l2
        else:
            p1 = r1 <= l2

        if (t2 == 1 or t2 == 3) and (t1 == 1 or t1 == 2):
            p2 = r2 < l1
        else:
            p2 = r2 <= l1

        if p1 or p2:
            pass
        else:
            ans += 1

print(ans)