from math import *

def f(x, y, c, s):
    return c * x + s * y, - s * x + c * y

N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
X, Y = (x1 + x2)/2, (y1 + y2)/2
x2, y2 = x2 - X, y2 - Y
c, s = x2/sqrt(x2 ** 2 + y2 ** 2), y2/sqrt(x2 ** 2 + y2 ** 2)

for _ in range(N):
    A, B = map(int, input().split())
    print(*f(A - X, B - Y, c, s))
