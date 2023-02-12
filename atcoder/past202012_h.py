from collections import deque

H, W = map(int, input().split())
N = H * W
r, c = map(int, input().split())
at = (r - 1) * W + (c - 1)
s = "".join([input() for _ in range(H)])
g = [[] for _ in range(N)]

for i in range(H):
    for j in range(W):
        x = i * W + j
        if s[x] in ".^" and i > 0:
            g[x - W].append(x)
        if s[x] in ".<" and j > 0:
            g[x - 1].append(x)
        if s[x] in ".>" and j + 1 < W:
            g[x + 1].append(x)
        if s[x] in ".v" and i + 1 < H:
            g[x + W].append(x)

reachable = [False] * N
reachable[at] = True
q = deque([at])
while q:
    at = q.popleft()
    for i in g[at]:
        if not reachable[i]:
            reachable[i] = True
            q.append(i)

for i in range(H):
    for j in range(W):
        x = i * W + j
        if s[x] == "#":
            print("#", end="")
        elif reachable[x]:
            print("o", end="")
        else:
            print("x", end="")
    print()
