import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
sy, sx = -1, -1
gy, gx = -1, -1
c = []
for i in range(H):
    ci = input()
    c.append(ci)
    for j in range(W):
        if ci[j] == "s":
            sy, sx = i, j
        elif ci[j] == "g":
            gy, gx = i, j

done = [[False]*W for _ in range(H)]
def dfs(y, x):
    if y == gy and x == gx:
        print("Yes")
        exit()

    if done[y][x]: return
    done[y][x] = True
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W and not done[ny][nx] and c[ny][nx] != "#":
            dfs(ny, nx)

dfs(sy, sx)

print("No")
