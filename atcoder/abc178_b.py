a, b, c, d = map(int, input().split())

s = [a, b]
if a <= 0 and 0 <= b: s.append(0)
t = [c, d]
if c <= 0 and 0 <= d: t.append(0)

ans = -10**100
for si in s:
    for ti in t:
        ans = max(ans, si*ti)

print(ans)