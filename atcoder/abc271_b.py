N, Q = map(int, input().split())
A = []
for _ in range(N):
    L, *a = map(int, input().split())
    A.append(a)

for _ in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    print(A[s][t])
