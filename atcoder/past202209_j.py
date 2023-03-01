from math import *

H, W, D = map(int, input().split())

if D <= W/2:
    if D <= H/2:
        print(pi*D*D/(H*W))
    else:
        pass
else:
    pass
