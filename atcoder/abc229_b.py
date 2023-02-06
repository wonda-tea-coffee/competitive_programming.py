import sys

A, B = input().split()
la = len(A)
lb = len(B)
for i in range(1, min(la, lb)+1):
    if int(A[la-i]) + int(B[lb-i]) >= 10:
        print("Hard")
        sys.exit(0)

print("Easy")
