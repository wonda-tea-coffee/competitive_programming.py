import copy
from collections import deque

H, W = map(int, input().split())
S = []
dot = 0
for _ in range(H):
    si = input()
    dot += si.count(".")
    S.append(list(si))

sy = -1
sx = -1
found = False
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            sy = i
            sx = j
            found = True
            break
    if found:
        break

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".": continue

        T = copy.deepcopy(S)
        T[i][j] = "."
        done = set([(i, j)])
        Q = deque([(i, j)])
        while Q:
            y, x = Q.popleft()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and T[ny][nx] == "." and not (ny, nx) in done:
                    done.add((ny, nx))
                    Q.append((ny, nx))

        if len(done) == dot+1:
            ans += 1

print(ans)
