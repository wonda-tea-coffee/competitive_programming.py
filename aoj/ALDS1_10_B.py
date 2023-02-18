N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[float("inf")]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for len in range(2, N+1):
    # print("len:", len)
    for i in range(N-len+1):
        j = i+len-1
        # print("  i ~ j = %d ~ %d" % (i, j))
        for k in range(i, j):
            # [i, j] = min([i, k],[k+1, j])(k=1,2,...,j)
            # print("      i ~ k = %d ~ %d" % (i, k))
            # print("    k+1 ~ j = %d ~ %d" % (k+1, j))
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + M[i][0]*M[k][1]*M[j][1])

# print(dp)
print(dp[0][-1])
