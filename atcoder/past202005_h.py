N, L = map(int, input().split())
H = [False]*(L+1)
x = list(map(int, input().split()))
for xi in x: H[xi] = True
T1, T2, T3 = map(int, input().split())
dp = [float("inf")]*(L+1)
dp[0] = 0

for i in range(1, L+1):
    dp[i] = dp[i-1] + T1
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + T1 + T2)
    if i >= 4:
        dp[i] = min(dp[i], dp[i-4] + T1 + 3*T2)
    if H[i]:
        dp[i] += T3

ans = dp[L]
for i in [L-1, L-2, L-3]:
    if i >= 0:
        ans = min(ans, dp[i] + T1//2 + T2*(2*(L-i)-1)//2)
print(ans)
