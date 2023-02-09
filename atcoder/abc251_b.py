from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))
s = set()

for i in range(1, 4):
    for a in combinations(A, i):
        t = sum(a)
        if t <= W:
            s.add(t)

print(len(s))
