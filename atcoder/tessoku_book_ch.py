N = int(input())
M = 1500
S = [[0]*(M+2) for _ in range(M+2)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    S[A][B] += 1
    S[A][D] -= 1
    S[C][B] -= 1
    S[C][D] += 1
for i in range(M+1):
    for j in range(M):
        S[i][j+1] += S[i][j]
for i in range(M):
    for j in range(M+1):
        S[i+1][j] += S[i][j]

ans = 0
for i in range(M+1):
    for j in range(M+1):
        if S[i][j] > 0: ans += 1
print(ans)
