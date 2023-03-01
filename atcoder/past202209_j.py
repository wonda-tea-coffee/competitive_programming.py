from math import *

H, W, D = map(int, input().split())

def f(x):
    return 2*D*D*acos(x/(2*D)) - x*sqrt(D*D - (x/2)**2)

if sqrt(H*H+W*W) <= 2*D:
    print(1)
else:
    ans = D*D*pi
    if 2*D > H: ans -= f(H)
    if 2*D > W: ans -= f(W)
    print(ans/(H*W))
