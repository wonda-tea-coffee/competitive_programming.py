from collections import deque

def print_path(path):
    print(len(path))
    for x, y in path:
        print(x+1, y+1)

H, W = map(int, input().split())
S = []
length = 0
for _ in range(H):
    si = input()
    length += si.count("#")
    S.append(si)

for hi in range(H):
    for wi in range(W):
        if S[hi][wi] == ".": continue

        Q = deque([(hi, wi, [(hi, wi)])])
        while Q:
            x, y, path = Q.popleft()
            if len(path) == length:
                print_path(path)
                exit()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "#" and not (nx, ny) in path:
                    Q.append((nx, ny, path+[(nx, ny)]))
