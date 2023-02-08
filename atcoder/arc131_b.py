H, W = map(int, input().split())
d = []
for _ in range(H):
    d.append(list(input()))

n = {"1", "2", "3", "4", "5"}
for i in range(H):
    for j in range(W):
        if d[i][j] != ".": continue

        s = set()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = i + dy
            nx = j + dx
            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] != ".":
                s.add(d[ny][nx])

        d[i][j] = list(n - s)[0]

for i in range(H):
    print("".join(d[i]))
