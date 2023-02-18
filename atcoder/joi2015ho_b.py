import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

def dfs(i, j, turn):
    if dp[i][j] >= 0: return dp[i][j]

    if i == j:
        if turn:
            dp[i][j] = A[i]
            return A[i]
        else:
            return 0

    ret = 0
    di, dj = (i + 1) % N, j - 1 if j - 1 >= 0 else N - 1
    if turn:
        ret = max(dfs(di, j, not turn) + A[i], dfs(i, dj, not turn) + A[j])
    else:
        if A[i] > A[j]:
            ret = dfs(di, j, not turn)
        else:
            ret = dfs(i, dj, not turn)

    dp[i][j] = ret
    return ret

ans = 0
for x in range(N):
    s, e = (x + 1) % N, x - 1 if x - 1 >= 0 else N - 1
    ans = max(ans, dfs(s, e, False) + A[x])
print(ans)
