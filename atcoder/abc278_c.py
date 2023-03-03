import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N, Q = map(int, input().split())
E = defaultdict(set)

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        E[A].add(B)
    elif T == 2:
        if B in E[A]:
            E[A].remove(B)
    else:
        if B in E[A] and A in E[B]:
            print("Yes")
        else:
            print("No")
