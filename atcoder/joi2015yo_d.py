import copy

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

INF = 10**10
dp = [INF]*(N+1)
dp[0] = 0
for i in range(M):
    ndp = copy.deepcopy(dp)
    for j in range(N+1):
        # 待機する
        ndp[j] = min(ndp[j], dp[j])

        if j > 0:
            ndp[j] = min(ndp[j], dp[j-1] + C[j-1]*D[j-1])

    dp = ndp

print(dp[-1])
