import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solve(a, b, c):
    return a - a//b - a//c + a//lcm(b, c)

A, B, C, D = map(int, input().split())
print(solve(B, C, D) - solve(A-1, C, D))
