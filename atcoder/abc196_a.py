a, b = map(int, input().split())
c, d = map(int, input().split())
ans = -10**100

for x, y in [(a, c), (b, c), (a, d), (b, d)]:
    ans = max(ans, x - y)

print(ans)
