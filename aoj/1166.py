from collections import deque

ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    W = 2*w-1
    H = 2*h-1
    s = [[-1]*W for _ in range(H)]
    for i in range(H):
        if i % 2 == 0:
            start = 1
        else:
            start = 0

        si = list(map(bool, map(int, input().split())))
        # print("si:", si)
        for sij in si:
            # print(i, sij, start)
            s[i][start] = sij
            start += 2

    Q = deque([(0, 0, 1)])
    done = set()
    # print("s:", s)
    res = 0
    while Q:
        y, x, step = Q.popleft()

        if y == H-1 and x == W-1:
            res = step
            break

        if (y, x) in done: continue
        done.add((y, x))

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy*2
            nx = x + dx*2
            if 0 <= ny < H and 0 <= nx < W and not (ny, nx) in done and not s[y+dy][x+dx]:
                Q.append((ny, nx, step+1))

    ans.append(res)

for a in ans:
    print(a)