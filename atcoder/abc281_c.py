N, T = map(int, input().split())
A = list(map(int, input().split()))
T %= sum(A)
s = 0
for i in range(N):
    if s + A[i] >= T:
        print(i+1, T-s)
        exit()
    else:
        s += A[i]
