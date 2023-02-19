N = int(input())
p = list(map(int, input().split()))
M = sum(p)
dp = [False]*(M+1)
dp[0] = True

for i in range(N):
    ndp = list(dp)
    for j in range(M+1):
        if j + p[i] <= M:
            ndp[j + p[i]] |= dp[j]
        else:
            break
    dp = ndp

# print(dp)
ans = 0
for i in range(M+1):
    if dp[i]:
        ans += 1
print(ans)