N = int(input())
h = [0] + list(map(int, input().split()))
dp = [0]*(N+1)
dp[2] = abs(h[1] - h[2])
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]), dp[i-2] + abs(h[i]-h[i-2]))

i = N
ans = [N]
while i > 1:
    if dp[i] == abs(h[i] - h[i-1]) + dp[i-1]:
        ans.append(i-1)
        i -= 1
    elif i > 2 and dp[i] == abs(h[i] - h[i-2]) + dp[i-2]:
        ans.append(i-2)
        i -= 2

print(len(ans))
print(*ans[::-1])
