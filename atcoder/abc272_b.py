import sys

N, M = map(int, input().split())
x = []
for _ in range(M):
    ki, *xi = map(int, input().split())
    x.append(set(xi))

for i in range(1, N+1):
    for j in range(i+1, N+1):
        res = False
        for k in range(M):
            res |= i in x[k] and j in x[k]
        if not res:
            print("No")
            sys.exit(0)

print("Yes")
