# オリジナル
# https://atcoder.jp/contests/joi2017yo/submissions/19853109

N, M = map(int, input().split())
D = [[0] for i in range(M)]
for i in range(N):
    a = int(input())-1
    for m in range(M):
        d = D[m][-1]
        if a == m:
            d += 1
        D[m].append(d)
dp = [10 ** 10 for j in range(1 << M)]
dp[0] = 0

for bit in range(1 << M):
    l = 0
    for m in range(M):
        if bit & (1 << m):
            l += D[m][-1]
    for m in range(M):
        if bit & (1 << m): continue
        r = l + D[m][-1]
        b = D[m][-1] - (D[m][r] - D[m][l])

        to = bit | (1 << m)
        dp[to] = min(dp[to], dp[bit] + b)

print(dp[-1])
