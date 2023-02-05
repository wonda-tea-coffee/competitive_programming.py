A = sorted(list(map(int, input().split())))

if A[0]==A[1] and A[2]==A[3]==A[4] or A[0]==A[1]==A[2] and A[3]==A[4]:
    print("Yes")
else:
    print("No")