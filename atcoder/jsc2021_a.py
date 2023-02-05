import math

X, Y, Z = map(int, input().split())

d = int(Y/X*Z)

if d/Z >= Y/X:
    d -= 1

print(d)