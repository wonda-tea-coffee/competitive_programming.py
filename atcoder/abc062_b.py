H, W = map(int, input().split())
a = [input() for _ in range(H)]
print("#"*(W+2))
for i in range(H):
    print("#", end="")
    for j in range(W):
        print(a[i][j], end="")
    print("#")
print("#"*(W+2))