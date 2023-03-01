from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

for i in range(H):
    if A.count("#.#") > 0:
        print("Impossible")
        exit()

r = 0
for i in range(1, H):
    ri = A[i-1].rindex("#")
    li = A[i].index("#")
    if li < ri:
        print("Impossible")
        exit()

print("Possible")
