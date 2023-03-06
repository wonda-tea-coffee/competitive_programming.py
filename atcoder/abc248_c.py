import sys
sys.setrecursionlimit(10000000)

memo = {}
def solve(n, k):
    if (n, k) in memo: return memo[(n, k)]

    if n == 1:
        if 1 <= k <= M:
            return 1
        else:
            return 0

    ret = 0
    for i in range(1, M+1):
        if i > k: break
        ret = (ret + solve(n-1, k-i)) % MOD

    memo[(n, k)] = ret
    return ret

N, M, K = map(int, input().split())
MOD = 998244353

ans = 0
for k in range(1, K+1):
    ans = (ans + solve(N, k)) % MOD
print(ans)
