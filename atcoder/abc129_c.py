N, M = map(int, input().split())
broken = [False]*(N+1)
for _ in range(M):
    a = int(input())
    broken[a] = True
dp = [0]*(N+1)
dp[0] = 1

if N >= 1 and not broken[1]:
    dp[1] = 1

for i in range(2, N+1):
    if broken[i]: continue
    dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_007

# print(dp)
print(dp[-1])
