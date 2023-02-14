from itertools import product
from collections import deque

N, M = map(int, input().split())
h = {}
i = 0
while i*i <= M:
    j = (M - i*i)**0.5
    if j == int(j):
        h[i] = int(j)
    i += 1

Q = deque([(1, 1, 0)])
cnt = [[-1]*(N+1) for _ in range(N+1)]
cnt[1][1] = 0
while Q:
    i, j, c = Q.popleft()

    for a in h:
        for sig1, sig2 in product([1, -1], repeat=2):
            k = i + sig1 * h[a]
            l = j + sig2 * a
            if 1 <= k <= N and 1 <= l <= N and cnt[k][l] == -1:
                cnt[k][l] = c+1
                Q.append((k, l, c+1))

for ci in range(1, N+1):
    print(*cnt[ci][1:])
