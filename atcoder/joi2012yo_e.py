from collections import deque

def itov(i):
    if i % 2 == 0:
        return [(-1,  0), (-1, 1), (0, -1), (0, 1), (1,  0), (1, 1)]
    else:
        return [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]

def walk(i, j):
    # print("walk", j+1, i+1)
    Q = deque([(i, j)])
    done = [[False]*W for _ in range(H)]
    check[i][j] = True
    while Q:
        y, x = Q.popleft()

        for dy, dx in itov(y):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and not S[ny][nx] and not check[ny][nx]:
                check[ny][nx] = True
                Q.append((ny, nx))

W, H = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(map(bool, map(int, input().split()))))
check = [[False]*W for _ in range(H)]

for i in range(H):
    for j in [0, W-1]:
        if S[i][j]: continue
        if check[i][j]: continue
        walk(i, j)
for i in [0, H-1]:
    for j in range(W):
        if S[i][j]: continue
        if check[i][j]: continue
        walk(i, j)

ans = 0
for i in range(H):
    for j in range(W):
        if not S[i][j]: continue
        c = 0
        for dy, dx in itov(i):
            ny = i + dy
            nx = j + dx
            if not (0 <= ny < H and 0 <= nx < W) or check[ny][nx]:
                # print("  ++", nx+1, ny+1)
                c += 1
            else:
                pass
                # print("  --", nx+1, ny+1)
        # print(j+1, i+1, c)
        ans += c

print(ans)
