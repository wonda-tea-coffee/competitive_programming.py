import math

A, B = map(int, input().split())
d = math.sqrt(A*A + B*B)
print(A/d, B/d)