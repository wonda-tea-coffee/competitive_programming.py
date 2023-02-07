N = int(input())
p = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x_1, y_1 = p[i]
    for j in range(i+1, N):
        x_2, y_2 = p[j]
        if abs((y_1 - y_2)/(x_1 - x_2)) <= 1:
            # print(i, j)
            ans += 1

print(ans)
# y_1 = ax_1 + b
# y_2 = ax_2 + b
# y_1 - y_2 = a(x_1 - x_2)
# a = (x_1 - x_2)/(y_1 - y_2)