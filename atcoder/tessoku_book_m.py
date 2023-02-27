N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0]*(N-1)
for i in range(N-1):
    if i == 0:
        R[0] = 0
    else:
        R[i] = R[i-1]

    while R[i] < N and (A[R[i]] - A[i]) <= K:
        R[i] += 1
    R[i] -= 1

ans = 0
# print(*R)
for i in range(N-1):
    ans += R[i] - i
print(ans)
