def bit_count(n):
    ret = 0
    while n > 0:
        ret += n & 1
        n >>= 1

    return ret

N, M = map(int, input().split())
xy = set([tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)])

ans = 0
for i in range(1<<N):
    # print("i:", i)
    res = True

    for j in range(N):
        if (i>>j)&1==0: continue
        for k in range(j+1, N):
            if (i>>k)&1==0: continue

            if (j, k) in xy or (k, j) in xy:
                pass
            else:
                res = False
        if not res:
            break

    if res:
        # print(" ", i)
        ans = max(ans, bit_count(i))

print(ans)
