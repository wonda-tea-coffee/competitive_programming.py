H, W = map(int, input().split())
S = []
T = []
for _ in range(H):
    S.append(input())

v = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(H):
    t = ""
    for j in range(W):
        if S[i][j] == "#":
            t += "#"
            continue

        bomb = 0
        for dy, dx in v:
            ny = i + dy
            nx = j + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#":
                bomb += 1
        t += str(bomb)
    T.append(t)

for i in range(H):
    print(T[i])
