N, M = map(int, input().split())
k = []
s = []
for _ in range(M):
    ki, *si = map(int, input().split())
    k.append(ki)
    s.append(list(map(lambda x: x-1, si)))
p = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    on = 0
    # print("i:", i)
    for j in range(M):
        cnt = 0

        for k in s[j]:
            if (i >> k) & 1 == 1:
                cnt += 1

        # print("  cnt:", cnt, "p[%d] = %d" % (j, p[j]))

        if cnt % 2 == p[j]:
            on += 1

    if on == M:
        # print("on:", i)
        ans += 1

print(ans)
