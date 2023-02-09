import sys

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
h = {}
for i in range(M):
    x, y = map(int, input().split())
    h[x] = y

for i in range(N-1):
    if T - A[i] <= 0:
        print("No")
        sys.exit(0)

    T -= A[i]
    if i+2 in h:
        T += h[i+2]

print("Yes")
