def lcs(s, t):
    lens = len(s)
    lent = len(t)
    dp = [[0]*(lent+1) for _ in range(lens+1)]
    for i in range(lens):
        for j in range(lent):
            val = [dp[i+1][j], dp[i][j+1]]
            if s[i] == t[j]:
                val.append(dp[i][j] + 1)
            else:
                val.append(dp[i][j])
            dp[i+1][j+1] = max(dp[i+1][j], *val)

    return dp[-1][-1]

N = int(input())
for _ in range(N):
    print(lcs(input(), input()))
