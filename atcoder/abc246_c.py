import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, X = map(int, input().split())
A = list(map(int, input().split()))
suma = sum(A)

c = 0
k = 0
for i in range(N):
    t = A[i]//X
    if t == 0: continue
    if k+t <= K:
        c += X*t
        k += t
        A[i] %= X
        if k == K: break
    else:
        t = K-k
        c += X*t
        k += t
        A[i] -= X*t
        break

A.sort(reverse=True)
i = 0
while i < N and k < K:
    c += A[i]
    k += 1
    i += 1

print(suma - c)
