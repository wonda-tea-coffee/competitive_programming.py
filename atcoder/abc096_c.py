H, W = map(int, input().split())
s = [input() for _ in range(H)]
v = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for y in range(H):
    for x in range(W):
        if s[y][x] == ".": continue
        check = False
        for dy, dx in v:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
            if s[ny][nx] == "#":
                check = True
                break
        if not check:
            print("No")
            exit()

print("Yes")