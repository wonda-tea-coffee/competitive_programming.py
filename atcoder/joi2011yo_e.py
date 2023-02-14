from collections import deque

H, W, N = map(int, input().split())
S = [input() for _ in range(H)]
T = [None] * (N+1)

for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            T[0] = (i, j)
        elif "1" <= S[i][j] <= "9":
            T[int(S[i][j])] = (i, j)

ans = 0
for i in range(N):
    sy, sx = T[i]
    gy, gx = T[i+1]
    done = set([(sy, sx)])
    Q = deque([(sy, sx, 0)])
    while Q:
        y, x, step = Q.popleft()

        if y == gy and x == gx:
            ans += step
            break

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and not (ny, nx) in done and S[ny][nx] != "X":
                done.add((ny, nx))
                Q.append((ny, nx, step+1))

print(ans)
