n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

maked = set()

for i in range(1<<n):
    s = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            s += A[j]
    maked.add(s)

for mi in m:
    if mi in maked:
        print("yes")
    else:
        print("no")
