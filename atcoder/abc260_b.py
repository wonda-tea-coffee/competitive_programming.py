N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = (-A[i], i+1)
B = list(map(int, input().split()))
for i in range(N):
    B[i] = (-B[i], i+1)
C = []
for i in range(N):
    C.append((A[i][0]+B[i][0], i+1))

A.sort()
B.sort()
C.sort()

ans = set()
for i1 in range(X):
    ans.add(A[i1][1])

i2 = 0
y = 0
while y < Y:
    if not B[i2][1] in ans:
        ans.add(B[i2][1])
        y += 1
        if y == Y: break
    i2 += 1

i3 = 0
z = 0
while z < Z and i3 < N:
    if not C[i3][1] in ans:
        ans.add(C[i3][1])
        z += 1
        if z == Z: break
    i3 += 1

for ai in sorted(list(ans)):
    print(ai)
