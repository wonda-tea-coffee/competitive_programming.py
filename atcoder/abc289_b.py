def rev(a, s, e):
    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1

N, M = map(int, input().split())
a = list(map(int, input().split()))
ans = list(range(1, N+1))

if M == 0:
    print(*ans)
    exit()

s = a[0]
mae = a[0]
for i in range(1, M):
    if mae + 1 == a[i]:
        mae = a[i]
    else:
        # sからa[i]+1を逆順にする
        # print("s:", s, "a[i]+1:", a[i]+1)
        # print(*ans)
        rev(ans, ans.index(s), ans.index(mae+1))
        # print(*ans)
        s = a[i]
        mae = a[i]

rev(ans, ans.index(s), ans.index(mae+1))

print(*ans)
