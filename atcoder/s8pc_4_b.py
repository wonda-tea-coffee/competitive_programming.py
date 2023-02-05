N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 10**100
for i in range(1<<N):
    cost = 0
    mieteru = 1
    left = a[0]
    # print("i: {0:b}".format(i))
    dbg = [left]
    res = False
    for j in range(1, N):
        if left >= a[j]: # a[j]が見えない
            if (i>>j)&1 == 0: # a[j]は見えなくてもいい
                pass
            else: # a[j]を見たい
                d = left - a[j] + 1
                cost += d
                # print("  ", d)
                left = a[j] + d
                dbg.append(left)
                mieteru += 1
        else: # a[j]が見える
            mieteru += 1
            left = a[j]
            dbg.append(left)

        if mieteru == K:
            res = True
            # print("  ", dbg)
            break

    if res:
        ans = min(ans, cost)

print(ans)
