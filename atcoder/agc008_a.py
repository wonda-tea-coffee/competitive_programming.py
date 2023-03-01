x, y = map(int, input().split())

ans = 10**10
for i in range(2):
    x0 = x
    if i == 1: x0 = -x0
    for j in range(2):
        c = abs(abs(y) - abs(x))
        x1 = x0 + c
        if j == 1: x1 = -x1
        if x1 == y:
            ans = min(ans, i+j+c)

print(ans)
