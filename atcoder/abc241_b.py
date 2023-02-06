import sys
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = defaultdict(lambda: 0)
for ai in A:
    d[ai] += 1

for bi in B:
    if d[bi] > 0:
        d[bi] -= 1
    else:
        print("No")
        sys.exit(0)

print("Yes")