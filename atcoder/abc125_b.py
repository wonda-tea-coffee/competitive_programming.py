N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(1<<N):
    c = 0
    for j in range(N):
        if (i>>j)&1 == 1:
            c += V[j] - C[j]
    ans = max(ans, c)

print(ans)
