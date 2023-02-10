n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n-2):
    q = sorted([p[i], p[i+1], p[i+2]])
    if q[1] == p[i+1]:
        ans += 1
print(ans)