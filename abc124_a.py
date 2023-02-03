A = sorted(list(map(int, input().split())))

a = A[1]
A[1] -= 1
A.sort()
print(a + A[1])
