import sys

N = int(input())
p = list(map(int, input().split()))
q = list(range(1, N+1))

if p == q:
    print("YES")
    sys.exit(0)

for i in range(N):
    for j in range(i+1, N):
        p[i], p[j] = p[j], p[i]
        if p == q:
            print("YES")
            sys.exit(0)
        p[i], p[j] = p[j], p[i]

print("NO")