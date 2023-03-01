import math

N = int(input())
A = [0]*(N+1)
B = [0]*(N+1)
for i in range(1, N+1):
    A[i], B[i] = map(int, input().split())

ans = 0
for i in range(N, 0, -1):
    ans += math.ceil((A[i]+ans)/B[i])*B[i] - (A[i]+ans)

print(ans)
