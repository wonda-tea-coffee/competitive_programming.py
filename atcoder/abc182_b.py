N = int(input())
A = list(map(int, input().split()))

ans = 0
maxc = 0
for i in range(2, max(A)+1):
    c = 0
    for ai in A:
        if ai % i == 0:
            c += 1
    if c > maxc:
        maxc = c
        ans = i

print(ans)