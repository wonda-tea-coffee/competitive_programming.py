N = int(input())
A = list(map(int, input().split()))
d = {}
for i, a in enumerate(sorted({*A}), 1):
    d[a] = i
for a in A:
    print(d[a])
