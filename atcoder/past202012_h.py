from collections import deque

H, W = map(int, input().split())
r, c = map(lambda x: int(x)-1, input().split())
s = "".join([input() for _ in range(H)])
N = H * W
E = [[] for _ in range(N)]

for i in range(H):
    for j in range(W):
        x = i*W+j
        if i < H-1 and s[x+W] in ".^": E[x].append(x+W)
        if i >   0 and s[x-W] in ".v": E[x].append(x-W)
        if j < W-1 and s[x+1] in ".<": E[x].append(x+1)
        if j >   0 and s[x-1] in ".>": E[x].append(x-1)

reachable = [False]*N
Q = deque([r*W+c])
while Q:
    id = Q.popleft()

    if reachable[id]: continue
    reachable[id] = True

    for nid in E[id]:
        if reachable[nid]: continue
        Q.append(nid)

for i in range(H):
    for j in range(W):
        x = i*W+j
        if s[x] == "#":
            print("#", end="")
        elif reachable[x]:
            print("o", end="")
        else:
            print("x", end="")
    print()
