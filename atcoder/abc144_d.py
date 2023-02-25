from math import *

a, b, x = map(int, input().split())
S = a*a*b
if 2*x <= S:
    ans = atan(a*b*b/(2*x))
else:
    ans = atan((2*a*a*b-2*x)/a**3)

print(ans*180/pi)
