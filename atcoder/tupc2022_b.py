N, M, K = map(int, input().split())
ab = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(M)]

if ab[-1][0] != N:
    ab += [(N, 0)]

yuki = 0
ans = 0
for i in range(1, len(ab)):
    # 何日間空いたか
    bet = ab[i][0] - ab[i-1][0]
    # yuki-1,...,yuki-(bet-1)
    # yuki-n >= K
    # -n >= K - yuki
    # n <= yuki - K
    # n <= bet-1
    ans += max(min(yuki-K, bet-1), 0)
    yuki = max(yuki-(bet-1), 0)

    yuki += ab[i][1]-1
    if yuki >= K: ans += 1

print(ans)
