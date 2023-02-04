N = int(input())

G = [[[0]*11 for _ in range(4)] for _ in range(5)]

for _ in range(N):
    b, f, r, v = map(int, input().split())
    G[b][f][r] += v

for i in range(1, 5):
    for j in range(1, 4):
        print(" " + " ".join(map(str, G[i][j][1:])))
    if i < 4:
        print("####################")
