M = 998244353
A, B, C, D, E, F = map(lambda x: int(x)%M, input().split())
print((A*B*C - D*E*F) % M)
