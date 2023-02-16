from collections import deque

W = int(input())
H = int(input())
S = []
for _ in range(H):
    S.append(list(map(bool, map(int, input().split()))))

ans = 0
for i in range(H):
    for j in range(W):
        if not S[i][j]: continue

        deq = deque([(i, j, 1, set([(i, j)]))])
        while deq:
            y, x, step, visited = deq.pop()

            if step > ans:
                ans = step

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] and not (ny, nx) in visited:
                    deq.append((ny, nx, step+1, visited|{(ny, nx)}))

print(ans)
