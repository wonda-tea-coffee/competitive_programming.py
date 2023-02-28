from collections import deque

A, B = map(lambda x: int(x)-1, input().split())
S = [list(input()) for _ in range(3)]
v = []
for i in range(3):
    for j in range(3):
        if S[i][j] == ".": continue
        v.append((i-1, j-1))

ans = 0
que = deque([(A, B)])
seen = [[False]*9 for _ in range(9)]
seen[A][B] = True
while que:
    x, y = que.popleft()
    # print(x, y)
    ans += 1

    for dx, dy in v:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 9 and 0 <= ny < 9 and not seen[nx][ny]:
            seen[nx][ny] = True
            que.append((nx, ny))

print(ans)
