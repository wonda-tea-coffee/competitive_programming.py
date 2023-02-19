from collections import deque

R, C  = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())
S = [input() for _ in range(R)]

Q = deque([(sy, sx, 0)])
done = set()
while Q:
    y, x, step = Q.popleft()
    # print(y, x, step)

    if y == gy and x == gx:
        print(step)
        exit()

    if (y, x) in done: continue
    done.add((y, x))

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C and S[ny][nx] == "." and not (ny, nx) in done:
            Q.append((ny, nx, step+1))
