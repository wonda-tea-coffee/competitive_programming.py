S = input()
T = input()
lens = len(S)
lent = len(T)
dp = [[0]*(lent+1) for _ in range(lens+1)]

for i in range(lens):
    for j in range(lent):
        if S[i] != T[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

print(dp[-1][-1])
