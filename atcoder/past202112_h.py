S = input()
T = input()
lens = len(S)
lent = len(T)
dp = [[0]*(lent+1) for _ in range(lens+1)]

for si, s in enumerate(S, 1):
    for ti, t in enumerate(T, 1):
        dp[si][ti] = max(dp[si][ti-1], dp[si-1][ti])
        if s != t:
            dp[si][ti] = max(dp[si][ti], dp[si-1][ti-1]+1)

print(dp[-1][-1])
