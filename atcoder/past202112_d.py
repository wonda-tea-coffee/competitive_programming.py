N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Q = []
for i in range(N):
    Q.append((-A[i]-B[i], -A[i], i+1))
Q.sort()

for i in range(N):
    print(Q[i][2])
