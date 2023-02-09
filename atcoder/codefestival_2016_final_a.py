import sys

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input().split())

for i in range(H):
    for j in range(W):
        if S[i][j] == "snuke":
            print(str(chr(ord("A") + j)) + "" + str(i+1))
            sys.exit(0)
