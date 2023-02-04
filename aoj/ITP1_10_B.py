import math

def heron(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


a, b, C = map(int, input().split())
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C*math.pi/180))

S = heron(a, b, c)
L = a + b + c
h = 2*S/a

print(S)
print(L)
print(h)
