H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

seen = set([A[0][0]])
ans = 0
def dfs(y, x):
    global ans

    if y == H-1 and x == W-1:
        ans += 1
        return

    for dy, dx in [(0, 1), (1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W and not A[ny][nx] in seen:
            seen.add(A[ny][nx])
            dfs(ny, nx)
            seen.remove(A[ny][nx])

dfs(0, 0)

print(ans)
