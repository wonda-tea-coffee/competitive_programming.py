# 一番遅く都市2に着くのはmath.ceil(N/A)
# t秒後に都市iに何人いるか、がわかれば段階的に答えが求められる
import math

N = int(input())
town = [0, N, 0, 0, 0, 0, 0]
v = [0]*2 + [int(input()) for _ in range(5)]

t = 0
while town[6] < N:
    for i in range(6, 0, -1):
        j = min(town[i-1], v[i])
        town[i] += j
        town[i-1] -= j

    t += 1
    print(t, *town)

print(t)
