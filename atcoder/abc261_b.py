import sys

N = int(input())
A = []
for _ in range(N):
    A.append(input())
for i in range(N):
    for j in range(i+1, N):
        if {A[i][j], A[j][i]} == {"W", "L"} or A[i][j] == A[j][i] == "D":
            pass
        else:
            print("incorrect")
            sys.exit(0)

print("correct")
