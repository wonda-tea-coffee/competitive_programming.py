N = int(input())
X = []
Y = []
for _ in range(N):
    xi, yi = map(int, input().split())
    X.append(xi)
    Y.append(yi)
ALL = 1<<N
dp = [[10**10]*N for _ in range(ALL)]
dp[0][0] = 0
for bit in range(ALL):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if (bit>>j)&1 == 1: continue

            to = bit | (1<<j)
            dp[to][j] = min(dp[to][j], dp[bit][i] + ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5)

print(dp[-1][0])
