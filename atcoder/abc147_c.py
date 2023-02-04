def count_bit(n):
    ret = 0
    while n > 0:
        ret += n & 1
        n >>= 1
    return ret

N = int(input())
P = []
for _ in range(N):
    ai = int(input())
    q = []
    for i in range(ai):
        x, y = map(int, input().split())
        x -= 1
        q.append((x, y))
    P.append(q)

ans = 0

for i in range(1<<N):
    res = True
    for j in range(N):
        # 真偽不明な人の証言は無視
        if (i >> j) & 1 == 0: continue

        for x, y in P[j]:
            if (i >> x) & 1 != y:
                res = False
                break
        if not res:
            break

    if res:
        ans = max(ans, count_bit(i))

print(ans)
