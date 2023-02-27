H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
S = [[0]*(W+1)]
for i in range(H):
    si = [0]
    for j in range(W):
        si.append(si[-1] + X[i][j])
    S.append(si)
for i in range(H):
    for j in range(W+1):
        S[i+1][j] += S[i][j]

# print(S)

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = S[C][D] + S[A-1][B-1] - S[C][B-1] - S[A-1][D]
    print(ans)
