A = int(input())
B = int(input())
C = int(input())
D = sorted([A, B, C])
for i in [A, B, C]:
    print(3-D.index(i))
