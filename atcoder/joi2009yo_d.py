import sys
sys.setrecursionlimit(1000000)

w = int(input())
h = int(input())
s = []
for _ in range(h):
    s.append(list(map(bool, map(int, input().split()))))
ans = 0

def dfs(y, x, step, path):
    global ans

    ans = max(ans, step)
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and s[ny][nx] and not (ny, nx) in path:
            dfs(ny, nx, step+1, path|{(ny, nx)})

for i in range(h):
    for j in range(w):
        if not s[i][j]: continue
        dfs(i, j, 1, {(i, j)})

print(ans)
