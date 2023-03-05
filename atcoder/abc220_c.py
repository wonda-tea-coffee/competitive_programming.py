N = int(input())
A = list(map(int, input().split()))
X = int(input())

suma = sum(A)
ans = X//suma*N
X %= suma
for i in range(N):
    if A[i] > X:
        print(ans + i+1)
        exit()
    else:
        X -= A[i]
