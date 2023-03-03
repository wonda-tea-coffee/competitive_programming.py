H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
U = []
V = []
for i in range(W):
    colu = []
    colv = []
    for j in range(H):
        colu.append(S[j][i])
        colv.append(T[j][i])
    U.append(colu)
    V.append(colv)

if sorted(U) == sorted(V):
    print("Yes")
else:
    print("No")