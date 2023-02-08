H, W, Y, X = map(int, input().split())
X -= 1
Y -= 1
G = []
for _ in range(H):
    G.append(input())

ans = 1
# print(Y, X)
for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    y = Y
    x = X
    while 0 <= x + dx < W and 0 <= y + dy < H and G[y + dy][x + dx] == ".":
        x += dx
        y += dy
        # print(y, x)
        ans += 1
    # print("out:", G[y][x])

print(ans)
