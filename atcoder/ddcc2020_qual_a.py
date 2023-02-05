X, Y = map(int, input().split())
ans = 0
if X <= 3:
    ans += 100000*(4-X)
if Y <= 3:
    ans += 100000*(4-Y)
if X==Y==1: ans += 400000
print(ans)