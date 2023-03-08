N = int(input())
p = list(map(int, input().split()))
d = [0]*N

q = {}
for i in range(N):
    q[p[i]] = i

for i in range(N):
    if q[i] >= i:
        dist = q[i] - i
    else:
        dist = N - i + q[i]
    d[dist] += 1

ans = 0
for i in range(N):
    ans = max(ans, d[i] + d[(i+1)%N] + d[(i+2)%N])
print(ans)
