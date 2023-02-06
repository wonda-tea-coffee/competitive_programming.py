N = int(input())
S = list(map(int, input().split()))
p = set()
for a in range(1, 143):
    b = a
    while True:
        s = 4*a*b + 3*a + 3*b
        if s > 1000: break
        p.add(s)
        b += 1

ans = 0
for si in S:
    if not si in p:
        ans += 1

print(ans)
