A, B, C = map(int, input().split())

while A > B*C:
    A -= 1

if A > B*C:
    print(C)
else:
    print(A / B)
