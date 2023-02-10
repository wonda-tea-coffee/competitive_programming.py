import sys

N = int(input())
A = sorted(list(map(int, input().split())))
p = 1
M = 10**18
for ai in A:
    p *= ai
    if p > M:
        print(-1)
        sys.exit(0)

print(p)
