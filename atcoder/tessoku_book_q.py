N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 10**100] + list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(2, N+1):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

ans = [N]
i = N
while i > 1:
    if dp[i] == dp[i-1] + A[i]:
        ans.append(i-1)
        i -= 1
    elif i-2 >= 1 and dp[i] == dp[i-2] + B[i]:
        ans.append(i-2)
        i -= 2

# print(dp)
print(len(ans))
print(*reversed(ans))
