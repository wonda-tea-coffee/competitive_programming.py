N = int(input())
a = []
b = []
c = []
for _ in range(N):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
dp = [a[0], b[0], c[0]]
for i in range(1, N):
    ndp = [0]*3

    ndp[0] = max(dp[1], dp[2]) + a[i]
    ndp[1] = max(dp[0], dp[2]) + b[i]
    ndp[2] = max(dp[0], dp[1]) + c[i]

    dp = ndp

print(max(dp))
