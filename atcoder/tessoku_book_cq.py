N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False]*(S+1) for _ in range(N+1)]

for i in range(N):
    dp[i][0] = True
    for j in range(S+1):
        dp[i+1][j] |= dp[i][j]
        if j+A[i] <= S:
            dp[i+1][j+A[i]] |= dp[i][j]

if not dp[-1][S]:
    print(-1)
    exit()

ans = []
s = S
for i in range(N, -1, -1):
    if s-A[i-1] >= 0 and dp[i-1][s-A[i-1]]:
        ans.append(i)
        s -= A[i-1]

print(len(ans))
print(*ans[::-1])
