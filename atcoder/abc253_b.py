H, W = map(int, input().split())
o = []
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == "o":
            o.append((i, j))

print(abs(o[0][0] - o[1][0]) + abs(o[0][1] - o[1][1]))
