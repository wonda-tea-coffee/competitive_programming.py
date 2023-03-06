import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

N, A, B = map(int, input().split())
a = N//A
b = N//B
C = lcm(A, B)
c = N//C
ans1 = N*(N+1)//2
ans2 = A*a*(a+1)//2
ans3 = B*b*(b+1)//2
ans4 = C*c*(c+1)//2
print(ans1 - ans2 - ans3 + ans4)
