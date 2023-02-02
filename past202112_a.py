import sys
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
h, w = map(int, input().split())

if h >= H and w <= W:
    print("Yes")
else:
    print("No")
