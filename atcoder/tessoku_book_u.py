import sys
sys.setrecursionlimit(1000000)

N = int(input())
P = [0]
A = [0]
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)
block = list(range(N+1))

dp = [[-1]*(N+1) for _ in range(N+1)]
def solve(i, j):
    if dp[i][j] >= 0: return dp[i][j]
    if i == j: return 0

    ret = 0
    # ブロックP[i]が既に取り除かれているか
    if P[i] < i or j < P[i]:
        ret = solve(i+1, j)
    else:
        ret = solve(i+1, j) + A[i]

    # ブロックP[j]が既に取り除かれているか
    if P[j] < i or j < P[j]:
        ret = max(ret, solve(i, j-1))
    else:
        ret = max(ret, solve(i, j-1) + A[j])

    dp[i][j] = ret
    return ret

print(solve(1, N))
