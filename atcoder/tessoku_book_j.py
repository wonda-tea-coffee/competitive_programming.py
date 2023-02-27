N = int(input())
A = list(map(int, input().split()))
D = int(input())

lmax = [0]
for i in range(N):
    lmax.append(max(lmax[-1], A[i]))
rmax = [0]
for i in range(N-1, -1, -1):
    rmax.append(max(rmax[-1], A[i]))

for _ in range(D):
    L, R = map(int, input().split())
    print(max(lmax[L-1], rmax[N-R]))
