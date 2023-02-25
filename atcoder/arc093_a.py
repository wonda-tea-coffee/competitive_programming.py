N = int(input())
A = [0] + list(map(int, input().split())) + [0]
allsum = 0
for i in range(1, N+2):
    allsum += abs(A[i] - A[i-1])

ans = []
for i in range(1, N+1):
    print(allsum - abs(A[i-1] - A[i]) - abs(A[i] - A[i+1]) + abs(A[i-1] - A[i+1]))
