N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(set(A))
max1 = B[-1]
f = A.count(max1) > 1
max2 = -1
if len(B) > 1:
    max2 = B[-2]

for ai in A:
    if ai == max1:
        if f:
            print(max1)
        else:
            print(max2)
    else:
        print(max1)
