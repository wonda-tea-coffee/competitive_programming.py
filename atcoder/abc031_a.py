A, D = map(int, input().split())
if A < D:
    A, D = D, A
print(A * (D + 1))