from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
d = defaultdict(int)

for di in D:
    d[di] += 1

for ti in T:
    if ti in d and d[ti] > 0:
        d[ti] -= 1
    else:
        exit(print("NO"))

print("YES")
