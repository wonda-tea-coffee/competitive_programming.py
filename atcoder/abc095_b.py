N, X = map(int, input().split())
m = []
for _ in range(N):
    m.append(int(input()))
m.sort()

ans = 0
for mi in m:
    if X - mi >= 0:
        X -= mi
        ans += 1
    else:
        break

print(ans + X//m[0])