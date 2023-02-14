from collections import deque

a, N = map(int, input().split())

Q = deque([(N, 0)])
seen = set()
while Q:
    x, step = Q.popleft()

    if x in seen: continue
    seen.add(x)

    if x == 1:
        exit(print(step))

    sx = str(x)
    if x >= 10 and sx[1] != "0":
        x0 = sx[0]
        x1 = sx[1:]
        Q.append((int(x1 + x0), step+1))

    if x % a == 0:
        Q.append((x//a, step+1))

print(-1)
