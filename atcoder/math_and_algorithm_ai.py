N, Q = map(int, input().split())
A = list(map(int, input().split()))
D = [0]
for ai in A:
    D.append(D[-1] + ai)

res = []
for _ in range(Q):
    L, R = map(int, input().split())
    res.append(D[R] - D[L-1])

for r in res:
    print(r)