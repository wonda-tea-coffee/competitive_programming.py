N = int(input())
s = [int(input()) for _ in range(N)]
M = 10000
dp = [False]*(M+1)
dp[0] = True
for si in s:
    ndp = list(dp)
    for i in range(M+1):
        if i + si <= M:
            ndp[i + si] |= dp[i]
    dp = ndp

for i in range(M, -1, -1):
    if not dp[i] or i % 10 == 0: continue
    print(i)
    exit()

print(0)
