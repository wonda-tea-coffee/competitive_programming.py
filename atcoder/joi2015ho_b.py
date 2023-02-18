# オリジナル
# https://at274.hatenablog.com/entry/2020/04/09/224749

import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

def dfs(i, j, picked):
    if dp[i][j] > 0: return dp[i][j]

    if i == j:
        if picked == 0:
            dp[i][j] = A[i]
            return dp[i][j]
        else:
            return 0

    di, dj = (i + 1) % N, j - 1 if j - 1 >= 0 else N - 1
    if picked == 0:
        ret = max(dfs(di, j, 1) + A[i], dfs(i, dj, 1) + A[j])
    else:
        if A[i] > A[j]:
            ret = dfs(di, j, 0)
        else:
            ret = dfs(i, dj, 0)

    dp[i][j] = ret
    return ret

ans = 0
for x in range(N):
    s = (x + 1) % N
    e = x - 1 if x - 1 >= 0 else N - 1
    r = dfs(s, e, 1) + A[x]
    ans = max(ans, r)
print(ans)
