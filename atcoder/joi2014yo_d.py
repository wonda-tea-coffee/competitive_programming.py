N = int(input())
S = list(map(lambda x: {"J":0,"O":1,"I":2}[x], list(input())))
MOD = 10007

dp = [0]*8
for i in range(8):
    res = True
    for j in {0, S[0]}:
        if (i>>j)&1 == 0:
            res = False
            break
    if res:
        dp[i] = 1

for i in range(1, N):
    ndp = [0]*8
    # dp[j]からndp[k]への遷移を考える
    for j in range(8):
        if dp[j] == 0: continue
        for k in range(8):
            # 前日と同じ人がいない
            if j & k == 0: continue
            # 指定された人がいない
            if (k>>S[i]) & 1 == 0: continue
            ndp[k] += dp[j]
            ndp[k] %= MOD
    dp = ndp

print(sum(dp) % MOD)
