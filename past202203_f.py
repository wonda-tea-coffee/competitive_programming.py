import sys

H, W, N = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

C = list(map(int, input().split()))
color = [[-1]*W for i in range(H)]

# 色を塗る
for i in range(H):
    for j in range(W):
        color[i][j] = C[A[i][j]-1]

# チェック
v = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(H):
    for j in range(W):
        for dy, dx in v:
            ni = i + dy
            nj = j + dx
            if ni < 0 or nj < 0 or ni >= H or nj >= W: continue
            if A[i][j] == A[ni][nj]: continue

            # print(i, j, ni, nj)
            if color[i][j] == color[ni][nj]:
                print("No")
                sys.exit()

print("Yes")
