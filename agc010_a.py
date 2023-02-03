N = int(input())

A = list(map(int, input().split()))
c = 0
for ai in A:
    if ai % 2 == 1:
        c += 1

if c % 2 == 1:
    print("NO")
else:
    print("YES")
