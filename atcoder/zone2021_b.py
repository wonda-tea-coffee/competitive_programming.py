N, D, H = map(int, input().split())
ans = 0
for _ in range(N):
    d, h = map(int, input().split())
    ans = max(ans, h - (H-h)/(D-d)*d)

print(ans)
