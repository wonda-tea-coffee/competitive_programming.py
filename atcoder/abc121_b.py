N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
    c = C
    A = list(map(int, input().split()))
    for i in range(M):
        c += A[i] * B[i]
    if c > 0:
        ans += 1

print(ans)