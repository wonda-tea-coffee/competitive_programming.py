N = int(input())
p = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    if p[i] == i:
        if i < N:
            p[i], p[i+1] = p[i+1], p[i]
        else:
            p[i], p[i-1] = p[i-1], p[i]
        ans += 1
print(ans)
