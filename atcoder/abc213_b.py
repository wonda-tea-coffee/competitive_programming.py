N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] = (A[i], i+1)

A.sort()
print(A[-2][1])
