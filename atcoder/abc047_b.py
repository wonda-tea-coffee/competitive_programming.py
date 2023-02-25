W, H, N = map(int, input().split())

x1 = 0
x2 = W
y1 = 0
y2 = H
for _ in range(N):
    xi, yi, ai = map(int, input().split())
    if ai == 1:
        x1 = max(x1, xi)
    elif ai == 2:
        x2 = min(x2, xi)
    elif ai == 3:
        y1 = max(y1, yi)
    else:
        y2 = min(y2, yi)

print(max(x2-x1, 0)*max(y2-y1, 0))
