import math

n = int(input())
if n*math.log(2, 10) > 2*math.log(n, 10):
    print("Yes")
else:
    print("No")