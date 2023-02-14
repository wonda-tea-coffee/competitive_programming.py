from collections import deque

H, W = map(int, input().split())
s = [input() for _ in range(H)]

kabe = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == "#": kabe += 1

Q = deque([(0, 0, 0)])
done = [[False]*W for _ in range(H)]
minstep = -1
while Q:
    y, x, step = Q.popleft()

    if y == H-1 and x == W-1:
        minstep = step
        break

    if done[y][x]: continue
    done[y][x] = True

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W and s[ny][nx] == "." and not done[ny][nx]:
            Q.append((ny, nx, step+1))

if minstep == -1:
    print(-1)
else:
    print(H*W - kabe - (minstep + 1))
