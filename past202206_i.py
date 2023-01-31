# PyPy3でないと通らない

import sys
from collections import deque

input = sys.stdin.readline
H, W = map(int, input().split())

S = []
for i in range(H):
    S.append(input())

M = 51
M2 = M*M
M3 = M2*M
dist = [-1] * (M3*M)

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            sy, sx = i, j
        elif S[i][j] == "a":
            ay, ax = i, j

def valtoidx(a, b, c, d):
    return a*M3 + b*M2 + c*M + d

def idxtoval(idx):
    idx1 = idx//M2
    idx2 = idx%M2
    return idx1//M, idx1%M, idx2//M, idx2%M

sval = valtoidx(sy, sx, ay, ax)
dist[sval] = 0
que = deque()
que.append(sval)
v = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while que:
    pidx = que.popleft()
    d = dist[pidx]
    py, px, pay, pax = idxtoval(pidx)

    # print(py, px, pay, pax)

    if S[pay][pax] == "g":
        print(d)
        sys.exit()

    for dy, dx in v:
        ny = py + dy
        nx = px + dx

        if 0 <= ny < H and 0 <= nx < W:
            if S[ny][nx] == "#": continue

            if ny == pay and nx == pax:
                nay, nax = pay + dy, pax + dx
                if 0 <= nay < H and 0 <= nax < W:
                    if S[nay][nax] == "#": continue

                    nidx = valtoidx(pay, pax, nay, nax)
                    if dist[nidx] == -1:
                        dist[nidx] = d + 1
                        que.append(nidx)
            else:
                nidx = valtoidx(ny, nx, pay, pax)
                if dist[nidx] == -1:
                    dist[nidx] = d + 1
                    que.append(nidx)

print(-1)
