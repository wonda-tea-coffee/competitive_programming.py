s = int(input())
ans = 2
seen = set([s])
while True:
    if s % 2 == 0:
        s //= 2
    else:
        s = 3*s + 1
    if s in seen:
        print(ans)
        break
    else:
        seen.add(s)
    ans += 1
