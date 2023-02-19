N, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
for ai in a:
    if x - ai >= 0:
        ans += 1
        x -= ai
if x == 0:
    print(ans)
elif ans == N:
    print(ans-1)
else:
    print(ans)
