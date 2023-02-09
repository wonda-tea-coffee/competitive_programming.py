from collections import deque

N = int(input())
A = list(map(int, input().split()))
P = deque([360])

#  90:             [360] -> [90, 270]
# 180:         [90, 270] -> [180, 90, 90]
#  45:     [180, 90, 90] -> [45, 180, 90, 45]
# 195: [45, 180, 90, 45] -> [60, 90, 45, 45, 120]

for ai in A:
    bi = ai
    while bi > P[-1]:
        c = P.pop()
        bi -= c
        P.appendleft(c)

    P[-1] -= bi
    P.appendleft(bi)

print(max(P))