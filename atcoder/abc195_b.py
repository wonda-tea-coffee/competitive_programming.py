import math

A, B, W = map(int, input().split())
W *= 1000

if W > W//A*B:
    print("UNSATISFIABLE")
else:
    print(math.ceil(W/B), W//A)
