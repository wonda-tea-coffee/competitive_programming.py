N = int(input())
a = list(map(int, input().split()))
M = 10**5
c = [0]*(M+1)
for ai in a:
    c[ai] += 1
ans = 0
for i in range(1, M):
    ans = max(ans, c[i-1]+c[i]+c[i+1])

print(ans)
