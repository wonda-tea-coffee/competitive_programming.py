A = sorted(list(map(int, input().split())))
if A[0]%2==0 or A[1]%2==0 or A[2]%2==0:
    print(0)
else:
    print(A[0]*A[1])