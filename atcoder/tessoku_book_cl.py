N, K = map(int, input().split())
A = list(map(int, input().split()))

D = [0]
for ai in A:
    D.append(D[-1] + ai)

R = [0]*N
for i in range(N):
    if i > 0: R[i] = R[i-1]
    while R[i] <= N and D[R[i]] - D[i] <= K:
        R[i] += 1
    R[i] -= 1

ans = 0
for i in range(N):
    ans += R[i] - i
print(ans)
