N, M = map(int, input().split())
A = []
for _ in range(N):
    K, *Ai = map(int, input().split())
    A.append(set(Ai))

s = A[0]
for i in range(1, N):
    s &= A[i]

print(len(s))
