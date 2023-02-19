N = int(input())
M = 1000000007
ans = 1
for i in range(1, N+1):
    ans = ans * i % M
print(ans)