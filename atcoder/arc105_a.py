import sys

A = list(map(int, input().split()))
s = sum(A)

for i in range(1<<4):
    c = 0
    for j in range(4):
        if (i>>j)&1 == 1:
            c += A[j]
    if s-c == c:
        print("Yes")
        sys.exit(0)

print("No")