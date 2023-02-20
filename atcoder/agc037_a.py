# 参考
# https://atcoder.jp/contests/agc037/submissions/38763750

S = input()
N = len(S)
dp = [0]*N
dp[0] = 1
if N >= 2:
    if S[0] == S[1]:
        dp[1] = 1
    else:
        dp[1] = 2
if N >= 3:
    if S[0] != S[1] and S[1] != S[2]:
        dp[2] = 3
    else:
        dp[2] = 2

for i in range(3, N):
    if S[i] == S[i-1]:
        dp[i] = dp[i-3] + 2
    else:
        dp[i] = dp[i-1] + 1
print(dp[-1])

#  S:  a  a  a  c  c  a  c  a  b  a  a  b  a  b  c
# dp:  1  1  2  3  3  4  5  6  7  8  8  9 10 11 12