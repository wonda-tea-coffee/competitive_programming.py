N, A, B = map(int, input().split())
dp = [[-1]*(B+1) for _ in range(A+1)]
dp[0][0] = 0
ans = 0

for _ in range(N):
    w, v = map(int, input().split())
    ndp = [[-1]*(B+1) for _ in range(A+1)]

    for i in range(A+1):
        for j in range(B+1):
            if dp[i][j] == -1: continue

            ndp[i][j] = max(ndp[i][j], dp[i][j])
            nv = dp[i][j] + v
            if i+w <= A:
                ndp[i+w][j] = max(ndp[i+w][j], nv)
                ans = max(ans, ndp[i+w][j])
            if j+w <= B:
                ndp[i][j+w] = max(ndp[i][j+w], nv)
                ans = max(ans, ndp[i][j+w])

    dp = ndp

print(ans)
