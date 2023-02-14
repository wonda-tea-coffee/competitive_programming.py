from collections import *

def solve(c, h, w):
    ret = 0
    done = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if done[i][j] or c[i][j] == 0: continue

            ret += 1
            Q = deque([(i, j)])
            while Q:
                y, x = Q.popleft()
                done[y][x] = True

                for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < h and 0 <= nx < w and c[ny][nx] == 1 and not done[ny][nx]:
                        done[ny][nx] = True
                        Q.append((ny, nx))
    return ret

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    c = []
    for i in range(h):
        c.append(list(map(int, input().split())))
    print(solve(c, h, w))
