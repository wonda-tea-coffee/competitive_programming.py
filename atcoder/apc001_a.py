import sys

X, Y = map(int, input().split())

if X % Y == 0:
    print(-1)
    sys.exit(0)

print(X * Y - X)