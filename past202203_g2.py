# 二分探索
a, b, c = map(int, input().split())

def f(x):
    return a*x**5 + b*x + c

l, r = 1.0, 2.0
while r-l > 0.0000000001:
    m = (l+r)/2
    if f(m) >= 0:
        r = m
    else:
        l = m
print(r)
