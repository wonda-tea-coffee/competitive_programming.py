N = int(input())
A = [-1] + list(map(int, input().split()))

ans = []
for i in range(1, N+1):
    c = 1
    t = A[i]
    while t != i:
        t = A[t]
        c += 1
    ans.append(c)

print(*ans)
