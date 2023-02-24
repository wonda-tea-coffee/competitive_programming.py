H, W, N = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(H)]
C = list(map(int, input().split()))

for y in range(H):
    for x in range(W):
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= H or nx >= W: continue
            if A[y][x] == A[ny][nx]: continue
            if C[A[y][x]] == C[A[ny][nx]]:
                print("No")
                exit()

print("Yes")
