N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 10**100] + list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(2, N+1):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

print(dp[-1])
