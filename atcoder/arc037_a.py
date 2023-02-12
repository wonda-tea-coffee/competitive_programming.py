N = map(int, input().split())
m = list(map(int, input().split()))

ans = 0
for mi in m:
    ans += max(80 - mi, 0)

print(ans)