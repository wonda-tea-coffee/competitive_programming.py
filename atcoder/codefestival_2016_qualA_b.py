N = int(input())
a = list(map(int, input().split()))
F = [-1]*N
for i in range(N):
    F[i] = a[i]-1

ans = 0
for i in range(N):
    if i == F[F[i]]:
        ans += 1
print(ans//2)
