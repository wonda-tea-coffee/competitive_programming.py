N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [False]*(S+1)
dp[0] = True

for i in range(N):
    ndp = list(dp)
    for j in range(S+1):
        if j+A[i] <= S:
            ndp[j+A[i]] |= dp[j]
    dp = ndp

if dp[S]:
    print("Yes")
else:
    print("No")
