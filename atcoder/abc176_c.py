N = int(input())
A = list(map(int, input().split()))
ans = 0
h = A[0]
for i in range(1, N):
    if h > A[i]:
        ans += h - A[i]
    else:
        h = A[i]
print(ans)