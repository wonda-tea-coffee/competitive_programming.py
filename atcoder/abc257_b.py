import bisect

N, K, Q = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
L = list(map(lambda x: int(x)-1, input().split()))

for i in range(Q):
    if A[L[i]] == N - 1: continue
    b = A[L[i]] + 1
    if not b in A:
        A[L[i]] += 1

print(*map(lambda x: x+1, A))
