from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(lambda x: int(x)-1, input().split())
ans = 0

G = [[False]*9 for _ in range(9)]
G[A][B] = True

d = []
for i in range(1, 4):
    s = input()
    for j in range(1, 4):
        if s[j-1] == "#":
            d.append((i-2, j-2))

# print(d)

Q = deque([(A, B)])
while Q:
    y, x = Q.popleft()
    ans += 1
    # print(y, x)
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 9 and 0 <= nx < 9 and not G[ny][nx]:
            G[ny][nx] = True
            Q.append((ny, nx))

print(ans)
