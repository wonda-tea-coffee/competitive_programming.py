import math

X, Y = map(int, input().split())

print(max(math.ceil((Y-X)/10), 0))
