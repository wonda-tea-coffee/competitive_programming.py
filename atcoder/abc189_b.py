import sys

N, X = map(int, input().split())
al = 0
for i in range(1, N+1):
    v, p = map(int, input().split())
    al += v*p
    if al > 100*X:
        print(i)
        sys.exit(0)

print(-1)
