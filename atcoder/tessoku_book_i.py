H, W, N = map(int, input().split())
S = [[0]*(W+2) for _ in range(H+2)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    S[A][B] += 1
    S[A][D+1] -= 1
    S[C+1][B] -= 1
    S[C+1][D+1] += 1
for i in range(H+1):
    for j in range(W):
        S[i][j+1] += S[i][j]
for i in range(H):
    for j in range(W+1):
        S[i+1][j] += S[i][j]

for i in range(1, H+1):
    print(*S[i][1:-1])
