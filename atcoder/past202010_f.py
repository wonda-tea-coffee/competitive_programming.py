from collections import defaultdict

N, K = map(int, input().split())
d = defaultdict(lambda: 0)

for _ in range(N):
    d[input()] += 1

A = []
for key in d:
    A.append((-d[key], key))
A.sort()

kth = A[K-1]
if (K-2 >= 0 and A[K-2][0] == A[K-1][0]) or (K < len(A) and A[K][0] == A[K-1][0]):
    print("AMBIGUOUS")
else:
    print(kth[1])
