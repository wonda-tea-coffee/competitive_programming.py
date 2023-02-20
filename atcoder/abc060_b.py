import math

A, B, C = map(int, input().split())

g = math.gcd(A, B)
if C % g == 0:
    print("YES")
else:
    print("NO")
