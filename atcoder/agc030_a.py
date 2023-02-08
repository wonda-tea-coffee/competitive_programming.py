A, B, C = map(int, input().split())
c1 = min(A, C)
C -= c1

if C > 0:
    if B >= C:
        print(c1 + B + C)
    else: # B < C
        print(c1 + 2*B + 1)
else:
    print(c1 + B)