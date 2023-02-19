from collections import deque

N, X, Y = map(int, input().split())
v = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)]
kabe = set()
for _ in range(N):
    x, y = map(int, input().split())
    kabe.add((y, x))

Q = deque([(0, 0, 0)])
done = set()
while Q:
    y, x, step = Q.popleft()

    if y == Y and x == X:
        print(step)
        exit()

    if (y, x) in done: continue
    done.add((y, x))

    for dy, dx in v:
        ny = y + dy
        nx = x + dx
        if not (ny, nx) in done and not (ny, nx) in kabe and abs(ny) <= 201 and abs(nx) <= 201:
            Q.append((ny, nx, step+1))

print(-1)
